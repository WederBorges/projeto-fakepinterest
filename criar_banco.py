from pinterest import app, db
from pinterest import models

with app.app_context():
    db.drop_all()
    db.create_all()
    