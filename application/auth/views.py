from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user

from application import app, db
from application.auth.models import User
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

    db.session().add(u)
    db.session().commit()

    return redirect(url_for("auth_login"))

@app.route("/auth/profile/", methods=["GET"])
def auth_profile_view():
    idnum = current_user.id
    form = ProfileForm(request.form)
    
    return render_template("auth/profileform.html",form=form, current = User.query.get(idnum))


@app.route("/auth/profile/edit/", methods=["GET","POST"])
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
    
    db.session().commit()

    return redirect(url_for("auth_profile_view"))
    

