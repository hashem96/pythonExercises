import flask
from random import randrange

app = flask.Flask("rollNumber")

irand = randrange(1, 100)


@app.route("/")

def index():

   message = "Welcome to our guessing game !"

   return message


@app.route("/roll/<int:number>")
def roll(number) :

   if number > 100 or number < 0 :
      return "Your guess should be between 1 and 100"

   if number == irand :
      return "Congrats , You guess the number correctly"
   else:
      return f"Sorry you failed the number was {irand}. Try Again "
   

app.run(debug=True)
