# Meeting Prep Agent

A minimal AI meeting preparation assistant that stores meeting history, summarizes notes, extracts follow-ups, and suggests future agendas using persistent memory.

## Features

- Save meeting details with summary and task extraction
- Persist memory in `meeting_memory.json`
- Recall past meetings
- Suggest agenda items from recent meeting history
- Show pending follow-ups
- Display learning/improvement over time

## Setup

1. Create a Python environment
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set your OpenAI API key:
   - Windows PowerShell:
     ```powershell
     $env:OPENAI_API_KEY = "your-key"
     ```
   - macOS/Linux:
     ```bash
     export OPENAI_API_KEY="your-key"
     ```
4. Run the app:
   ```bash
   python app.py
   ```
5. Open `http://127.0.0.1:5000` in your browser

## Notes

- The app stores memory in `meeting_memory.json`.
- Use `OPENAI_MODEL` to switch models if desired.
- The backend provides API routes for meetings, agenda suggestions, reminders, and learning summaries.
