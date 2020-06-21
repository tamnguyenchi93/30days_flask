## Setup Python virtual environment
Install python3 virtual environment
```bash
sudo apt-get update
sudo apt-get install python3-venv
```
Create virtual environment 
```bash
cd working_dir
mdkir .venv
python3 -m venv .venv
source .venv/bin/active
```

Install `flask`
```bash
pip install flask
```

## Run

```bash
export FLASK_APP=my_app.py
flask run
```