from flask import Flask
from random import randint

app = Flask(__name__)
num = randint(0, 9)

@app.route("/")
def root():
    return "<h1>Hello world!</h1>" \
            "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>"

@app.route("/<int:guess_number>")
def play_the_game(guess_number):
    if guess_number == num:
        output = "<h1 style='color=green'>You found me!</h1>" \
                "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"
    elif guess_number < num:
        output = "<h1 style='color=yellow'>Too low, try again!</h1>" \
                "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
    elif guess_number > num:
        output = "<h1 style='color=red'>Too high, try again!</h1>" \
                "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"
    return output

if __name__ == "__main__":
    #Run the app in debug mode and auto-reload
    app.run(debug=True)

