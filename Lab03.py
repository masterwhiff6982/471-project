from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), default="Pending")

with app.app_context():
    db.create_all()

@app.route('/api/tasks', methods=['POST'])
def add_task():
    data = request.get_json() 
    new_task = Task(title=data['title'])
    db.session.add(new_task)
    db.session.commit()
    return jsonify({"message": "Task created!", "id": new_task.id}), 201

if __name__ == '__main__':
    app.run(port=1412, debug=True)