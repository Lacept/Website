from flask import Flask, send_from_directory,render_template, request #import from the flask library the functions Flask and render_template
from DBHandler import DBUtil
import DBHandler
from json2html import *
import logging

app = Flask(__name__) #initializes the Flask object
@app.route('/<path:filename>') #associates the root() function with the ‘/’ route
def root(filename):
    return send_from_directory("templates/Index", filename) #serve up the ‘index.html’ webpage
##def calcScore():
##    # find how to get the form body here
##    # return json {"art": [], "science" : []}
##    pass

#

# #Poly
# lis_MIPoly = {"MI": [], "poly": []}
# for i in db.getEligiblePoly(7):
#     lis["poly"].append(dict(zip(("School", "Code", "Name", "Cutoff"), i)))
# #MI
# if L1R4 <= 20:
#     lis.append({"School": "Millennial Institution", "Cutoff": 20})

# # JC
# lis_JC = {"art": [], "science": []}
# for i in db.getEligibleScience(4):
#     lis["science"].append(dict(zip(("School", "Cutoff"), i)))

# for i in db.getEligibleArt(4):
#     lis["art"].append(dict(zip(("School", "Cutoff"), i)))
# print(lis)

##db = DBUtil.getDBUtil()
##db.convertJson(db.getEligibleScience(q1), DBHandler.SchoolType.JC))
##db.closeConnections()
#
@app.route('/api/calcScore', methods=["POST"]) #associates the show() function with the ‘/’ route
def show():
    #@app.route('/show',methods=["POST"]) 
    L1R5 = request.form['q1'] 
    L1R4 = request.form['q2']
    db = DBUtil.getDBUtil()
    JC_Sci = db.convertJson(db.getEligibleScience(L1R5), DBHandler.SchoolType.JC)
    JC_Art = db.convertJson(db.getEligibleArt(L1R5), DBHandler.SchoolType.JC)
    Poly = db.convertJson(db.getEligiblePoly(L1R4), DBHandler.SchoolType.POLY)
    JC_Sci = json2html.convert(JC_Sci)
    JC_Art = json2html.convert(JC_Art)
    Poly = json2html.convert(Poly)
    db.closeConnections()
    return render_template(send_from_directory("templates/Show", 'show.html'), Sci=JC_Sci, Arts=JC_Art, Polytech = Poly)  #serve up the ‘show.html’ webpage


app.run() #run the app, this must correspond to the variable name you chose
