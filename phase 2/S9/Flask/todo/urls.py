from flask import request, redirect, url_for, render_template, flash
from flask_login import current_user, logout_user, login_required, login_user
from todo.models import User, Todo
from todo import bcrypt, app, db, login_manager
from datetime import datetime, timedelta
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            flash('Logged in successfully', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid email or password', 'danger')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        password = request.form['password']
        user_check = User.query.filter_by(email=email).first()
        if user_check:
            flash('Email already in use', 'danger')
            return redirect(url_for('register'))
        else:
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            user = User(email=email, fname=fname, lname=lname, password=hashed_password)
            db.session.add(user)
            db.session.commit()
            flash('Account created successfully', 'success')
            login_user(user)
            return redirect(url_for('dashboard'))
    return render_template('register.html')

@app.route('/dashboard')
@login_required
def dashboard():
    todos = current_user.todos
    return render_template('dashboard.html', todos=todos)

@app.route('/profile', methods = ['GET', 'POST'])
@login_required
def profile():
    if request.method == 'POST':
        user_check = User.query.filter_by(email = request.form['email']).first()
        if not user_check:
            current_user.email = request.form['email']
            current_user.fname = request.form['fname']
            current_user.lname = request.form['lname']
            db.session.commit()
            flash('Changes are done successfully', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Email already used', 'danger')


    return render_template('profile.html', user=current_user)

@app.route('/add_todo', methods=['GET', 'POST'])
@login_required
def add_todo():
    default_due_date = (datetime.now() + timedelta(days=7)).strftime('%Y-%m-%d')
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        due_date = request.form['due_date']
        due_date = datetime.strptime(due_date, '%Y-%m-%d')
        todo = Todo(title=title, content=content, author=current_user.id, due_date=due_date)
        db.session.add(todo)
        db.session.commit()
        flash('Todo added successfully', 'success')
        return redirect(url_for('dashboard'))
    return render_template('add_todo.html', default_due_date = default_due_date)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully', 'info')
    return redirect(url_for('login'))

@app.route('/delete_todo/<int:todo_id>', methods=['POST'])
@login_required
def delete_todo(todo_id):
    todo = Todo.query.get(todo_id)
    if todo:
        db.session.delete(todo)
        db.session.commit()
        flash('Todo deleted successfully', 'success')
    else:
        flash('Todo not found', 'danger')
    return redirect(url_for('dashboard'))