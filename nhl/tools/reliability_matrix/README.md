# ReliabilityMatrix (v9.0)

**Component Status:** `LIVE`
**Version:** 9.0 (Operation Dec 5 Build)
**Role:** Visualizer for Player Prop Reliability & Deployment Quality.

## Overview
The `ReliabilityMatrix` is a React component designed to visualize the quality of a player's minutes ("Empty Calorie" vs. "High Value") and their reliability based on recent performance ("Hit Rate"). It translates "Surveillance Speak" (raw data/notes) into "Developer Speak" (visual cues).

### Key Features
*   **The Deployment Bar:** Splits TOI into Even Strength (Green) vs. Power Play (Blue).
*   **The Chase Script:** Automatically sorts players with "CHASE MODE" script grades to the top.
*   **Zap Icon:** Identifies "Pure Shooters" (Goals > 60% of Assists).
*   **Hit Rate Bubbles:** Visualizes last 5 game performance against the baseline target (2+ shots).

## Installation & Setup

This component is provided as a raw React/JSX file. To use it, you need a React environment.

### Dependencies
You must install `lucide-react` for the icons to work.

```bash
npm install lucide-react
```

### Usage
1.  Copy the content of `ReliabilityMatrix.jsx` into your React project (e.g., `src/components/ReliabilityMatrix.jsx`).
2.  Import and render it in your main App file:

```jsx
import ReliabilityMatrix from './components/ReliabilityMatrix';

function App() {
  return (
    <div className="App">
      <ReliabilityMatrix />
    </div>
  );
}
```

## Daily Workflow (The "Universal" Approach)

The component provided contains static data ("Operation Dec 5"). To use this daily:

1.  **Generate Data:** Use the **[Daily Prompt Template](./DAILY_PROMPT_TEMPLATE.md)**. Copy and paste that file's content into an AI assistant (like Gemini or ChatGPT) along with the day's `daily-intel` report.
2.  **Update Component:** The AI will provide a new `players` array.
3.  **Inject Data:** Open `ReliabilityMatrix.jsx` and replace the `const [players] = useState([...])` block with the new array provided by the AI.

## Logic Glossary (Script Grades)

*   **CHASE MODE (Green Border):** Player's team is expected to trail, forcing high volume shooting. *Overrides all other sorts.*
*   **BLOWOUT RISK (Amber Border):** Player's team is a massive favorite; risk of benched starters in 3rd period.
*   **SUPPRESSED (Red Border/Lock Icon):** Opponent is elite at blocking shots (e.g., "Shin Pad Equity" risk).
*   **HISTORY CHASE (Purple Border):** Player is chasing a specific milestone (e.g., Ovechkin goals).
*   **NEUTRAL/LOW PACE:** Standard game environments.
