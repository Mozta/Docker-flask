from flask.cli import FlaskGroup
from project import app, db, User

cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()
    print("Database tables created.")


@cli.command("seed_db")
def seed_db():
    db.session.add(User(email="rafa@correo.com"))
    db.session.commit()
    print("Database seeded with initial data.")


if __name__ == "__main__":
    cli()
