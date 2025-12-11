/**
 * APEXVIPER Common Surveillance Dashboard Scripts
 * Shared JavaScript utilities for all NHL surveillance tools
 */

/**
 * Format timestamp to readable format
 * @param {Date} date - Date object
 * @returns {string} Formatted timestamp
 */
function formatTimestamp(date = new Date()) {
    const options = {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit',
        timeZone: 'America/New_York'
    };
    return date.toLocaleString('en-US', options) + ' EST';
}

/**
 * Update last updated timestamp on page
 */
function updateTimestamp() {
    const timestampElements = document.querySelectorAll('.timestamp, .last-updated');
    timestampElements.forEach(el => {
        el.textContent = `Last Updated: ${formatTimestamp()}`;
    });
}

/**
 * Calculate APEX score color class
 * @param {number} score - APEX score value
 * @returns {string} CSS class name
 */
function getSignalClass(score) {
    if (score >= 0.75) return 'signal-green';
    if (score >= 0.60) return 'signal-yellow';
    return 'signal-red';
}

/**
 * Calculate APEX score signal text
 * @param {number} score - APEX score value
 * @returns {string} Signal description
 */
function getSignalText(score) {
    if (score >= 0.75) return '🟢 GREEN (ELITE)';
    if (score >= 0.60) return '🟡 YELLOW (PLAYABLE)';
    return '🔴 RED (AVOID)';
}

/**
 * Format percentage
 * @param {number} value - Decimal value (0-1)
 * @param {number} decimals - Number of decimal places
 * @returns {string} Formatted percentage
 */
function formatPercentage(value, decimals = 1) {
    return (value * 100).toFixed(decimals) + '%';
}

/**
 * Format currency
 * @param {number} amount - Dollar amount
 * @returns {string} Formatted currency
 */
function formatCurrency(amount) {
    return '$' + amount.toFixed(2);
}

/**
 * Sort table by column
 * @param {HTMLTableElement} table - Table element
 * @param {number} column - Column index to sort by
 * @param {boolean} ascending - Sort direction
 */
function sortTable(table, column, ascending = true) {
    const tbody = table.querySelector('tbody');
    const rows = Array.from(tbody.querySelectorAll('tr'));

    rows.sort((a, b) => {
        const aValue = a.children[column].textContent.trim();
        const bValue = b.children[column].textContent.trim();

        // Try parsing as number
        const aNum = parseFloat(aValue.replace(/[^0-9.-]/g, ''));
        const bNum = parseFloat(bValue.replace(/[^0-9.-]/g, ''));

        if (!isNaN(aNum) && !isNaN(bNum)) {
            return ascending ? aNum - bNum : bNum - aNum;
        }

        // String comparison
        return ascending
            ? aValue.localeCompare(bValue)
            : bValue.localeCompare(aValue);
    });

    // Clear and re-append sorted rows
    rows.forEach(row => tbody.appendChild(row));
}

/**
 * Add click handlers to table headers for sorting
 * @param {string} tableId - ID of table element
 */
function makeTableSortable(tableId) {
    const table = document.getElementById(tableId);
    if (!table) return;

    const headers = table.querySelectorAll('thead th');
    headers.forEach((header, index) => {
        header.style.cursor = 'pointer';
        header.title = 'Click to sort';

        let ascending = true;
        header.addEventListener('click', () => {
            sortTable(table, index, ascending);
            ascending = !ascending;

            // Update header indicator
            headers.forEach(h => h.textContent = h.textContent.replace(' ↑', '').replace(' ↓', ''));
            header.textContent += ascending ? ' ↓' : ' ↑';
        });
    });
}

/**
 * Filter table rows based on search input
 * @param {string} tableId - ID of table element
 * @param {string} searchValue - Search string
 */
function filterTable(tableId, searchValue) {
    const table = document.getElementById(tableId);
    if (!table) return;

    const rows = table.querySelectorAll('tbody tr');
    const search = searchValue.toLowerCase();

    rows.forEach(row => {
        const text = row.textContent.toLowerCase();
        row.style.display = text.includes(search) ? '' : 'none';
    });
}

/**
 * Highlight rows based on condition
 * @param {string} tableId - ID of table element
 * @param {number} column - Column index to check
 * @param {Function} condition - Condition function
 * @param {string} className - CSS class to apply
 */
function highlightRows(tableId, column, condition, className) {
    const table = document.getElementById(tableId);
    if (!table) return;

    const rows = table.querySelectorAll('tbody tr');
    rows.forEach(row => {
        const cell = row.children[column];
        if (cell && condition(cell.textContent)) {
            row.classList.add(className);
        }
    });
}

/**
 * Auto-refresh page after specified interval
 * @param {number} minutes - Refresh interval in minutes
 */
function autoRefresh(minutes = 5) {
    const milliseconds = minutes * 60 * 1000;
    setTimeout(() => {
        location.reload();
    }, milliseconds);

    // Show countdown
    console.log(`Auto-refresh enabled: ${minutes} minutes`);
}

/**
 * Export table to CSV
 * @param {string} tableId - ID of table element
 * @param {string} filename - Output filename
 */
function exportTableToCSV(tableId, filename = 'export.csv') {
    const table = document.getElementById(tableId);
    if (!table) return;

    const rows = table.querySelectorAll('tr');
    const csv = Array.from(rows).map(row => {
        return Array.from(row.querySelectorAll('th, td'))
            .map(cell => `"${cell.textContent.trim()}"`)
            .join(',');
    }).join('\n');

    // Download CSV
    const blob = new Blob([csv], { type: 'text/csv' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = filename;
    a.click();
    URL.revokeObjectURL(url);
}

/**
 * Calculate bankroll percentage
 * @param {number} amount - Bet amount
 * @param {number} bankroll - Total bankroll
 * @returns {string} Percentage string
 */
function calculateBankrollPercentage(amount, bankroll) {
    const percentage = (amount / bankroll) * 100;
    return percentage.toFixed(2) + '%';
}

/**
 * Validate bet size against bankroll limits
 * @param {number} betAmount - Proposed bet amount
 * @param {number} bankroll - Current bankroll
 * @param {number} maxPercentage - Maximum percentage allowed (default 5%)
 * @returns {Object} Validation result
 */
function validateBetSize(betAmount, bankroll, maxPercentage = 5) {
    const percentage = (betAmount / bankroll) * 100;
    const maxAmount = (bankroll * maxPercentage) / 100;

    return {
        isValid: percentage <= maxPercentage,
        percentage: percentage,
        maxAllowed: maxAmount,
        message: percentage > maxPercentage
            ? `Bet exceeds ${maxPercentage}% limit`
            : 'Bet size OK'
    };
}

/**
 * Initialize common dashboard features
 */
function initializeDashboard() {
    // Update timestamp on load
    updateTimestamp();

    // Make tables sortable
    document.querySelectorAll('table[data-sortable="true"]').forEach(table => {
        makeTableSortable(table.id);
    });

    // Log initialization
    console.log('🐍 APEXVIPER Dashboard initialized');
    console.log(`Timestamp: ${formatTimestamp()}`);
}

// Auto-initialize when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initializeDashboard);
} else {
    initializeDashboard();
}

// Export functions for use in other scripts
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        formatTimestamp,
        updateTimestamp,
        getSignalClass,
        getSignalText,
        formatPercentage,
        formatCurrency,
        sortTable,
        makeTableSortable,
        filterTable,
        highlightRows,
        autoRefresh,
        exportTableToCSV,
        calculateBankrollPercentage,
        validateBetSize
    };
}
