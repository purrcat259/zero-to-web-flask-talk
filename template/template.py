from flask import Flask, abort, render_template

app = Flask(__name__)

# this would usually be stored in some sort of Database
users = {
    'simonam': {
        'name': 'Simon',
        'age': 23,
        'username': 'simonam'
    },
    'rachelf': {
        'name': 'Rachel',
        'age': 25,
        'username': 'rachelf'
    }
}

usernames = users.keys()
# this will result in: ['simonam', 'rachelf']


@app.context_processor
def inject_dict_for_all_templates():
    return dict(page={
        'title': 'My Flask Website'
    })


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/users')
def user_list():
    user_data = [users[name] for name in usernames]
    return render_template('users.html', data={
        'users': user_data
    })


@app.route('/user/<username>')
def user(username=None):
    # this checks if the username is in ['simonam', 'rachelf'] or if it is not provided
    if username not in usernames or username is None:
        abort(404)
    return render_template('user.html', data={
        'user': users[username]
    })


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


app.run(host='127.0.0.1', port=3000, debug=True)
