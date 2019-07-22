import app.util.json as json
from app.util.error import HTTPError

class SQLAlchemySessionManager:
    """
        Create a scoped session for every request and close it when the request ends.

        For further reference :-
        -------------------------
        Py Falcon - middleware:- https://falcon.readthedocs.io/en/stable/api/middleware.html
        Sql Alchemy - scoped session :- https://docs.sqlalchemy.org/en/13/orm/contextual.html#sqlalchemy.orm.scoping.scoped_session
        Idea :- https://stackoverflow.com/questions/38863057/sqlalchemy-and-falcon-session-initialization
    """

    def __init__(self, Session):
        try:
            self.Session = Session
        except Exception as e:
            raise HTTPError(400, "Error connecting to db")

    def process_resource(self, req, resp, resource, params):
        resource.sess = self.Session()

    def process_response(self, req, resp, resource, req_succeeded):
        if hasattr(resource, 'sess'):
            self.Session.remove()
