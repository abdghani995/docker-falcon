from app.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

# BASE
'''
	declarative_base() is a factory function that constructs a base class
	for declarative class definitions.
	Ref : https://docs.sqlalchemy.org/en/13/orm/extensions/declarative/api.html
'''
Base = declarative_base()

def get_engine():
	return create_engine(settings.get('DATABASE_URL'))

def drop_table():
	Base.metadata.drop_all(create_engine(settings.get('DATABASE_URL')))

def create_all(drop=None):
	print("----- Created all called -----")
	print('Database : {}'.format(settings.get('DATABASE_URL')))
	return Base.metadata.create_all(create_engine(settings.get('DATABASE_URL'), echo=True))

def get_session():
	print("=================================")
	print("Session Created")
	print("=================================")
	engine = get_engine()
	session_factory = sessionmaker(bind=engine, autoflush=True)
	sess = scoped_session(session_factory)
	return sess


from .countries import Countries
