from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        new_todo = request.form["new_todo"]
        todos.append(new_todo) 
    return render_template('first.html.jinja', my_todos=todos)

todos = ['have fun', 'figure myself out', 'thank god for another year']

@app.route("/delete_todo/<int:todo_index>", methods=["POST"])
def todo_delete(todo_index):
    del todos[todo_index]

    return redirect('/')