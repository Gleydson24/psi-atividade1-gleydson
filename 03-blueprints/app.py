from flask import Flask
from blueprints.auth import auth_bp
from blueprints.catalog import catalog_bp
from blueprints.comments import comments_bp

app = Flask(__name__)
app.secret_key = "chave-secreta"

app.register_blueprint(auth_bp)
app.register_blueprint(catalog_bp)
app.register_blueprint(comments_bp, url_prefix="/post/<int:post_id>")

if __name__ == "__main__":
    app.run(debug=True)