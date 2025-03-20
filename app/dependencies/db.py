from app.core.database import db


def get_db():
    db.connect(reuse_if_open=True)
    try:
        yield
    finally:
        if not db.is_closed():
            db.close()
