from flask import Flask, render_template, request, redirect
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
import pymysql
import pymysql.cursors

app = Flask(__name__)
auth = HTTPBasicAuth()

conn = pymysql.connect(
    database="kdavidson_todos",
    user="kdavidson",
    password="231534561",
    host="10.100.33.60",
    cursorclass=pymysql.cursors.DictCursor
)

users = {
    "kas": generate_password_hash("ily"),
    "susan": generate_password_hash("bye")
}

@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username

@app.route('/', methods=['GET', 'POST'])
@auth.login_required
def index():
    if request.method == "POST":
        new_todo = request.form["new_todo"]
        todos.append(new_todo) 
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO `todos` (`description`) VALUES ('{new_todo}')")
        cursor.close()
        conn.commit()

    cursor = conn.cursor()

    cursor.execute("SELECT * from `todos` ORDER BY `complete`")

    results = cursor.fetchall()

    cursor.close()
    return render_template('first.html.jinja', my_todos=results)
if __name__ == '__main__':
    app.run()

todos = ['have fun', 'figure myself out', 'thank god for another year']

@app.route("/delete_todo/<int:todo_index>", methods=["POST"])
def todo_delete(todo_index):
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM `todos` WHERE `id` = {todo_index}")
    cursor.close()
    conn.commit()
    return redirect('/')

@app.route("/complete_todo/<int:todo_index>", methods=["POST"])
def todo_complete(todo_index):
    cursor = conn.cursor()
    cursor.execute(f"UPDATE `todos` SET `complete` = 1 WHERE `id` = {todo_index}")
    cursor.close()
    conn.commit()
    return redirect('/')