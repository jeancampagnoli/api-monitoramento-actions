from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "API Flask está rodando!🚀🚀🚀🚀🚀🚀"

if __name__ == "__main__":
    print("🚀 Iniciando API Flask na porta 8085...")
    print("📋 Endpoints disponíveis:")
    print("   GET  /health")
    print("   GET  /")
    print("   CRUD /api/users")
    print("   CRUD /api/products")
    app.run(host="0.0.0.0", port=8085, debug=True)
