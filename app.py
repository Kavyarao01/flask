# Step 1 - To import FLASK
from flask import Flask, request

# Step 2 - Create the object with a parameter __name__
app = Flask(__name__)

###################################################
# Step 3 - Create an END POINT using routes and bind them with a functionality

@app.route('/')
def home_page():
    return "<h1 style='background-color:None;'text-align:center;'>Hello! </h1><h2>I am Kavya. Welcome to Home Page.Please redirect to     http://127.0.0.1:5000/upper</h2>"


@app.route('/upper')
def UpperCase():
    user = request.args.get('user')
    if user:
        user = user.upper()

        return f'<div><h2>Your Username is {user}</h2></div>'
    else:
        return '<div><h1>Please input your username </h1></div>'


###################################################

# Step 4 - Run the app
if __name__ == '__main__':
    app.run(debug=True)

