from flask import Flask, render_template #import from the flask library the functions Flask and render_template
app = Flask(__name__) #initializes the Flask object
@app.route('/') #associates the root() function with the ‘/’ route
def root():
    return render_template('main_page.html') #serve up the ‘index.html’ webpage
app.run(debug=True) #run the app, this must correspond to the variable name you chose
