from flask import Flask, jsonify, request

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

# this will result in: ['simonam', 'rachelf']
usernames = users.keys()


@app.route('/api/')
def index():
    return jsonify(
        {
            'name': 'My Application Users API',
            'version': 1
        }
    )


@app.route('/api/v1/users')
def users():
    return jsonify(
        {
            'usernames': usernames
        }
    )


@app.route('/api/v1/user')
def user():
    username = request.args.get('username')
    if username in usernames:
        return jsonify(
            {
                'user': users[username]
            }
        )
    else:
        return jsonify(
            {
                'error': 'User does not exist'
            }
        ), 404


app.run(host='127.0.0.1', port=3000, debug=True)
