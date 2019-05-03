from application import app, db, login_required
from application.auth.models import User, Role
from flask import redirect, render_template, request, url_for
from application.gigs.models import Gig
from application.auth.models import User
from application.gigs.forms import GigForm
from application.tour.models import Tour
from flask_login import current_user
from sqlalchemy import desc, asc


@app.route("/gigs/",methods=["GET"])
@login_required()
def gigs_index():
    if current_user.role.name == "ADMIN":
        return render_template("gigs/list.html", tours=Tour.query.all(), tourName = Tour.get_tourName_by_id)
    else:
        return render_template("gigs/list.html", tourName = Tour.get_tourName_by_id, tours=current_user.tours)

@app.route("/gigs/new/", methods=["GET","POST"])
@login_required()
def gigs_form(role="ADMIN"):

    form = GigForm(request.form)
    tours = [(tour.id, tour.name) for tour in Tour.query.all()]
    form.tour_id.choices = tours
    
    return render_template("gigs/new.html", form=form)
    
    

@app.route("/gigs/<gig_id>/", methods=["POST"])
@login_required(role="ADMIN")
def gigs_change_status(gig_id):

    gig = Gig.query.get(gig_id)
    if gig.status=="Upcoming":
        gig.status = "Past"
        db.session().commit()
    elif gig.status== "Past": 
        gig.status="Cancelled"
        db.session().commit()
    elif gig.status=="Cancelled":
        gig.status="Upcoming"
        db.session().commit()
  
    return redirect(url_for("gigs_index"))

@app.route("/gigs/delete/<gig_id>/", methods=["GET","POST"])
@login_required(role="ADMIN")
def gigs_remove(gig_id):
    
    gig = Gig.query.get(gig_id)
    db.session().delete(gig)
    db.session().commit()

    return redirect(url_for("gigs_index"))

@app.route("/tour/delete/<gig_id>/", methods=["GET","POST"])
@login_required(role="ADMIN")
def gigs_remove_2(gig_id):
    gig = Gig.query.get(gig_id)
    db.session().delete(gig)
    db.session().commit()
    
    return redirect(url_for("tour_index"))

@app.route("/gigs/", methods=["POST"])
@login_required()
def gigs_create(role="ADMIN"):
    
    form = GigForm(request.form)  
    tours = [(tour.id, tour.name) for tour in Tour.query.order_by('name')]
    form.tour_id.choices = tours
    
    if  form.validate_on_submit():
        gig = Gig(form.name.data, form.place.data, form.pvm.data, form.showtime.data)
        gig.status = form.status.data
        gig.account_id = current_user.id
        gig.tour_id = form.tour_id.data
    
        db.session().add(gig)
        db.session().commit() 

        return redirect(url_for("gigs_index"))
    
    elif not form.validate():
        
        tours = [(tour.id, tour.name) for tour in Tour.query.order_by('name')]
        form.tour_id.choices = tours
        
        return render_template("gigs/new.html", form = form)


@app.route("/gigs/view/<gig_id>/", methods=["GET"])
@login_required()
def gigs_view(gig_id):
    form = GigForm(request.form)
    return render_template("gigs/single.html", gig = Gig.query.get(gig_id), form=form)

@app.route("/gigs/edit/<gig_id>/", methods=["GET","POST"])
@login_required(role="ADMIN")
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
    args = "%" + request.args.get('query') + "%"

    if current_user.role.name=="USER":
        idx = Tour.get_index(current_user.id)
        tours = Tour.query.filter(Tour.name.like(args),Tour.id.in_(idx))
        return render_template("gigs/list.html", tours=tours, tourName=Tour.get_tourName_by_id) 

    elif current_user.role.name=="ADMIN":
        tours = Tour.query.filter(Tour.name.like(args))
        return render_template("gigs/list.html", tours=tours, tourName=Tour.get_tourName_by_id)    
   


@app.route("/gigs/asc_by_date/", methods=["GET"])
@login_required()
def list_by_date_asc():
    
    return render_template("/gigs/list.html",gigs=Gig.query.order_by(asc(Gig.pvm)).all(), tourName=Tour.get_tourName_by_id)    

@app.route("/gigs/desc_by_date/", methods=["GET"])
@login_required()
def list_by_date_desc():
    return render_template("/gigs/list.html", gigs=Gig.query.order_by(desc(Gig.pvm)).all(), tourName=Tour.get_tourName_by_id)    

