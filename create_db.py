import sqlite3

def StudentResult():
    con=sqlite3.connect(database='StudentRecords.db')
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS StudentRecord(id INTEGER PRIMARY KEY,stid text,coursecode text,firstname text,surname text,examno text, maths text,computing text,english text,biology text,chemistry text,physics text, addmaths text, business text,totalscore text,average text,ranking text)")
    con.commit()
    con.close()
StudentResult()

def AddStdRec(StdID ,CourseCode,Firstname,Surname,ExamNo,Maths,Computing,English,Biology,chemistry,Physics,AddMaths,Business,TotalScore,Average,Ranking):
    con = sqlite3.connect(database='StudentRecords.db')
    cur = con.cursor()
    cur.execute("INSERT INTO StudentRecord VALUES(null,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(StdID ,CourseCode,Firstname,Surname,ExamNo,Maths,Computing,English,Biology,chemistry,Physics,AddMaths,Business,TotalScore,Average,Ranking))
    con.commit()
    con.close()

def ShowData():
    con = sqlite3.connect(database='StudentRecords.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM StudentRecord")
    rows=cur.fetchall()
    con.commit()
    con.close()
    return rows

def DeleteData(id):

    con = sqlite3.connect(database='StudentRecords.db')
    cur = con.cursor()
    cur.execute("DELETE FROM StudentRecord WHERE id=?",(id,))
    con.commit()
    con.close()



def SearchData(StdID ="",CourseCode="",Firstname="",Surname="",ExamNo="",Maths="",Computing="",English="",Biology="",chemistry="",Physics="",AddMaths="",Business="",TotalScore="",Average="",Ranking=""):
    con = sqlite3.connect(database='StudentRecords.db')
    cur = con.cursor()
    cur = con.execute(" SELECT * FROM StudentRecord WHERE stid =? OR coursecode=? OR firstname=? OR surname=? OR examno=? OR maths=? OR computing=? OR english=? OR biology=? OR chemistry=? OR physics=? OR addmaths=? OR business=? OR totalscore=? OR average=? OR ranking=? ",(StdID,CourseCode,Firstname, Surname,ExamNo, Maths,Computing, English, Biology, chemistry, Physics, AddMaths, Business, TotalScore, Average, Ranking))
    rows=cur.fetchall()
    con.close()
    return rows


def UpdateData(StdID="", CourseCode="", Firstname="", Surname="", ExamNo="", Maths="", Computing="", English="",Biology="", chemistry="", Physics="", AddMaths="", Business="", TotalScore="", Average="", Ranking=""):
    con = sqlite3.connect(database='StudentRecords.db')
    cur = con.cursor()
    cur = con.execute("UPDATE StudentRecord SET coursecode=?,firstname=?,surname=?,examno=?,maths=?,computing=?,english=?,biology=?,chemistry=?,physics=?,addmaths=?,business=?,totalScore=?,average=?,ranking=? WHERE stid=?",(CourseCode, Firstname, Surname, ExamNo, Maths, Computing, English, Biology, chemistry, Physics, AddMaths,Business, TotalScore, Average, Ranking,StdID))
    con.commit()

