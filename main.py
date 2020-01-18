import os
from app import cria_app

# double underscore
# underline
# underscore
app = cria_app(os.environ["FLASK_ENV"])

if __name__ == "__main__":
    app.run(debug=True)