from flask import render_template, request, redirect, url_for, session
from blueprints.auth import auth_bp
import models
@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        nome = request.form["nome"]
        senha = request.form["senha"]
        for usuario in models.usuarios:
            if usuario["nome"] == nome and usuario["senha"] == senha:
                session["usuario"] = nome
                return redirect(url_for("catalog.index"))
        return render_template("auth/login.html", erro="Usuário ou senha incorretos")
    return render_template("auth/login.html")
@auth_bp.route("/logout")
def logout():
    session.pop("usuario", None)
    return redirect(url_for("catalog.index"))