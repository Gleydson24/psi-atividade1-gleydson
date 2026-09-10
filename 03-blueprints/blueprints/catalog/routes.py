from flask import render_template, request, abort
from . import catalog_bp
LIVROS = {
    1: {"titulo": "Dom Casmurro", "autor": "Machado de Assis", "ano": 1899, "resenhas": []},
    2: {"titulo": "O Cortiço", "autor": "Aluísio Azevedo", "ano": 1890, "resenhas": []},
    3: {"titulo": "Capitães da Areia", "autor": "Jorge Amado", "ano": 1937, "resenhas": []},
    4: {"titulo": "A Hora da Estrela", "autor": "Clarice Lispector", "ano": 1977, "resenhas": []}
}
@catalog_bp.route('/')
def index():
    q = request.args.get('q', '')
    resultados = [l for id_l, l in LIVROS.items() if q.lower() in l['titulo'].lower()] if q else LIVROS.values()
    return render_template('catalog/index.html', livros=resultados, q=q)
@catalog_bp.route('/livro/<int:livro_id>')
def ver_livro(livro_id):
    livro = LIVROS.get(livro_id)
    if livro is None:
        abort(404) 
    return render_template('catalog/livro.html', livro=livro, livro_id=livro_id)