#!/usr/bin/python3
"""Defines the State class."""
import models
from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from models.base_model import BaseModel
from models.city import City
import sqlalchemy
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship
import shlex


class State(BaseModel, Base):
    """Represents a state for a MySQL database.

    Inherits from SQLAlchemy Base and links to the MySQL table states.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store States.
        name (sqlalchemy String): The name of the State.
        cities (sqlalchemy relationship): The State-City relationship.
    """
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City",  backref="state", cascade="delete, delete-orphan, all")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """Initializes a new State.

        Args:
            *args: Unused.
            **kwargs: Key/value pairs of attributes.
        """
        super().__init__(*args, **kwargs)

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Get a list of all related City objects."""
            city_list = []
            var = models.storage.all()
            lista = []
            for key in var:
                city = key.replace('.', ' ')
                city = shlex.split(city)
                if (city[0] == 'City'):
                    lista.append(var[key])
            for elem in lista:
                if (elem.state_id == self.id):
                    city_list.append(elem)
            return (city_list)
