pip install virtualenv
 python -m venv env
pip install fastapi
pip install uvicorn
pip install motor
pip install pymongo
pip install email-validator
uvicorn app.main:app --reload
