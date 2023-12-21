from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    new_todo 
    new_todo = request.form["new_todo"]
    return render_template('first.html.jinja', my_todos=todos)

todos = ['have fun', 'figure myself out', 'thank god for another year']