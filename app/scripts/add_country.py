import uuid
from app.model import *
from sqlalchemy import Column, String


create_all()

sess = get_session()
sess.add(Countries(
    country_id = uuid.uuid4(),
    country_name = "Denmark"
))
sess.commit()
sess.close()
