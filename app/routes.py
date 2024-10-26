from flask import render_template, redirect, url_for, request
from sqlmodel import select
from . import app
from .models import engine, Option, Question, SESSION, Vote


def mock():
    with SESSION.begin() as session:
        lang = Question(
            name="Ваша улюблена мова програмування",
            options=[
                Option(name="Python"),
                Option(name="Java"),
                Option(name="JavaScript"),
                Option(name="C#"),
                Option(name="C++"),
            ],
        )
        gender = Question(
            name="Оберіть зайве",
            options=[
                Option(name="Male"),
                Option(name="Female"),
                Option(name="Neither"),
                Option(name="Helicopter"),
                Option(name="Quadrobber"),
            ],
        )
        session.add(gender)
        session.add(lang)


mock()


def endpoints() -> list:
    return [rule.endpoint for rule in app.url_map.iter_rules()]


@app.get("/")
def index():
    return render_template("index.html", endpoints=endpoints())


@app.get("/vote/")
def vote():
    with SESSION.begin() as session:
        questions = session.scalars(select(Question)).all()
        return render_template("vote.html", questions=questions, endpoints=endpoints())


@app.post("/vote/result/")
def vote_result():
    question_id = request.form.get("question_id")
    option_id = request.form.get("option_id")
    with SESSION.begin() as session:
        question = session.get(Question, question_id)
        option = session.get(Option, option_id)
        if question and option:
            session.add(Vote(question=question, option=option))
        print(f"{question=},  {option=}")
        return redirect(url_for(index.__name__))
    return redirect(url_for(vote.__name__))
