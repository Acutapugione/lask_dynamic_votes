import random
from json import dump, load
from typing import final
from flask import Flask, render_template


def custom_filter(value):
    return f"{value}s"


@final
class Client(object):
    def __init__(self, app: Flask):
        self.app = app
        self.app.jinja_env.filters["custom_filter"] = custom_filter
        self.app.add_url_rule("/", view_func=self.index)
        self.app.add_url_rule("/students", view_func=self.students)

    def students(self):
        def get_students(filename: str = "data.json") -> list[dict]:
            with open(filename, "r", encoding="utf-8") as f:
                return load(f)

        return render_template("list.html", items=get_students())

    def index(
        self,
        required_methods=[
            "GET",
        ],
    ):
        endpoints = [rule.endpoint for rule in self.app.url_map.iter_rules()]

        number = random.randint(0, 10000)
        return render_template("index.html", number=number, endpoints=endpoints)

    def run(self, debug: bool = True):
        self.app.run(debug=debug)


def main():
    cli = Client(Flask(__name__))
    cli.run()


if __name__ == "__main__":
    main()
