from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////data/todos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)

@app.route('/')
def index():
    todos = Todo.query.all()
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add():
    content = request.form['content']
    todo = Todo(content=content)
    db.session.add(todo)
    db.session.commit()
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    app.logger.debug(f'Deleting Todo with id {id}')
    todo = db.session.get(Todo, id)
    db.session.delete(todo)
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        db.session.commit()
    app.run(host='0.0.0.0', debug=True)
