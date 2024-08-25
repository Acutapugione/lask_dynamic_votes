import random
from flask import Flask, render_template


class Client(object):
    def __init__(self, app: Flask):
        self.app = app
        self.app.add_url_rule("/", view_func=self.index)
        self.app.add_url_rule("/data", view_func=self.data)

    def data(self):
        return {"my little pohny": 123}

    def index(
        self,
        required_methods=[
            "GET",
        ],
    ):
        number = random.randint(0, 10000)
        return render_template("index.html", number=number)

    def run(self, debug: bool = True):
        self.app.run(debug=debug)


def main():
    cli = Client(Flask(__name__))
    cli.run()


if __name__ == "__main__":
    main()
