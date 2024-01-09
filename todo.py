from flask import Flask, render_template, request, redirect
import pymysql
import pymysql.cursors

app = Flask(__name__)

conn = pymysql.connect(
    database="kdavidson_todos",
    user="kdavidson",
    password="231534561",
    host="10.100.33.60",
    cursorclass=pymysql.cursors.DictCursor
)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        new_todo = request.form["new_todo"]
        todos.append(new_todo) 
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO `todos` (`description`) VALUES ('{new_todo}')")
        cursor.close()
        conn.commit()

    cursor = conn.cursor()

    cursor.execute("SELECT * from `todos`")

    results = cursor.fetchall()

    cursor.close()
    return render_template('first.html.jinja', my_todos=results)


todos = ['have fun', 'figure myself out', 'thank god for another year']

@app.route("/delete_todo/<int:todo_index>", methods=["POST"])
def todo_delete(todo_index):
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM `todos` WHERE `id` = {todo_index}")
    cursor.close()
    conn.commit()
    return redirect('/')