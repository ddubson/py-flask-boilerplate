# Python with Flask Microframework Web Service Boilerplate

## Development

### Setting up environment

Run:
```
make init
```

### Running the app

Run:
```
export FLASK_APP=service.py
make run
```
### Executing tests

Run `make test` to execute the test suite located in tests directory

## Deploy

### Push to Heroku

```
heroku login
heroku create my_app_name
git commit
git push heroku master
```

