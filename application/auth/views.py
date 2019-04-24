from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user

from application import app, db, login_required, login_manager
from application.auth.models import User, Role
from application.gigs.models import Gig
from application.tour.models import Tour

from application.auth.forms import LoginForm, RegistrationForm, ProfileForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)
    # mahdolliset validoinnit

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                               error = "Käyttäjätunnusta tai salasanaa ei löydy")


    print("Käyttäjä " + user.name + " tunnistettiin")
    login_user(user)
    return redirect(url_for("index"))    

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))    


@app.route("/auth/register", methods = ["GET", "POST"])
def auth_register():
    if request.method == "GET":
        return render_template("auth/registrationform.html", form = RegistrationForm())

    form = RegistrationForm(request.form)

    if not form.validate():
        return render_template("auth/registrationform.html", form = form)

    u = User(form.name.data, form.username.data, form.password.data)
    u.role_id = 1
    db.session().add(u)
    db.session().commit()

    tour = Tour.query.get(1)
    u.tours.append(tour)
    db.session().commit()

    return redirect(url_for("auth_login"))

@app.route("/auth/profile/", methods=["GET"])
@login_required()
def auth_profile_view():
    idnum = current_user.id
    form = ProfileForm(request.form)
    upcoming_gigs = Gig.upcoming_gigs(idnum)
    past_gigs = Gig.past_gigs(idnum)
    cancelled_gigs = Gig.cancelled_gigs(idnum)
    return render_template("auth/profileform.html",form=form, current = User.query.get(idnum), upcoming = upcoming_gigs, past = past_gigs, cancelled = cancelled_gigs)


@app.route("/auth/profile/edit/", methods=["GET","POST"])
@login_required()
def auth_profile_edit():
    if request.method == "GET":
        profile = User.query.get(current_user.id)
        form = ProfileForm(obj=profile)
    
        return render_template("auth/profileeditform.html",form=form,user_id=current_user.id)
    
    form = ProfileForm(request.form)
    if not form.validate():
        return render_template("auth/profileeditform.html", form = form)
    profile = User.query.get(current_user.id)
    
    profile.name = form.name.data
    profile.username = form.username.data
    profile.role = form.role.data
    
    db.session().commit()

    return redirect(url_for("auth_profile_view"))
    

@app.route("/auth/allusers/", methods=["GET"])
@login_required(role="ADMIN")
def user_list():
    return render_template("auth/userlist.html", users=User.query.all())

@app.route("/users/delete/<user_id>/", methods=["GET","POST"])
@login_required(role="ADMIN")
def users_remove(user_id):
    
    u = User.query.get(user_id)
    db.session().delete(u)
    db.session().commit()

    return redirect(url_for("user_list"))


@app.route("/auth/allusers/changestatus/<user_id>/", methods=["POST"])
@login_required(role="ADMIN")
def user_change_role(user_id):

    u = User.query.get(user_id)
    if u.role_id == 1:
        u.role_id = 2
        db.session().commit()
    elif u.role_id == 2: 
        u.role_id=1
        db.session().commit()
    

    return redirect(url_for("user_list"))