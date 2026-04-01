# TaskManager

A lightweight command-line task manager with optional AI-assisted task splitting.

## ⭐ Case Study Overview

`TaskManager` is a minimal, test-driven CLI project showcasing Python, file persistence, user interaction, and AI integration.

- Goal: implement a simple productivity tool with clean code, unit testing, and API extension points.
- Audience: hiring managers and engineers reviewing practical Python project implementation.

## 📦 Project Structure

- `main.py` - CLI interface with menu for tasks.
- `task_manager.py` - `TaskManager` and `Task` classes with JSON persistence.
- `ai_service.py` - OpenAI task decomposition helper.
- `tasks.json` - persistent data store (auto-created).
- `test_task_manager.py` - unit tests for task completion logic.
- `requirements.txt` - dependency list.

## 🧩 Tech Stack & Libraries

- Python 3.10+
- `json`, `os`, `venv` (standard)
- `openai` for AI assistant
- `python-dotenv` for environment variables
- `pytest` for unit testing
- `requests`, `urllib3`, `certifi`, `charset-normalizer`, `idna`

## 🚀 Installation

1. Clone repository:

```bash
git clone <repo-url> && cd TaskManager
```

2. Create virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
pip install pytest python-dotenv openai
```

4. Configure OpenAI API key (optional):

```bash
cat > .env <<'EOL'
OPENAI_API_KEY=your_api_key_here
EOL
```

5. Verify API key:

```bash
python - <<'PY'
import os
from dotenv import load_dotenv
load_dotenv()
print('OPENAI_API_KEY:', os.getenv('OPENAI_API_KEY'))
PY
```

## ▶️ Run the app

```bash
python main.py
```

### CLI Options

- 1: Add task manually
- 2: Add AI-assisted tasks (with OpenAI key)
- 3: List tasks
- 4: Complete task by ID
- 5: Delete task by ID
- 6: Exit

## 🧪 Tests

```bash
pytest -q
```

### What is tested

- `TaskManager.complete_task(id)` marks correct item complete.
- Nonexistent ID returns not found and no state change.
- `complete_task` does not alter other tasks.
- Re-completion keeps task marked complete.

## 🔧 Code Summary

- `Task` has `id`, `description`, `completed`; `__str__` prints status (✓ / blank).
- `TaskManager` tracks `_tasks`, `_next_id`, load/save from `tasks.json`.
- `load_tasks()` handles missing file.
- `save_tasks()` writes JSON with indentation.

## 🤖 AI Assistant Guide

`ai_service.py` calls OpenAI chat completion for decomposition:

- Takes complex task string.
- Requests 3-5 subtasks in dash list format.
- Parses lines starting with `-` to subtasks.

> ⚠️ fix bug before use:
> `substacks.append(subtask)` should be `subtasks.append(subtask)`.

## ✅ Roadmap

1. Expand CLI: add due date, priority, filtering.
2. Add CLI args mode with `argparse` or `click`.
3. Implement `SQLite` backend with optional JSON fallback.
4. Add editing and undo actions.
5. Improve tests: add add/delete/list coverage and error conditions.
6. Integrate a web UI (FastAPI / Flask).
7. Add CI pipeline with GitHub Actions and coverage report.

## 📁 Example Walkthrough

```bash
python main.py
# choose 1 -> 'Buy groceries'
# choose 1 -> 'Write project report'
# choose 3 -> list tasks
# choose 4 -> 2
# choose 3 -> verify completed
# choose 2 -> generate subtasks (OpenAI)
# choose 6 -> exit
```

## 💡 Suggestions for interview discussion

- Explain decisions around JSON persistence and in-memory model.
- Describe how unit tests provide behavior contract and prevent regressions.
- Discuss tradeoffs between simple file storage and DB-backed solutions.
- Outline OpenAI prompt design and error handling.

## 🧹 Troubleshooting

- Make sure `.venv` is activated.
- If `TaskManager` can’t read/write `tasks.json`, check file permissions.
- For invalid ID entries in menu, main.py prints message and continues.

## 📝 License

MIT License

```
MIT License

Copyright (c) 2026 Your Name

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## 📣 Author

- `Your Name` (replace with your own name)
- Link to portfolio/resume/project URL

