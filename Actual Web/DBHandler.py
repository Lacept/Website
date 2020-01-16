import sqlite3
from enum import Enum
from Map import Map
from typing import Union

dbfolder = "db/"

class SchoolType(Enum):
    JC = 1
    POLY = 2

class DBUtil:
    _instance = None
    
    jc = Map({ # gamer sql
        "db": dbfolder + "JC_2019.db",
        "query": Map({
            "art": """
                SELECT JuniorCollege, Arts
                FROM JC_2019
                WHERE Arts >= ?
                ORDER BY Arts ASC
            """,
            "science": """
                SELECT JuniorCollege, Science_IB
                FROM JC_2019
                WHERE Science_IB >= ?
                ORDER BY Science_IB ASC
            """
        })
    })

    poly = Map({
        "db": dbfolder + "Poly_2019.db",
        "query": Map({
            "jae": """
                SELECT *
                FROM Poly_2019
                WHERE JAE_ELR2B2 >= ?
                ORDER BY JAE_ELR2B2 ASC
            """
        })
    })
    
    def __init__(self):
        if DBUtil._instance == None:
            self.connection = Map({"poly": sqlite3.connect(DBUtil.poly.db), "jc": sqlite3.connect(DBUtil.jc.db)})
            DBUtil._instance = self
            

    @staticmethod
    def getDBUtil() -> "DBUtil":
        if DBUtil._instance == None:
            DBUtil()
        return DBUtil._instance


    def executeScoreQuery(self, schoolType: SchoolType, query: str, score: Union[int, str]) -> list:
        try:
            res = self.getConnection(schoolType).execute(query, [str(score)])
            return res.fetchall()
        except Exception:
            raise Exception("Error retrieving database results")


    # only use below functions
    def convertJson(self, res: list, schoolType: SchoolType) -> list:
        lis = []
        _format = ("School", "Cutoff") if schoolType == SchoolType.JC else ("School", "Code", "Name", "Cutoff")
        for i in res:
            lis.append(dict(zip(_format, i)))
        return lis
            

    def getConnection(self, schoolType: SchoolType) -> sqlite3.Connection:
        return self.connection.jc if schoolType == schoolType.JC else self.connection.poly

    def closeConnections(self):
        DBUtil._instance = None
        for i in self.connection.values():
            i.close()

    def getEligibleArt(self, l1r5: Union[int, str]) -> list: # jc art
        return self.executeScoreQuery(SchoolType.JC, DBUtil.jc.query.art, l1r5)

    def getEligibleScience(self, l1r5: Union[int, str]) -> list: # jc science
        return self.executeScoreQuery(SchoolType.JC, DBUtil.jc.query.science, l1r5)
    
    def getEligiblePoly(self, l1r4: Union[int, str]) -> list: # poly
        return self.executeScoreQuery(SchoolType.POLY, DBUtil.poly.query.jae, l1r4)

