from flask import Flask # Import the Flask library for use in our routes

app =Flask(__name__) # Create an “app” variable to use for route creation

@app.route('/') # Import the Flask library for use in our routes
def homepage(): # Define a function “homepage”
    return "Hello, world!" # Return a response of “Hello, world!”

@app.route('/sharks')
def sharks():
    return """
    <h1>Welcome Sharks!</h1>
    <p> Sharks are cool because ... </p> """

@app.route('/school')
def make_school():
    return """
    <h1>Make School is a really great school!</h1>
    <p> Welcome incoming students </p> """

@app.route('/profile/<users_name>')
def profile(users_name):
    return "Hello " + users_name

if __name__ == '__main__': # If this is the file being run
    app.run(debug=True) # Run the web application in debug mode