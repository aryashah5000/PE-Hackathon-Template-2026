from app.database import db
from app.models.link import Link
from app import create_app

app = create_app()
print("creating tables...")
with app.app_context():
    db.create_tables([Link])
print("done.")