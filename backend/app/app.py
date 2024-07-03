
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/twix_ai'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Example model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

# Example route
@app.route('/')
def home():
    return 'Welcome to Twix AI Backend'

@app.route('/api/example', methods=['GET'])
def example_api():
    data = {
        'message': 'Hello from Twix AI Backend!'
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

