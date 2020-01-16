from flask import Flask, send_from_directory, jsonify, request, Response
from DBHandler import DBUtil
import DBHandler

app = Flask(__name__)
@app.route('/<path:filename>')
def serve(filename):
    return send_from_directory("templates", filename)

@app.route("/")
def root():
    return send_from_directory("templates", "index.html")

# api to compare score with provided input and return json output with keys: science, art, poly
@app.route("/api/calcScore", methods=["GET", "POST"])
def calcScore():

    l1r5 = request.form.get("l1r5", None)
    l1r5 = l1r5 if l1r5 is None or l1r5.isdecimal() else None

    l1r4 = request.form.get("l1r4", None)
    l1r4 = l1r4 if l1r4 is None or l1r4.isdecimal() else None

    if not(l1r4 or l1r5):
        return Response("Invalid parameters supplied", status=400)

    if l1r4 and l1r5:
        a, b = int(l1r4), int(l1r5)
        if a >= b or not(2 <= b <= 54 and 1 <= a <= 45):
            return Response("Invalid parameters supplied1", status=400)


    res = {
        "science": [],
        "art": [],
        "poly": []
    }
    
    db = DBUtil.getDBUtil()

    try:
        if l1r5 is not None:
            res["science"] = db.convertJson(db.getEligibleScience(l1r5), DBHandler.SchoolType.JC)
            res["art"] = db.convertJson(db.getEligibleArt(l1r5), DBHandler.SchoolType.JC)
        
        if l1r4 is not None:
            res["poly"] = db.convertJson(db.getEligiblePoly(l1r4), DBHandler.SchoolType.POLY)
            if int(l1r4) <= 20:
                res["poly"].append({"School": "Millennial Institution", "Code": "", "Name": "", "Cutoff": 20})
        
    except Exception as e:
        return Response(e.message, status=400)
    finally:
        db.closeConnections()
    

    return jsonify(res)

app.run(host="0.0.0.0", port=80)
