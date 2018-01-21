from web_service import app


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"
