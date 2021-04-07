# monke-api
monke based microservices 🐒
why implement logic, when you can do a GET request 🦍

basado on fastapi + uvicorn 🦧🧡

## development

### install
1. `pipenv install`*
2. `pipenv run uvicorn main:monke_api --reload`
3. go to [localhost:8000/docs](http://localhost:8000/docs)

*for pycharm'lets, refer to [guide](https://www.jetbrains.com/help/pycharm/pipenv.html) how to setup pipenv env 🦧

### best practices
- commit messages with monke are preferred
- do not forget to tag and name your endpoints!
- bigger functions go to `utils.py` to declutter `main.py`
