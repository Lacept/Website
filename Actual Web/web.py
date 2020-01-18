from flask import Flask, send_from_directory,render_template, request, url_for #import from the flask library the functions Flask and render_template
from DBHandler import DBUtil
import DBHandler
from json2html import *
import logging

app = Flask(__name__) #initializes the Flask object
@app.route('/<path:filename>') #associates the root() function with the ‘/’ route
def routing(filename):
    return send_from_directory("templates/Index", filename) #serve up the ‘index.html’ webpage

@app.route("/")
def root():
    return send_from_directory("templates/Index", "index.html")

# lis_MIPoly = {"MI": [], "poly": []}
# #MI
# if L1R4 <= 20:
#     lis.append({"School": "Millennial Institution", "Cutoff": 20})
##db = DBUtil.getDBUtil()
##db.convertJson(db.getEligibleScience(q1), DBHandler.SchoolType.JC))
##db.closeConnections()
#
@app.route('/How')
def table1():
    return send_from_directory('templates/Help','table.html')

@app.route('/results', methods=["POST"]) #associates the show() function with the ‘/’ route
# def show():
#     #@app.route('/show',methods=["POST"]) 
#     L1R5 = request.form['q1'] 
#     L1R4 = request.form['q2']
#     db = DBUtil.getDBUtil()
#     JC_Sci = db.convertJson(db.getEligibleScience(L1R5), DBHandler.SchoolType.JC)
#     JC_Art = db.convertJson(db.getEligibleArt(L1R5), DBHandler.SchoolType.JC)
#     Poly = db.convertJson(db.getEligiblePoly(L1R4), DBHandler.SchoolType.POLY)
#     MI = []
#     if int(L1R4) <= 20:
#         MI = [{"School": "Millennial Institution", "Cutoff": 20}]

#     JC_Sci = json2html.convert(JC_Sci, table_attributes="id=\"table_id\" class=\"display\"")
#     JC_Art = json2html.convert(JC_Art, table_attributes="id=\"table_id\" class=\"display\"")
#     Poly = json2html.convert(Poly, table_attributes="id=\"table_id\" class=\"display\"")
#     MI = json2html.convert(MI, table_attributes="id=\"table_id\" class=\"display\"")
#     db.closeConnections()
#     return render_template('show.html', Sci = JC_Sci, Arts = JC_Art, Polytech = Poly, MI = MI)  #serve up the ‘show.html’ webpage

def show():
    #@app.route('/show',methods=["POST"]) 
    L1R5 = request.form['q1'] 
    L1R4 = request.form['q2']
    db = DBUtil.getDBUtil()
    JC_Sci = db.convertJson(db.getEligibleScience(L1R5), DBHandler.SchoolType.JC)
    JC_Art = db.convertJson(db.getEligibleArt(L1R5), DBHandler.SchoolType.JC)
    Poly = db.convertJson(db.getEligiblePoly(L1R4), DBHandler.SchoolType.POLY)
    unavail_string = "Sorry, you do not meet the requirments for any courses. 😔"
    if int(L1R4) <= 20:
        MI = [{"School": "Millennial Institution", "Cutoff": 20}]
        MI = json2html.convert(MI, table_attributes="id=\"table_id\" class=\"display\"")
    else:
        MI = 'Sorry, you do not meet the requirments for Millennial Institution. 😔'
    if int(L1R5) > 20:
        JC_Sci = unavail_string
        JC_Art = unavail_string
    else:
        JC_Sci = json2html.convert(JC_Sci, table_attributes="id=\"table_id\" class=\"display\"")
        JC_Art = json2html.convert(JC_Art, table_attributes="id=\"table_id\" class=\"display\"")

    if int(L1R4) > 26:
        Poly = unavail_string
    else:
        Poly = json2html.convert(Poly, table_attributes="id=\"table_id\" class=\"display\"")
    db.closeConnections()
    return render_template('show.html', Sci = JC_Sci, Arts = JC_Art, Polytech = Poly, MI = MI)  #serve up the ‘show.html’ webpage

#app.run()
app.run(host="0.0.0.0", port=80) #run the app, this must correspond to the variable name you chose