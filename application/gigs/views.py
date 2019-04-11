from application import app, db, login_required

from flask import redirect, render_template, request, url_for
from application.gigs.models import Gig
from application.gigs.forms import GigForm
from application.tour.models import Tour
from flask_login import current_user
from sqlalchemy import desc, asc




@app.route("/gigs/",methods=["GET"])
@login_required()
def gigs_index():
    return render_template("gigs/list.html", gigs=current_user.gigs, tourName = Tour.get_tourName_by_id)

@app.route("/gigs/new/", methods=["GET","POST"])
@login_required()
def gigs_form():
    form = GigForm(request.form)
    tours = [(g.id, g.name) for g in Tour.query.order_by('name')]
    print(tours)
    
    form.tour_id.choices = tours
    
    return render_template("gigs/new.html", form=form)
    
    

@app.route("/gigs/<gig_id>/", methods=["POST"])
@login_required()
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
@login_required()
def gigs_remove(gig_id):
    
    t = Gig.query.get(gig_id)
    db.session().delete(t)
    db.session().commit()

    return redirect(url_for("gigs_index"))

@app.route("/tour/delete/<gig_id>/", methods=["GET","POST"])
@login_required()
def gigs_remove_2(gig_id):
    t = Gig.query.get(gig_id)
    db.session().delete(t)
    db.session().commit()
    
    return redirect(url_for("tour_index"))

@app.route("/gigs/", methods=["POST"])
@login_required()
def gigs_create():
    
    form = GigForm(request.form)  
    #selvitä tämä mysteeri! 
    if not form.validate_on_submit():
        print("ONNISTUI")
        t = Gig(form.name.data, form.place.data, form.pvm.data, form.showtime.data)
        t.status = form.status.data
        t.account_id = current_user.id
        t.tour_id = form.tour_id.data
        
        print("TIEDOT: ")
        print(type(t.tour_id)) #int koska coerce = int
        print(t.tour_id) #2
    
        db.session().add(t)
        db.session().commit() 

        return redirect(url_for("gigs_index"))
    
    elif not form.validate():
        print("FORM EI VALIDOI")
        tours = [(g.id, g.name) for g in Tour.query.order_by('name')]
        form.tour_id.choices = tours
        print(tours)
        return render_template("gigs/new.html", form = form)


@app.route("/gigs/view/<gig_id>/", methods=["GET"])
@login_required()
def gigs_view(gig_id):
    form = GigForm(request.form)
    return render_template("gigs/single.html", gig = Gig.query.get(gig_id), form=form)

@app.route("/gigs/edit/<gig_id>/", methods=["GET","POST"])
@login_required()
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


@app.route("/gigs/search/", methods=["GET"])
@login_required()
def find_gigs():
    gigs = Gig.find_gigs(request.args.get("query"))
    print("FIND GIGS:")
    print(gigs)
    for gig in gigs:
        print(gig.name)
        print("*****")
    return render_template("gigs/list.html", gigs=Gig.find_gigs(request.args.get("query")), tourName=Tour.get_tourName_by_id)    


@app.route("/gigs/asc_by_date/", methods=["GET"])
@login_required()
def list_by_date_asc():
    
    return render_template("/gigs/list.html",gigs=Gig.query.order_by(asc(Gig.pvm)).all(), tourName=Tour.get_tourName_by_id)    

@app.route("/gigs/desc_by_date/", methods=["GET"])
@login_required()
def list_by_date_desc():
    return render_template("/gigs/list.html", gigs=Gig.query.order_by(desc(Gig.pvm)).all(), tourName=Tour.get_tourName_by_id)    

