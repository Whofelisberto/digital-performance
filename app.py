from flask import Flask
from controllers.api_controller import api_bp
from controllers.web_controller import web_bp

app = Flask(__name__, template_folder="frontend/templates")
app.secret_key = "chave-super-secreta"

app.register_blueprint(api_bp)
app.register_blueprint(web_bp)

if __name__ == "__main__":
    app.run(debug=True)
