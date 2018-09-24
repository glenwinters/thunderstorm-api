## Thunderstorm API

API root: [thunderstorm-api.herokuapp.com](https://thunderstorm-api.herokuapp.com)

### Local development
This app uses [Flask](http://flask.pocoo.org/).

##### Set up:
[Install Python 3](https://www.python.org/)  
[Install Pipenv](https://pipenv.readthedocs.io/en/latest/)  
`pipenv install` within project dir

##### Commands:
All commands need to be run in the pipenv shell. You can start a shell using
`pipenv shell` or prefix each command with `pipenv run`.

`flask run` - Run the app (use `FLASK_ENV=development` for dev mode)  
`flake8 .` - Lint all the python files using [Flake8](http://flake8.pycqa.org/en/latest/)
