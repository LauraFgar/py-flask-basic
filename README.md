```sh
python3 -m venv env
source env/bin/activate
pip install flask
pip3 freeze > requirements.text
flask run
export FLASK_APP=main.py
export FLASK_DEBUG=1
```