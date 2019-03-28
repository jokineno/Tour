from application import app, db
from flask import redirect, render_template, request, url_for
from application.gigs.models import Gig
from application.gigs.forms import GigForm
from flask_login import login_required, current_user


@app.route("/gigs/",methods=["GET"])
@login_required
def gigs_index():
    return render_template("gigs/list.html", gigs=current_user.gigs)

@app.route("/gigs/new/", methods=["GET","POST"])
@login_required
def gigs_form():
    form = GigForm()
    return render_template("gigs/new.html", form=form)

@app.route("/gigs/<gig_id>/", methods=["POST"])
@login_required
def gigs_change_status(gig_id):

    t = Gig.query.get(gig_id)
    if t.status=="Tulossa":
        t.status = "Mennyt"
        db.session().commit()
    elif t.status== "Mennyt": 
        t.status="Peruttu"
        db.session().commit()
    elif t.status=="Peruttu":
        t.status="Tulossa"
        db.session().commit()
  
    return redirect(url_for("gigs_index"))

@app.route("/gigs/delete/<gig_id>/", methods=["GET","POST"])
@login_required
def gigs_remove(gig_id):
    t = Gig.query.get(gig_id)
    db.session().delete(t)
    db.session().commit()

    return redirect(url_for("gigs_index"))

@app.route("/gigs/", methods=["POST"])
@login_required
def gigs_create():
    
    form = GigForm(request.form)   
    
    if not form.validate():
        return render_template("gigs/new.html", form = form)
    t = Gig(form.name.data, form.place.data, form.pvm.data, form.showtime.data)
    t.status = form.status.data
    t.account_id = current_user.id

    db.session().add(t)
    db.session().commit()
  

    return redirect(url_for("gigs_index"))


@app.route("/gigs/view/<gig_id>/", methods=["GET"])
def gigs_view(gig_id):
    form = GigForm(request.form)
    return render_template("gigs/single.html", gig = Gig.query.get(gig_id), form=form)

@app.route("/gigs/edit/<gig_id>/", methods=["GET","POST"])
def gigs_edit(gig_id):
    
    if request.method == "GET":
        gig = Gig.query.get(gig_id)
        form = GigForm(obj=gig)
    
        return render_template("gigs/edit.html",form=form, gig_id=gig_id)
    
    form = GigForm(request.form)
    gig = Gig.query.get(gig_id)

    gig.name = form.name.data
    gig.place = form.place.data
    gig.pvm = form.pvm.data
    gig.showtime = form.showtime.data
    gig.status = form.status.data

    db.session().commit()

    return redirect(url_for("gigs_view", gig_id = gig_id))