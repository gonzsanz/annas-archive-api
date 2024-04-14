from sanic import Sanic
from sanic_cors import CORS

from . import handlers

app = Sanic("api")

# Habilitar CORS para todas las rutas
CORS(app)

# También puedes configurar CORS para rutas específicas
# CORS(app, resources={r"/recents": {"origins": "*"}})
# CORS(app, resources={r"/search": {"origins": "*"}})
# CORS(app, resources={r"/download": {"origins": "*"}})

app.add_route(handlers.recents, "/recents", name="Recents")
app.add_route(handlers.search, "/search", name="Search")
app.add_route(handlers.download, "/download", name="Download")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
