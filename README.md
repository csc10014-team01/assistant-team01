# Smart Virtual Assistant (assistant-team01)

A rule-based virtual assistant for campus office information and schedules.

## Prerequisites
- Python >= 3.10
- Git

## Setup
```bash
git clone git@github.com:csc10014-team01/assistant-team01.git
cd assistant-team01

# Tạo và kích hoạt virtual environment
python -m venv .venv
source .venv/Scripts/activate       # Trên Linux/macOS: source .venv/bin/activate

# Cài đặt dependencies và package ở chế độ editable
pip install -r requirements.txt
pip install -e .

## Run
```bash
python -m assistant "where is the IT helpdesk?"
# Hoặc chạy chế độ tương tác:
python -m assistant

##Test
```bash
pytest -q

## Project structure
assistant-team01/ 
├── README.md               # Member 1 
├── .gitignore  requirements.txt  pyproject.toml   # Member 1 
├── src/assistant/          # backend — Member 2 (copy the starter package) 
├── ui/README.md            # UI plan — Member 3
├── data/README.md          # data sources & owners — Member 3 
├── tests/                  # smoke tests — Member 4 
├── docs/README.md  docs/team.md   # Member 4 
└── scripts/check_env.py    # Member 2 