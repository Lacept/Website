from DBHandler import DBUtil

db = DBUtil.getDBUtil()
print(db.getEligibleScience(4))
db.closeConnections()
