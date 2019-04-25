from application import app, db, login_required
from flask import redirect, render_template, request, url_for
from application.tour.models import Tour
from application.gigs.models import Gig
from application.auth.models import User
from application.tour.forms import TourForm
from flask_login import current_user


@app.route("/tours/", methods=["GET"])
@login_required()
def tour_index():
    alltours= current_user.tours

    return render_template("tour/tourform.html", tours=alltours, tour_gigs = Tour.get_gig_amount_by_id)

@app.route("/tours/new/", methods=["GET"])
@login_required()
def tour_form():
    form = TourForm()
    users = User.query.all()
    return render_template("tour/newtourform.html",users=users, form=form)

@app.route("/tours/", methods=["POST"])
@login_required()
def tour_create():
    form = TourForm(request.form)
    tour = Tour(form.name.data, form.start_date.data,form.end_date.data)
    if not form.validate_on_submit:
        form = TourForm()
        return render_template("tour/newtourform.html", form=form)
    
    db.session().add(tour)
    db.session().commit()

    selected_users = request.form.getlist("hello")
    
    for user in selected_users:
        selected = User.query.get(user)
        tour.tours.append(selected)
        db.session().commit()
    
        
    return redirect(url_for('tour_index'))

@app.route("/tours/view/<tour_id>/", methods=["GET"])
@login_required()
def tour_view(tour_id):
    form=TourForm(request.form)
    gigs = Gig.query.filter(Gig.tour_id == tour_id)
    return render_template("tour/single.html",gigs=gigs, tour = Tour.query.get(tour_id), form=form)

@app.route("/tours/delete/<tour_id>/", methods=["GET","POST"])
@login_required()
def tour_remove(tour_id):
    #jos kiertue poistetaan, niin silloin pitää kadota kaikki siihen liittyvät keikat. 
    if(tour_id == 1):
        return redirect('tour_index')
    tour = Tour.query.get(tour_id)
    gigs = Gig.query.filter(Gig.tour_id == tour_id)
    
    for gig in gigs: 
        db.session().delete(gig)
        db.session().commit()
    
    db.session().delete(tour)
    db.session().commit()

    
    
    return render_template("tour/removeFeedback.html", tour=tour)

