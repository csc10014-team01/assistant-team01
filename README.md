# Smart Virtual Assistant (assistant-team01)

A rule-based virtual assistant for campus office information and schedules.

## Prerequisites
- Python >= 3.10
- Git

## Setup
```bash
git clone git@github.com:csc10014-team01/assistant-team01.git
cd assistant-team01

# Tạo virtual environment
python -m venv .venv

# Kích hoạt virtual environment:
# Trên Windows (Git Bash):
source .venv/Scripts/activate
# Trên Windows (PowerShell):
.venv\Scripts\Activate.ps1
# Trên macOS / Linux:
source .venv/bin/activate

# Cài đặt dependencies và package ở chế độ editable
pip install -r requirements.txt
pip install -e .
```

## Run
```bash
# Chạy truy vấn đơn lẻ:
python -m assistant "where is the IT helpdesk?"
Type `help` to see the list of supported commands.

# Hoặc chạy chế độ tương tác (nhập 'quit' để thoát):
python -m assistant
```

## Test
```bash
pytest -q
```

## Project Structure
```text
assistant-team01/
├── README.md               # Member 1
├── .gitignore              # Member 1
├── requirements.txt        # Member 1
├── pyproject.toml          # Member 1
├── src/assistant/          # Member 2
├── scripts/check_env.py    # Member 2
├── ui/README.md            # Member 3
├── data/README.md          # Member 4
├── data/offices.csv        # Member 4
├── tests/test_smoke.py     # Member 5
├── docs/README.md          # Member 6
└── docs/team.md            # Member 6
```


## Troubleshooting
- No module named assistant: Chưa kích hoạt môi trường ảo .venv hoặc quên chạy lệnh pip install -e ..

- PowerShell: running scripts is disabled: Mở PowerShell với quyền Administrator hoặc CurrentUser và chạy lệnh:

```PowerShell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```
- Lỗi ký tự tiếng Việt trong CSV: Đảm bảo mở file với encoding utf-8.