from flask import Flask, send_from_directory #import from the flask library the functions Flask and render_template
app = Flask(__name__) #initializes the Flask object
@app.route('/<path:filename>') #associates the root() function with the ‘/’ route
def root(filename):
    return send_from_directory("templates", filename) #serve up the ‘index.html’ webpage

@app.route("/api/calcScore")
def calcScore():
    # find how to get the form body here
    # return json {"art": [], "science" : []}
    pass

app.run(debug=True) #run the app, this must correspond to the variable name you chose
