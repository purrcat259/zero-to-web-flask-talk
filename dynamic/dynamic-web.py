from flask import Flask, abort

app = Flask(__name__)

# this would usually be stored in some sort of Database
users = {
    'simonam': {
        'name': 'Simon',
        'age': 23
    },
    'rachelf': {
        'name': 'Rachel',
        'age': 25
    }
}

usernames = users.keys()
# this will result in: ['simonam', 'rachelf']


@app.route('/')
def index():
    return 'This is the home page'


@app.route('/user/<name>')
def user(username=None):
    # this checks if the username is in ['simonam', 'rachelf'] or if it is not provided
    if username not in usernames or username is None:
        abort(404)
    return 'This is the homepage for {}, age: {}'.format(
        username['name'],
        username['age']
    )


@app.errorhandler(404)
def page_not_found(e):
    return 'Oops, 404!, that does not exist!', 404


app.run(host='127.0.0.1', port=3000, debug=True)
