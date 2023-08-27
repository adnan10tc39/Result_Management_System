from tkinter import *
from tkinter import ttk,messagebox
import time
import datetime
import create_db
class Student:
    def __init__(self,root):
        self.root = root
        self.root.title('Students Result Management System')
        self.root.geometry('1350x750+0+0')
        self.root.config(bg='cadet blue')

        #===================================================variables================================================
        self.StdID = StringVar()
        self.Firstname = StringVar()
        self.Surname = StringVar()
        self.Maths = StringVar()
        self.English = StringVar()
        self.Biology = StringVar()
        self.Computing=StringVar()
        self.Chemistry = StringVar()
        self.Physics = StringVar()
        self.AddMaths = StringVar()
        self.Business = StringVar()
        self.TotalScore = StringVar()
        self.Average = StringVar()
        self.Ranking = StringVar()
        self.CourseCode=StringVar()
        self.ExamNo=StringVar()
        self.DateIssued=StringVar()





        #==================================================Frames===================================================
        MainFrame=Frame(self.root,bg="cadet blue")
        MainFrame.grid()

        DataFrame = Frame(MainFrame, bg="cadet blue", bd=2, width=1350, height=400, padx=5, pady=5, relief=RIDGE)
        DataFrame.pack(side=TOP)

        DataFrameLeft = LabelFrame(DataFrame, bg="Ghost White", bd=2, width=900, height=200, padx=10, relief=RIDGE,
                                   font=('arial', 18, 'bold'), text='Student Details')
        DataFrameLeft.pack(side=LEFT)

        DataFrameRight = LabelFrame(DataFrame, bg="powder blue", bd=1, width=450, height=180, padx=10, pady=12,
                                    relief=RIDGE, font=('arial', 18, 'bold'), text='Unit Grades')
        DataFrameRight.pack(side=RIGHT)

        DataFrame2 = Frame(MainFrame,bg="cadet blue",bd=2,width=1350,height=400,padx=5,pady=5,relief=RIDGE)
        DataFrame2.pack(side=BOTTOM)

        ListFrame = Frame(DataFrame2, bg="powder blue", bd=2, width=1350, height=360, padx=5, pady=10, relief=RIDGE)
        ListFrame.pack(side=TOP)

        ButtonFrame = Frame(DataFrame2, bg="powder blue", bd=2, width=1350, height=40, padx=5, pady=10, relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)



        #===============================================widgets in left Frame===============================
        #row=0
        self.lblStdID=Label(DataFrameLeft,font=('arial',14,'bold'),text='Student ID',padx=2,pady=2,bg='ghost white')
        self.lblStdID.grid(row=0,column=0,sticky='w')
        self.txtStdID =Entry(DataFrameLeft, font=('arial', 14, 'bold'),textvariable=self.StdID,bg='ghost white',width=28)
        self.txtStdID.grid(row=0, column=1,pady=7)

        self.lblMaths = Label(DataFrameLeft, font=('arial', 14, 'bold'), text='Maths', padx=2, pady=2, bg='ghost white')
        self.lblMaths.grid(row=0, column=2, sticky='w')
        self.txtMaths = Entry(DataFrameLeft, font=('arial', 14, 'bold'), textvariable=self.Maths, bg='ghost white',width=28)
        self.txtMaths.grid(row=0, column=3,pady=7)

        # row=1
        self.lblCourseCode = Label(DataFrameLeft, font=('arial', 14, 'bold'), text='CourseCode', padx=2, pady=2, bg='ghost white')
        self.lblCourseCode.grid(row=1, column=0, sticky='w')
        self.cboCourseCode = ttk.Combobox(DataFrameLeft, font=('arial', 14, 'bold'),width=26, textvariable=self.CourseCode)
        self.cboCourseCode["values"]=(" ","77101","77102","77103","77104","77105","77106")
        self.cboCourseCode.current(0)
        self.cboCourseCode.grid(row=1, column=1,padx=20,pady=7)

        self.lblComputing = Label(DataFrameLeft, font=('arial', 14, 'bold'), text='Computing', padx=2, pady=2, bg='ghost white')
        self.lblComputing.grid(row=1, column=2, sticky='w')
        self.txtComputing = Entry(DataFrameLeft, font=('arial', 14, 'bold'), textvariable=self.Computing, bg='ghost white',width=28)
        self.txtComputing.grid(row=1, column=3,pady=7)

        # row=2
        self.lblFirstname = Label(DataFrameLeft, font=('arial', 14, 'bold'), text='Firstname', padx=2, pady=2, bg='ghost white')
        self.lblFirstname.grid(row=2, column=0, sticky='w')
        self.txtFirstname = Entry(DataFrameLeft, font=('arial', 14, 'bold'), textvariable=self.Firstname, bg='ghost white',width=28)
        self.txtFirstname.grid(row=2, column=1,pady=7)

        self.lblEnglist = Label(DataFrameLeft, font=('arial', 14, 'bold'), text='English', padx=2, pady=2, bg='ghost white')
        self.lblEnglist.grid(row=2, column=2, sticky='w')
        self.txtEnglish = Entry(DataFrameLeft, font=('arial', 14, 'bold'), textvariable=self.English, bg='ghost white',width=28)
        self.txtEnglish.grid(row=2, column=3,pady=7)

        # row=3
        self.lblSurname = Label(DataFrameLeft, font=('arial', 14, 'bold'),text='Surname',padx=2,pady=2,bg='ghost white')
        self.lblSurname.grid(row=3, column=0, sticky='w')
        self.txtSurname = Entry(DataFrameLeft, font=('arial', 14, 'bold'), textvariable=self.Surname, bg='ghost white',width=28)
        self.txtSurname.grid(row=3, column=1,pady=7)

        self.lblBiology = Label(DataFrameLeft, font=('arial', 14, 'bold'), text='Biology', padx=2, pady=2, bg='ghost white')
        self.lblBiology.grid(row=3, column=2, sticky='w')
        self.txtBiology = Entry(DataFrameLeft, font=('arial', 14, 'bold'), textvariable=self.Biology, bg='ghost white',width=28)
        self.txtBiology.grid(row=3, column=3,pady=7)

        # row=4
        self.lblExamNo = Label(DataFrameLeft, font=('arial', 14, 'bold'), text='ExamNo', padx=2, pady=2, bg='ghost white')
        self.lblExamNo.grid(row=4, column=0, sticky='w')
        self.txtExamNo = Entry(DataFrameLeft, font=('arial', 14, 'bold'), textvariable=self.ExamNo, bg='ghost white',width=28)
        self.txtExamNo.grid(row=4, column=1,pady=7)

        self.lblChemistry = Label(DataFrameLeft, font=('arial', 14, 'bold'), text='Chemistry', padx=2, pady=2, bg='ghost white')
        self.lblChemistry.grid(row=4, column=2, sticky='w')
        self.txtChemistry = Entry(DataFrameLeft, font=('arial', 14, 'bold'), textvariable=self.Chemistry, bg='ghost white',width=28)
        self.txtChemistry.grid(row=4, column=3,pady=7)

        # row=5
        self.lblTotalScore = Label(DataFrameLeft, font=('arial', 14, 'bold'), text='TotalScore', padx=2, pady=2,bg='ghost white')
        self.lblTotalScore.grid(row=5, column=0, sticky='w')
        self.txtTotalScore = Entry(DataFrameLeft, font=('arial', 14, 'bold'), textvariable=self.TotalScore, bg='ghost white',width=28)
        self.txtTotalScore.grid(row=5, column=1,pady=7)

        self.lblPhysics = Label(DataFrameLeft, font=('arial', 14, 'bold'), text='Physics', padx=2, pady=2,bg='ghost white')
        self.lblPhysics.grid(row=5, column=2, sticky='w')
        self.txtPhysics = Entry(DataFrameLeft, font=('arial', 14, 'bold'), textvariable=self.Physics, bg='ghost white',width=28)
        self.txtPhysics.grid(row=5, column=3,pady=7)

        # row=6
        self.lblAverage = Label(DataFrameLeft, font=('arial', 14, 'bold'), text='Average', padx=2, pady=2,bg='ghost white')
        self.lblAverage.grid(row=6, column=0, sticky='w')
        self.txtAverage = Entry(DataFrameLeft, font=('arial', 14, 'bold'), textvariable=self.Average, bg='ghost white',width=28)
        self.txtAverage.grid(row=6, column=1,pady=7)

        self.lblAddMaths = Label(DataFrameLeft, font=('arial', 14, 'bold'), text='AddMaths', padx=2, pady=2, bg='ghost white')
        self.lblAddMaths.grid(row=6, column=2, sticky='w')
        self.txtAddMaths = Entry(DataFrameLeft, font=('arial', 14, 'bold'), textvariable=self.AddMaths, bg='ghost white',width=28)
        self.txtAddMaths.grid(row=6, column=3,pady=7)

        # row=7
        self.lblRanking = Label(DataFrameLeft, font=('arial', 14, 'bold'), text='Ranking', padx=2, pady=2, bg='ghost white')
        self.lblRanking.grid(row=7, column=0, sticky='w')
        self.txtRanking = Entry(DataFrameLeft, font=('arial', 14, 'bold'), textvariable=self.Ranking, bg='ghost white',width=28)
        self.txtRanking.grid(row=7, column=1,pady=7)

        self.lblBusiness = Label(DataFrameLeft, font=('arial', 14, 'bold'), text='Business', padx=2, pady=2,bg='ghost white')
        self.lblBusiness.grid(row=7, column=2, sticky='w')
        self.txtBusiness = Entry(DataFrameLeft, font=('arial', 14, 'bold'), textvariable=self.Business, bg='ghost white',width=28)
        self.txtBusiness.grid(row=7, column=3,pady=7)

        #==========================right Frame Unit Grade===================================================
        self.txtUnitGrade=Text(DataFrameRight,height=16,width=50,bd=2,font=('arail',11,'bold'))
        self.txtUnitGrade.grid(row=0,column=0,pady=2)

        #=========================== list in botton frame==================================================

        scrollBar=Scrollbar(ListFrame)
        scrollBar.grid(row=0,column=1,sticky='ns')
        self.studentList=Listbox(ListFrame,height=11,width=141,font=('arail',12,'bold'),yscrollcommand=scrollBar.set)
        self.studentList.grid(row=0,column=0,padx=19)
        self.studentList.bind("<<ListboxSelect>>", self.StudentRec)
        scrollBar.config(command=self.studentList.xview)

        #===============================button   Frame====================================================
        self.btnAddData=Button(ButtonFrame,text='Add New',height=1,width=16,font=('arail',12,'bold'),bd=2,padx=10,command=self.AddData)
        self.btnAddData.grid(row=0,column=0)

        self.btnDisplayData = Button(ButtonFrame, text='Display', height=1, width=16, font=('arail', 12, 'bold'), bd=2,
                                 padx=12,command=self.DisplayData)
        self.btnDisplayData.grid(row=0, column=1)

        self.btnClearData = Button(ButtonFrame, text='Clear', height=1, width=16, font=('arail', 12, 'bold'), bd=2,
                                 padx=12,command=self.Clear)
        self.btnClearData.grid(row=0, column=2)

        self.btnDeleteData = Button(ButtonFrame, text='Delete', height=1, width=16, font=('arail', 12, 'bold'), bd=2,
                                 padx=8,command=self.deleted)
        self.btnDeleteData.grid(row=0, column=3)

        self.btnSearchData = Button(ButtonFrame, text='Search', height=1, width=16, font=('arail', 12, 'bold'), bd=2,
                                 padx=12,command=self.Search)
        self.btnSearchData.grid(row=0, column=4)

        self.btnUpdateData = Button(ButtonFrame, text='Update', height=1, width=16, font=('arail', 12, 'bold'), bd=2,
                                 padx=12,command=self.Update)
        self.btnUpdateData.grid(row=0, column=5)

        self.btnExitData = Button(ButtonFrame, text='Exit', height=1, width=16, font=('arail', 12, 'bold'), bd=2,
                                 padx=10,command=self.qExit)
        self.btnExitData.grid(row=0, column=6)

     # ========================Functions that not connect data base without using self======================
    def qExit(self):
        qexit = messagebox.askyesno('Quite System','Do You Want Quit?')
        if qexit >0:
            self.root.destroy()
            return
    def Clear(self):
        self.StdID.set("")
        self.Firstname.set("")
        self.Surname.set("")
        self.Maths.set("")
        self.English.set("")
        self.Biology.set("")
        self.Computing.set("")
        self.Chemistry.set("")
        self.Physics.set("")
        self.AddMaths.set("")
        self.Business.set("")
        self.TotalScore.set("")
        self.Average.set("")
        self.Ranking.set("")
        self.CourseCode.set("")
        self.ExamNo.set("")
        self.txtUnitGrade.delete('1.0',END)
        self.studentList.delete('0',END)

    def AddData(self):

        Unit1 = float(self.Maths.get())
        Unit2 = float(self.Computing.get())
        Unit3 = float(self.English.get())
        Unit4 = float(self.Biology.get())
        Unit5 = float(self.Chemistry.get())
        Unit6 = float(self.Physics.get())
        Unit7 = float(self.AddMaths.get())
        Unit8 = float(self.Business.get())

        self.AverageMarks=(Unit1+Unit2+Unit3+Unit4+Unit5+Unit6+Unit7+Unit8)/8
        TotalMarks=Unit1+Unit2+Unit3+Unit4+Unit5+Unit6+Unit7+Unit8
        self.Average.set(int(self.AverageMarks))
        self.TotalScore.set(int(TotalMarks))

        if TotalMarks >=700:
            self.Ranking.set('1St Class')
        elif TotalMarks >=600:
            self.Ranking.set('2.i Upper')
        elif TotalMarks >=500:
            self.Ranking.set('2.ii Lower')
        elif TotalMarks >=400:
            self.Ranking.set('3rd Class')
        elif TotalMarks >=399:
            self.Ranking.set('CoHE')
        elif TotalMarks <=200:
            self.Ranking.set('Fail')

        # self.DateIssued.set(time.strftime("%d/%m/%Y"))
        # self.txtUnitGrade.insert(END,'===================Transcript================='+"\n")
        # self.txtUnitGrade.insert(END, 'Student ID:\t\t'+ self.StdID.get()+'\t\t'+self.DateIssued.get() + "\n")
        # self.txtUnitGrade.insert(END, '============================================' + "\n")
        # self.txtUnitGrade.insert(END, 'Firstname: \t\t\t\t'+self.Firstname.get()+ "\n")
        # self.txtUnitGrade.insert(END, 'Surname: \t\t\t\t' + self.Surname.get() + "\n")
        # self.txtUnitGrade.insert(END, 'Course Code: \t\t\t\t' + self.CourseCode.get() + "\n")
        # self.txtUnitGrade.insert(END, 'Maths: \t\t\t\t' + self.Maths.get() + "\n")
        # self.txtUnitGrade.insert(END, 'English: \t\t\t\t' + self.English.get() + "\n")
        # self.txtUnitGrade.insert(END, 'Biology: \t\t\t\t' + self.Biology.get() + "\n")
        # self.txtUnitGrade.insert(END, 'Computing: \t\t\t\t' + self.Computing.get() + "\n")
        # self.txtUnitGrade.insert(END, 'Chemistry: \t\t\t\t' + self.Chemistry.get() + "\n")
        # self.txtUnitGrade.insert(END, 'Physics: \t\t\t\t' + self.Physics.get() + "\n")
        # self.txtUnitGrade.insert(END, 'Maths: \t\t\t\t' + self.AddMaths.get() + "\n")
        # self.txtUnitGrade.insert(END, 'Business: \t\t\t\t' + self.Business.get() + "\n")
        # self.txtUnitGrade.insert(END, '============================================' + "\n")
        # self.txtUnitGrade.insert(END, 'Total Score: \t\t\t\t' + self.TotalScore.get() + "\n")
        # self.txtUnitGrade.insert(END, 'Average: \t\t\t\t' + self.Average.get() + "\n")
        # self.txtUnitGrade.insert(END, 'Ranking: \t\t\t\t' + self.Ranking.get() + "\n")
        # self.txtUnitGrade.insert(END, '============================================' + "\n")
        self.card()
        self.AddToDataBase()


        # ========================Functions connected with data base without using self======================

    def AddToDataBase(self):
        if (len(self.StdID.get())!=0):
            create_db.AddStdRec(self.StdID.get(),self.CourseCode.get(),self.Firstname.get(),self.Surname.get(),self.ExamNo.get(),self.Maths.get(),self.Computing.get(),self.English.get(),self.Biology.get(),self.Chemistry.get(),self.Physics.get(),self.AddMaths.get(),self.Business.get(),self.TotalScore.get(),self.Average.get(),self.Ranking.get())
            self.studentList.delete('0',END)
            self.studentList.insert(END,(self.StdID.get(),self.CourseCode.get(),self.Firstname.get(),self.Surname.get(),self.ExamNo.get(),self.Maths.get(),self.Computing.get(),self.English.get(),self.Biology.get(),self.Chemistry.get(),self.Physics.get(),self.AddMaths.get(),self.Business.get(),self.TotalScore.get(),self.Average.get(),self.Ranking.get()))
            self.DisplayData()

    def DisplayData(self):
        self.studentList.delete('0',END)
        for row in create_db.ShowData():
            self.studentList.insert(END,row,str(""))

    def StudentRec(self,event):
        searchStd=self.studentList.curselection()[0]
        sd=self.studentList.get(searchStd)
        self.sdid=sd[0]
        self.txtStdID.delete(0,END)
        self.txtStdID.insert(END,sd[1])
        self.cboCourseCode.delete(0, END)
        self.cboCourseCode.insert(END, sd[2])
        self.txtFirstname.delete(0, END)
        self.txtFirstname.insert(END, sd[3])
        self.txtSurname.delete(0, END)
        self.txtSurname.insert(END, sd[4])
        self.txtExamNo.delete(0, END)
        self.txtExamNo.insert(END, sd[5])

        self.txtMaths.delete(0, END)
        self.txtMaths.insert(END, sd[6])
        self.txtComputing.delete(0, END)
        self.txtComputing.insert(END, sd[7])
        self.txtEnglish.delete(0, END)
        self.txtEnglish.insert(END, sd[8])
        self.txtBiology.delete(0, END)
        self.txtBiology.insert(END, sd[9])

        self.txtChemistry.delete(0, END)
        self.txtChemistry.insert(END, sd[10])
        self.txtPhysics.delete(0, END)
        self.txtPhysics.insert(END, sd[11])
        self.txtAddMaths.delete(0, END)
        self.txtAddMaths.insert(END, sd[12])
        self.txtBusiness.delete(0, END)
        self.txtBusiness.insert(END, sd[13])
        self.txtTotalScore.delete(0, END)
        self.txtTotalScore.insert(END, sd[14])
        self.txtAverage.delete(0, END)
        self.txtAverage.insert(END, sd[15])
        self.txtRanking.delete(0, END)
        self.txtRanking.insert(END, sd[16])
        self.txtUnitGrade.delete('1.0',END)
        self.card()


    def deleted(self):
        if (len(self.StdID.get()) != 0):
            create_db.DeleteData(self.sdid)
            self.Clear()
            self.DisplayData()

    def Search(self):
        self.studentList.delete(0,END)
        for row in create_db.SearchData(self.StdID.get(),self.CourseCode.get(),self.Firstname.get(),self.Surname.get(),self.ExamNo.get(),self.Maths.get(),self.Computing.get(),self.English.get(),self.Biology.get(),self.Chemistry.get(),self.Physics.get(),self.AddMaths.get(),self.Business.get(),self.TotalScore.get(),self.Average.get(),self.Ranking.get()):

            self.studentList.insert(END,row,str(""))

    def Update(self):
        if (len(self.StdID.get()) != 0):
            an=create_db.UpdateData(self.StdID.get(),self.CourseCode.get(),self.Firstname.get(),self.Surname.get(),self.ExamNo.get(),self.Maths.get(),self.Computing.get(),self.English.get(),self.Biology.get(),self.Chemistry.get(),self.Physics.get(),self.AddMaths.get(),self.Business.get(),self.TotalScore.get(),self.Average.get(),self.Ranking.get())
            self.DisplayData()
            self.txtUnitGrade.delete('1.0', END)
            self.card()

    def card(self):
        self.DateIssued.set(time.strftime("%d/%m/%Y"))
        self.txtUnitGrade.insert(END, '===================Transcript=================' + "\n")
        self.txtUnitGrade.insert(END, 'Student ID:\t\t' + self.StdID.get() + '\t\t' + self.DateIssued.get() + "\n")
        self.txtUnitGrade.insert(END, '============================================' + "\n")
        self.txtUnitGrade.insert(END, 'Firstname: \t\t\t\t' + self.Firstname.get() + "\n")
        self.txtUnitGrade.insert(END, 'Surname: \t\t\t\t' + self.Surname.get() + "\n")
        self.txtUnitGrade.insert(END, 'Course Code: \t\t\t\t' + self.CourseCode.get() + "\n")
        self.txtUnitGrade.insert(END, 'Maths: \t\t\t\t' + self.Maths.get() + "\n")
        self.txtUnitGrade.insert(END, 'English: \t\t\t\t' + self.English.get() + "\n")
        self.txtUnitGrade.insert(END, 'Biology: \t\t\t\t' + self.Biology.get() + "\n")
        self.txtUnitGrade.insert(END, 'Computing: \t\t\t\t' + self.Computing.get() + "\n")
        self.txtUnitGrade.insert(END, 'Chemistry: \t\t\t\t' + self.Chemistry.get() + "\n")
        self.txtUnitGrade.insert(END, 'Physics: \t\t\t\t' + self.Physics.get() + "\n")
        self.txtUnitGrade.insert(END, 'Maths: \t\t\t\t' + self.AddMaths.get() + "\n")
        self.txtUnitGrade.insert(END, 'Business: \t\t\t\t' + self.Business.get() + "\n")
        self.txtUnitGrade.insert(END, '============================================' + "\n")
        self.txtUnitGrade.insert(END, 'Total Score: \t\t\t\t' + self.TotalScore.get() + "\n")
        self.txtUnitGrade.insert(END, 'Average: \t\t\t\t' + self.Average.get() + "\n")
        self.txtUnitGrade.insert(END, 'Ranking: \t\t\t\t' + self.Ranking.get() + "\n")
        self.txtUnitGrade.insert(END, '============================================' + "\n")

if __name__ == '__main__':
    root=Tk()
    application=Student(root)
    root.mainloop()
