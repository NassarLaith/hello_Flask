from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"


@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/dojo')
def say_dojo():
    return 'Dojo!'

@app.route('/say/<string:varible>')
def say_varible(varible):
    return f"hi {varible}!"

@app.route('/repeat/<int:num>/<string:word>')  
def repeat_word(num, word):
    return f" {word} "*num


@app.route('/<path:path>')   #If the user goes to a page that doesn't exist.
def wrong_route(path):
    return "Sorry! No response. Try again."





if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.