from flask import Flask, request, render_template
from random import choice, randint


COMPLIMENTS = ["smart", "clever", "tenacious", "awesome", "Pythonic", "automagical"]

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")



@app.route('/lucky')
def lucky_number():
    lucky_num = randint(1, 10)

    return render_template("lucky.html", num=lucky_num)


@app.route('/form')
def show_form():
    # add your code here
    return render_template("form.html")


@app.route('/greet')
def offer_greeting():
    # add your code here
    print "this is what is getting passed to python server.py %s" % (request.args)
    person = request.args.get("person")
    compliment = choice(COMPLIMENTS)

    return render_template("compliment.html", 
                            name=person, 
                            nice_thing=compliment)



if __name__ == "__main__":
    app.run(debug=True)
