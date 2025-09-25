from flask import Flask
from controllers.api_controller import api_bp

app = Flask(__name__)
app.secret_key = "chave-super-secreta"  # troque em produção

app.register_blueprint(api_bp)

if __name__ == "__main__":
    app.run(debug=True)
