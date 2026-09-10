from flask import request, redirect, url_for, session, render_template
from blueprints.comments import comments_bp
import models
@comments_bp.route("/novo", methods=["POST"])
def novo_comentario(post_id):
    if "usuario" not in session:
        return redirect(url_for("auth.login"))
    if request.method == "POST":
        nova_resenha = {
            "id": models.proximo_id_resenha,
            "livro_id": post_id,
            "usuario": session["usuario"],
            "texto": request.form["texto"],
            "nota": int(request.form.get("nota", 5))
        }
        models.resenhas.append(nova_resenha)
        models.proximo_id_resenha += 1
        return redirect(url_for("posts.ver_post", post_id=post_id))
