#!/usr/bin/python3
"""A script to list all `State` objects from the database `hbtn_0e_6_usa`
...
...
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    engine = create_engine(f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@\
localhost/{sys.argv[3]}", pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    found = False
    for state in session.query(State):
        if state.name == sys.argv[4]:
            print(f"{state.id}")
            found = True
            break
    if found is False:
        print("Not found")
