import os
from config import db
from models import Person

# Data to initialize db with
PEOPLE = [
    {'fname': 'Doug', 'lname': 'Farrell'},
    {'fname': 'Kent', 'lname': 'Brockman'},
    {'fname': 'Bunny','lname': 'Easter'}
]

# Delete the database file if it exists
if os.path.exists('people.db'):
    os.remove('people.db')

# Create the database
db.create_all()

# Iterate over PEOPLE
for person in PEOPLE:
    # 1. create the person object
    p = Person(lname=person['lname'], fname=person['fname'])
    # 2. Add it to session
    db.session.add(p)

# 3. Commit the session

db.session.commit()
