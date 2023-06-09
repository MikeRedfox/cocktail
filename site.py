from sqlmodel import SQLModel, Session, create_engine, Field, JSON, Column, select
import random
from flask import Flask, render_template
from main import Cocktail
from typing import List
import jsonpickle


app = Flask(__name__)
engine = create_engine("sqlite:///database.db")


@app.get('/random')
def get_random_cocktail():
    with Session(engine) as session:
        statement = select(Cocktail)
        results = session.exec(statement).all()
    r = random.choice(results)
    return jsonpickle.encode(r)

@app.route('/')
def home():
    return render_template('index.html')





if __name__ == '__main__':
    app.run(debug=True)