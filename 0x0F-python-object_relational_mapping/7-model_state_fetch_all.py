#!/usr/bin/python3
"""A script to list all `State` objects from the database `hbtn_0e_6_usa`"""
import sys

from sqlalchemy import (create_engine)
from sqlalchemy import select
from sqlalchemy.orm import Session
from model_state import Base, State # noqa


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    with Session(engine) as session:
        statement = select(State).order_by(State.id)
        rows = session.execute(statement).all()
        for row in rows:
            print(f"{row[0].id}: {row[0].name}")
