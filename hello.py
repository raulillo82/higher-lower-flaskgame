from flask import Flask
app = Flask(__name__)

def make_bold(function):
    def wrapper_function():
        function()
        return "<b>" + function() + "</b>"
    return wrapper_function

def make_emphasis(function):
    def wrapper_function():
        function()
        return "<em>" + function() + "</em>"
    return wrapper_function

def make_underlined(function):
    def wrapper_function():
        return "<u>" + function() + "</u>"
    return wrapper_function

@app.route("/")
def hello_world():
    return "Hello world!"

@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye"

@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}, you are {number} years old."

if __name__ == "__main__":
    #Run the app in debug mode and auto-reload
    app.run(debug=True)
