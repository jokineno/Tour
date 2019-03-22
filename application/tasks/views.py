from application import app, db
from flask import redirect, render_template, request, url_for
from application.tasks.models import Task
from application.tasks.forms import TaskForm
from flask_login import login_required


@app.route("/tasks/",methods=["GET"])
def tasks_index():
    return render_template("tasks/list.html", tasks=Task.query.all())

@app.route("/tasks/new/")
@login_required
def tasks_form():

    return render_template("tasks/new.html", form=TaskForm())

@app.route("/tasks/<task_id>/", methods=["POST"])
@login_required
def tasks_set_done(task_id):

    t = Task.query.get(task_id)
    if t.status=="Tulossa":
        t.status = "Mennyt"
        db.session().commit()
    elif t.status== "Mennyt": 
        t.status="Peruttu"
        db.session().commit()
    elif t.status=="Peruttu":
        t.status="Tulossa"
        db.session().commit()
  
    return redirect(url_for("tasks_index"))

@app.route("/tasks/delete/<task_id>/", methods=["POST","GET"])
@login_required
def tasks_remove(task_id):
    t = Task.query.get(task_id)
    db.session().delete(t)
    db.session().commit()

    return redirect(url_for("tasks_index"))


@app.route("/tasks/", methods=["POST"])
@login_required
def tasks_create():
    
    form = TaskForm(request.form)
    
    if not form.validate():
        return render_template("tasks/new.html", form = form)
    t = Task(form.name.data, form.place.data, form.pvm.data, form.showtime.data)
    t.status = form.status.data

    db.session().add(t)
    db.session().commit()
  

    return redirect(url_for("tasks_index"))