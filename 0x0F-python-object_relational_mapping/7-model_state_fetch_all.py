#!/usr/bin/python3
"""A script to list all `State` objects from the database `hbtn_0e_6_usa`"""
import sys

from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
from model_state import Base, State # noqa


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    session = Session(bind=engine)
    for state in session.query(State).order_by(State.id):
        print(f"{state.id}: {state.name}")
