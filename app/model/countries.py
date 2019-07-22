import uuid
import datetime
from sqlalchemy import  Column , ForeignKey, or_, String, DateTime,Boolean
from sqlalchemy.orm import relationship
from app.model import Base


class Countries(Base):
    __tablename__ = 'countries'

    country_id = Column(String , primary_key=True)
    country_name = Column(String )

    @property
    def repr(self):
        return{
            "country_id": self.country_id,
            "country_name": self.country_name
        }
