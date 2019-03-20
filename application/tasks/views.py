from application import app, db
from flask import redirect, render_template, request, url_for
from application.tasks.models import Task


@app.route("/tasks/",methods=["GET"])
def tasks_index():
    return render_template("tasks/list.html", tasks=Task.query.all())

@app.route("/tasks/new/")
def tasks_form():
    return render_template("tasks/new.html")

@app.route("/tasks/<task_id>/", methods=["POST"])
def tasks_set_done(task_id):

    t = Task.query.get(task_id)
    if t.done==True:
        t.done = False
        db.session().commit()
    else: 
        t.done=True
        db.session().commit()
  
    return redirect(url_for("tasks_index"))

@app.route("/tasks/delete/<task_id>/", methods=["POST","GET"])
def tasks_remove(task_id):
    t = Task.query.get(task_id)
    db.session().delete(t)
    db.session().commit()

    return redirect(url_for("tasks_index"))


@app.route("/tasks/", methods=["POST"])
def tasks_create():
    
    t = Task(request.form.get("date"),request.form.get("name"),request.form.get("place"),request.form.get("showtime"))
    
    db.session().add(t)
    db.session().commit()

    return redirect(url_for("tasks_index"))
