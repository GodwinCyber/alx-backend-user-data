#!/usr/bin/env python3
"""
DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Add a user to the database: Implement the add_user
            method, which has two required string arguments:
            email and hashed_password, and returns a User object.
            The method should save the user to the database.
            No validations are required at this stage.
        """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """Find a user by a key word argument: l implement the DB.find_user_by
            method. This method takes in arbitrary keyword arguments and
            returns the first row found in the users table as filtered by
            the method’s input arguments. No validation of input arguments
            required at this point.
        Note:
            Make sure that SQLAlchemy’s NoResultFound and InvalidRequestError
            are raised when no results are found, or when wrong query
            arguments are passed, respectively.
        Warning:
            NoResultFound has been moved from sqlalchemy.orm.exc to
            sqlalchemy.exc between the version 1.3.x and 1.4.x of SQLAchemy-
            please make sure you are importing it from sqlalchemy.orm.exc
        """
        if not kwargs:
            raise InvalidRequestError
        cols_keys = User.__table__.columns.keys()
        for key, value in kwargs.items():
            if key not in cols_keys:
                raise InvalidRequestError
        user = self._session.query(User).filter_by(**kwargs).first()
        if user is None:
            raise NoResultFound
        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """Update a user by user_id as integer: Implement the
            DB.update_user method and return None.
            The method will use find_user_by to locate the user to
            update, then will update the user’s attributes as passed in
            the method’s arguments then commit changes to the database.
            If an argument that does not correspond to a user
            attribute is passed, raise a ValueError.
        """
        user = self.find_user_by(id=user_id)
        for key, value in kwargs.items():
            if key not in User.__table__.columns.keys():
                raise ValueError
        setattr(user, key, value)
        self._session.commit()
        return None

