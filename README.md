cd the repo

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

uvicorn app:app --reload