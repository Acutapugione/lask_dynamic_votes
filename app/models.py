from sqlmodel import SQLModel, Field, Relationship, create_engine
from sqlalchemy.orm import sessionmaker


class Option(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str = Field(unique=True)
    question_id: int = Field(foreign_key="question.id")
    # question: "Question" = Relationship()


class Question(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str = Field(unique=True)
    options: list["Option"] = Relationship()


class Vote(SQLModel, table=True):
    id: int = Field(primary_key=True)
    question_id: int = Field(foreign_key="question.id")
    option_id: int = Field(foreign_key="option.id")
    question: Question = Relationship()
    option: Option = Relationship()


engine = create_engine("sqlite:///my_db.db", echo=True)
SESSION = sessionmaker(bind=engine)
SQLModel.metadata.drop_all(engine)
SQLModel.metadata.create_all(engine)
