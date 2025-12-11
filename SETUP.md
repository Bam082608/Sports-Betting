# 🐍 APEXVIPER Setup Guide

Complete installation and setup instructions for the APEXVIPER Sports Betting Intelligence System.

---

## 📋 Table of Contents

1. [System Requirements](#system-requirements)
2. [Quick Start](#quick-start)
3. [Detailed Installation](#detailed-installation)
4. [Configuration](#configuration)
5. [Running the Tools](#running-the-tools)
6. [Development Setup](#development-setup)
7. [Troubleshooting](#troubleshooting)

---

## 🔧 System Requirements

### Minimum Requirements
- **Python**: 3.10 or higher
- **Operating System**: Linux, macOS, or Windows
- **RAM**: 2GB minimum
- **Disk Space**: 500MB for dependencies and logs

### Recommended
- **Python**: 3.11+
- **RAM**: 4GB+
- **SSD**: For faster data processing

---

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/Bam082608/Sports-Betting.git
cd Sports-Betting
```

### 2. Create Virtual Environment
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On Linux/macOS:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
# Install core dependencies
pip install -r requirements.txt

# For development (includes testing and linting tools)
pip install -r requirements-dev.txt
```

### 4. Run Your First Analysis
```bash
# Run the APEXVIPER engine
python apexviper_engine.py

# Expected output: Analysis of player props with GREEN/YELLOW/RED signals
```

---

## 📦 Detailed Installation

### Step 1: Python Installation

#### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install python3.11 python3.11-venv python3-pip
```

#### macOS
```bash
# Using Homebrew
brew install python@3.11
```

#### Windows
Download Python from [python.org](https://www.python.org/downloads/) and run the installer.
**Important**: Check "Add Python to PATH" during installation.

### Step 2: Virtual Environment Setup

**Why use a virtual environment?**
- Isolates project dependencies
- Prevents version conflicts
- Makes the project portable

```bash
# Navigate to project directory
cd Sports-Betting

# Create virtual environment named 'venv'
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate  # Linux/macOS
# OR
venv\Scripts\activate  # Windows

# Verify activation (should show venv path)
which python  # Linux/macOS
where python  # Windows
```

### Step 3: Install Dependencies

```bash
# Upgrade pip to latest version
pip install --upgrade pip

# Install core dependencies
pip install -r requirements.txt

# Verify installation
pip list
```

**Core dependencies installed:**
- `pandas` - Data manipulation
- `numpy` - Numerical computing
- `playwright` - Browser automation for surveillance
- `pydantic` - Data validation
- `pyyaml` - Configuration management

### Step 4: Playwright Browser Setup

For the surveillance tools to work:

```bash
# Install Playwright browsers
playwright install chromium
```

### Step 5: Verify Installation

```bash
# Test the engine
python apexviper_engine.py --help

# Test the power index tool
python apexviper-power-index/apexviper_power_index.py --help

# Run data validation
python data_validator.py apexviper_master_data.csv
```

---

## ⚙️ Configuration

### Configuration File (config.yaml)

The `config.yaml` file contains all tunable parameters:

```yaml
engine:
  target_shots: 2.5
  modifiers:
    chase_bonus: 0.15
    blowout_penalty: -0.20
  signals:
    green_threshold: 0.75
    yellow_threshold: 0.60
```

**To modify:**
1. Edit `config.yaml` with your preferred text editor
2. Restart any running scripts to apply changes
3. Version control your changes with git

### Environment Variables (Optional)

Create a `.env` file for sensitive data (not tracked in git):

```bash
# .env file
SPORTSBOOK_API_KEY=your_api_key_here
LOG_LEVEL=DEBUG
```

---

## 🎯 Running the Tools

### APEXVIPER Engine (Player Props Analysis)

```bash
# Basic usage (uses default apexviper_master_data.csv)
python apexviper_engine.py

# Custom input file
python apexviper_engine.py --input my_data.csv

# Custom output file
python apexviper_engine.py --output my_results.csv

# Verbose logging
python apexviper_engine.py --verbose
```

**Output:**
- Terminal display with ranked players
- `apexviper_results.csv` with APEX scores
- Log file in `logs/` directory

### Power Index Tool

```bash
# Basic usage
python apexviper-power-index/apexviper_power_index.py --input team_matrix.csv

# With power play data
python apexviper-power-index/apexviper_power_index.py \
  --input team_matrix.csv \
  --pp_team team_pp_data.csv \
  --pp_player player_ppss_data.csv

# Custom output files
python apexviper-power-index/apexviper_power_index.py \
  --input data.csv \
  --output-csv results.csv \
  --output-json results.json
```

### Data Validation

```bash
# Validate player data
python data_validator.py apexviper_master_data.csv --type player

# Validate team PP data
python data_validator.py team_pp.csv --type team_pp

# Validate player PPSS data
python data_validator.py player_ppss.csv --type player_ppss
```

### Surveillance Tools

```bash
# Open surveillance dashboard
# Simply open any HTML file in nhl/surveillance/ with a web browser

# Or use the verification tool
python verification/verify_hub.py
```

---

## 🛠️ Development Setup

### Installing Development Tools

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Includes:
# - pytest (testing)
# - black (code formatting)
# - flake8 (linting)
# - mypy (type checking)
# - pre-commit (git hooks)
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov=. --cov-report=html

# Run specific test file
pytest tests/test_apexviper_engine.py

# Run with verbose output
pytest -v

# View coverage report
open htmlcov/index.html  # macOS
xdg-open htmlcov/index.html  # Linux
```

### Code Formatting

```bash
# Check formatting (don't modify files)
black --check .

# Auto-format all Python files
black .

# Check import sorting
isort --check-only .

# Auto-sort imports
isort .
```

### Linting

```bash
# Run flake8 linter
flake8 .

# Run pylint
pylint apexviper_engine.py

# Type checking with mypy
mypy apexviper_engine.py
```

### Pre-commit Hooks

```bash
# Install pre-commit hooks
pre-commit install

# Run hooks manually
pre-commit run --all-files

# Update hooks
pre-commit autoupdate
```

---

## 🐛 Troubleshooting

### Common Issues

#### Issue: "ModuleNotFoundError: No module named 'pandas'"

**Solution:**
```bash
# Ensure virtual environment is activated
source venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

#### Issue: "Permission denied" when running scripts

**Solution:**
```bash
# Make scripts executable
chmod +x apexviper_engine.py
chmod +x apexviper-power-index/apexviper_power_index.py

# Or run with python explicitly
python apexviper_engine.py
```

#### Issue: Playwright browsers not found

**Solution:**
```bash
# Install Playwright browsers
playwright install chromium

# Or install all browsers
playwright install
```

#### Issue: "No such file or directory: 'apexviper_master_data.csv'"

**Solution:**
- Ensure you're in the correct directory (`Sports-Betting/`)
- Check if the file exists: `ls -l apexviper_master_data.csv`
- Create sample data or specify correct path with `--input`

#### Issue: Tests failing with import errors

**Solution:**
```bash
# Ensure you're in project root
cd /path/to/Sports-Betting

# Run tests with Python path
PYTHONPATH=. pytest

# Or install package in editable mode
pip install -e .
```

### Getting Help

1. **Check Logs**: Look in `logs/` directory for detailed error messages
2. **Run with Verbose**: Use `--verbose` flag for more output
3. **Validate Data**: Run `python data_validator.py <file>` to check data quality
4. **GitHub Issues**: Report issues at https://github.com/Bam082608/Sports-Betting/issues

---

## 📚 Next Steps

After successful setup:

1. **Read the Main README**: [README.md](README.md) - System overview and protocols
2. **Explore Protocols**: [protocols/](protocols/) - 26+ betting protocols
3. **Review Lessons Learned**: [tracking/COMPLETE-LESSONS-LEARNED.md](tracking/COMPLETE-LESSONS-LEARNED.md)
4. **Check Daily Workflow**: [protocols/APEXVIPER_GAME_DAY_TIMELINE.md](protocols/APEXVIPER_GAME_DAY_TIMELINE.md)

---

## 🔄 Updating the System

```bash
# Pull latest changes
git pull origin main

# Update dependencies
pip install --upgrade -r requirements.txt

# Run tests to verify
pytest
```

---

## 🗑️ Uninstallation

```bash
# Deactivate virtual environment
deactivate

# Remove virtual environment
rm -rf venv

# Remove Python cache
find . -type d -name __pycache__ -exec rm -rf {} +
find . -type f -name "*.pyc" -delete
```

---

**Last Updated**: December 11, 2025
**Version**: 1.0.0
**Maintained By**: APEXVIPER Team
