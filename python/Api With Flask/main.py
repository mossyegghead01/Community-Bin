from flask import Flask

app = Flask(__name__)

# the home of the entire thing, only consist of text.
# This mean for landing page where you can tell what your web(or API in this case) is all about.
@app.route("/")
def home():
    return "Welcome to home!"


# Part of the API, this one is send the user all available command
# This one is still manual because we just making a minimal setup/basic setup
# if you wish to automate it feel free to do it, you may use url_for method
@app.route("/help")
def help():
    # The basic idea of making API with something like flask is simple!
    # Just return a dictionary(or some of you mgiht know it as "json")
    # And it will count as API
    return {"commands": [
        "help", "hello"
    ]}


# another part of the API, this one is returning value with the name of "response" and it's value wich is "Hello"
@app.route("/hello")
def hello():
    return {"response": "hello"}


# If you wish to add some stuff to the API feel free
# Just make something similar to the code above
# Basically a route that return a dictionary


# error handler in case someone tried to call a command that does not exist
# or just simply run / wich is does not exist in our code
@app.errorhandler(404)
def code_404():
    return """Whoops, this page/method does not exist, 
    please re check your url.""", 404


if __name__ == "__main__":
    app.run()
