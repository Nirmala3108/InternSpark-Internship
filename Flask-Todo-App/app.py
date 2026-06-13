from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []


@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)


@app.route("/add", methods=["POST"])
def add_task():
    task = request.form.get("task")

    if task:
        tasks.append(task)

    return redirect(url_for("index"))


@app.route("/delete/<int:id>")
def delete_task(id):
    if 0 <= id < len(tasks):
        tasks.pop(id)

    return redirect(url_for("index"))


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_task(id):
    if request.method == "POST":
        tasks[id] = request.form["task"]
        return redirect(url_for("index"))

    return render_template("edit.html", id=id, task=tasks[id])


if __name__ == "__main__":
    app.run(debug=True)