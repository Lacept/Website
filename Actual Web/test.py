from DBHandler import DBUtil
import DBHandler

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

db = DBUtil.getDBUtil()

print(db.convertJson(db.getEligibleScience(10), DBHandler.SchoolType.JC))

db.closeConnections()
