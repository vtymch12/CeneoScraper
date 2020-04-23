from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/test')
def test():
    return "test"