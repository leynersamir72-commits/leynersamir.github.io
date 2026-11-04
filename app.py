import os
from flask import Flask, render_template, abort, url_for, Response
from data import PROVINCIA, CANTONES, AUTORIDADES

app = Flask(__name__)
IMG_DIR = os.path.join(app.static_folder, "img")

@app.context_processor
def helpers():
    def _buscar(base):
        base = os.path.splitext(base)[0]
        for ext in (".jpg", ".jpeg", ".png", ".webp", ".svg"):
            if os.path.exists(os.path.join(IMG_DIR, base + ext)):
                return base + ext
        return None

    def img(nombre, etiqueta=""):
        """Foto del usuario (jpg/png/webp) o ilustración .svg; si no hay nada, un recuadro con el nombre."""
        f = _buscar(nombre)
        if f:
            return url_for("static", filename="img/" + f)
        return url_for("placeholder", texto=etiqueta or nombre)

    def foto_propia(nombre):
        """True si el usuario subió su propia imagen (no svg), p. ej. un mapa."""
        base = os.path.splitext(nombre)[0]
        return any(os.path.exists(os.path.join(IMG_DIR, base + e)) for e in (".jpg", ".jpeg", ".png", ".webp"))
    return {"cantones_menu": CANTONES, "img": img, "foto_propia": foto_propia}

@app.route("/placeholder/<texto>.svg")
def placeholder(texto):
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 360">
<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
<stop offset="0" stop-color="#2e8b6a"/><stop offset="1" stop-color="#1b4f7a"/></linearGradient></defs>
<rect width="640" height="360" fill="url(#g)"/>
<text x="320" y="170" font-family="Arial" font-size="34" fill="#fff" text-anchor="middle">{texto}</text>
<text x="320" y="210" font-family="Arial" font-size="18" fill="#dfeee8" text-anchor="middle">Agrega tu foto en static/img</text>
</svg>'''
    return Response(svg, mimetype="image/svg+xml")

@app.route("/")
def index():
    return render_template("index.html", p=PROVINCIA, cantones=CANTONES)

@app.route("/autoridades")
def autoridades():
    return render_template("autoridades.html", autoridades=AUTORIDADES)

@app.route("/canton/<slug>")
def canton(slug):
    c = CANTONES.get(slug)
    if not c:
        abort(404)
    return render_template("canton.html", c=c, slug=slug)

if __name__ == "__main__":
    app.run(debug=True)
