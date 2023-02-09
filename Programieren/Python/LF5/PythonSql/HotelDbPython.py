import sqlite3
def CreateHotelTbl(constr : str):
    DbCon = sqlite3.connect(constr)
    DbCursor = DbCon.cursor()
    SqlCommand = """Create Table IF NOT EXISTS tbl_gast(
        Gast_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Gast_Vorname Text,
        Gast_Nachname text,
        Gast_Zimmer text)"""
    
    DbCursor.execute(SqlCommand)
    DbCon.commit()
    DbCon.close()

constring="Programieren\\Python\\LF5\\PythonSql\\mitarbeiterverwaltung.db"
CreateHotelTbl(constring)