import sqlite3
def ShowTable(constring:str)->bool:
    try:
        DbCon:sqlite3.Connection = sqlite3.connect(constring)
        DbCursor = DbCon.cursor()
        SqlCommand = "Select * From Mitarbeiter"

        try:
            DbCursor.execute(SqlCommand)
            DbCon.commit()
        except Exception as ex:
            print(ex)
            return False
        
        for DataSet in DbCursor:
            print(f"{DataSet[0]} {DataSet[1]} {DataSet[2]} {DataSet[3]}")
    except Exception as ex:
        print(ex)
    finally:
        return True

connectionstring :str= "Programieren\\Python\\LF5\\PythonSql\\mitarbeiterverwaltung.db"
ShowTable(connectionstring)