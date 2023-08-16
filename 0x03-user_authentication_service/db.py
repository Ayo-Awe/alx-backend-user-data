#!/usr/bin/env python3

"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

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
        """Create a new user with email and
        password and adds the user to the
        database
        """

        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()

        return user

    def find_user_by(self, **kwargs) -> User:
        """Finds and returns the first user that matches the set
        of filters provided in the keyword arguments
        """

        session = self._session
        user = session.query(User).filter_by(**kwargs).one()

        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """Finds and updates a user by id
        """
        session = self._session
        user = self.find_user_by(id=user_id)

        for key, value in kwargs.items():
            if key not in dir(user):
                raise ValueError()
            user.__setattr__(key, value)

        session.add(user)
        session.commit()
