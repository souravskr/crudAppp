from flask import Flask, render_template, url_for, request, redirect
from flask.globals import request
from flask_sqlalchemy import SQLAlchemy
from datetime import date, datetime
from flask_sqlalchemy.model import Model

from werkzeug.utils import redirect

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id


@app.route('/', methods=['POST', 'GET'])
def index():

    # print(request.form.get('content'))

    if request.method == 'POST':
        task_content = request.form['content']

        if task_content == '':
            return redirect('/')
        else:
            new_task = Todo(content=task_content)

            try:
                db.session.add(new_task)
                db.session.commit()
                return redirect('/')

            except:
                return 'Error during adding the task'

    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks=tasks)


@app.route('/delete/<int:id>')
def delete(id):

    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')

    except:
        return 'There was a problem'


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):

    task = Todo.query.get_or_404(id)

    if request.method == 'POST':
        task.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/')

        except:
            return 'There was a problem'

    else:
        return render_template('update.html', task=task)


@app.route('/deleteall')
def delete_all():
    # all_tasks = Todo.query.order_by(Todo.date_created).all()

    try:
        db.session.query(Todo).delete()
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem'


if __name__ == "__main__":
    app.run(debug=True)
