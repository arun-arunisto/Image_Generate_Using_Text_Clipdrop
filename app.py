from flask import Flask
import os
from dotenv import load_dotenv
from application.views import app_bp

load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

app.register_blueprint(app_bp)

if __name__ == "__main__":
    app.run()