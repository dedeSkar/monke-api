# monke-api
monke based microservices ๐
why implement logic, when you can do a GET request ๐ฆ

basado on fastapi + uvicorn ๐ฆง๐งก

## development

### install
1. `pipenv install`*
2. `pipenv run uvicorn main:monke_api --reload`
3. go to [localhost:8000/docs](http://localhost:8000/docs)

*for pycharm'lets, refer to [guide](https://www.jetbrains.com/help/pycharm/pipenv.html) how to setup pipenv env ๐ฆง

### best practices
- commit messages with monke are preferred
- do not forget to name your endpoints!
- bigger functions go to `utils.py` to declutter `main.py`

