from flask import Flask, render_template, request, redirect
import pymysql
import pymysql.cursors

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        new_todo = request.form["new_todo"]
        todos.append(new_todo) 
    return render_template('first.html.jinja', my_todos=todos)
conn = pymysql.connect(
    database="kdavidson_todos",
    user="kdavidson",
    password="231534561",
    host="10.100.33.60",
    cursorclass=pymysql.cursors.DictCursor
    )

cursor = conn.cursor()

cursor.execute("SELECT `description` FROM `todos`")

results = cursor.fetchall()

todos = ['have fun', 'figure myself out', 'thank god for another year']

@app.route("/delete_todo/<int:todo_index>", methods=["POST"])
def todo_delete(todo_index):
    del todos[todo_index]

    return redirect('/')