# api/app.py
from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics

def create_app():
    """Cria e configura uma instância da aplicação Flask."""
    app = Flask(__name__)

    # Expõe as métricas padrão do Flask (/metrics)
    PrometheusMetrics(app)

    @app.route('/')
    def home():
        return jsonify({
            "status": "online",
            "message": "API Flask está rodando!"
        })

    @app.route('/health')
    def health():
        """Endpoint de Health Check."""
        return jsonify({"status": "ok"}), 200

    return app

app = create_app()

if __name__ == "__main__":
    # A porta 8085 será gerenciada pelo Gunicorn no Docker
    app.run(host="0.0.0.0", port=8085, debug=True)