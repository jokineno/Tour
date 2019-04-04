from application import app, db
from flask import redirect, render_template, request, url_for
from application.tour.models import Tour
from application.tour.forms import TourForm
from flask_login import login_required, current_user


@app.route("/tours/", methods=["GET"])
def tour_index():
    alltours= Tour.query.all()
    return render_template("tour/tourform.html", tours=alltours)

    