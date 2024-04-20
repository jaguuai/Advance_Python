# 1- Workbench IDE ile schooldb isminde bir database oluşturup Student tablosunu ekleyiniz.
    # Id,StudentNumber,Name,Surname,Birthdate,Gender

# 2- Database bağlantısını oluşturunuz. 
import mysql.connector
from datetime import datetime
from connection import connection
# # Eğer datetime from yapmazsak asagıda datime.datetime yapmayı unutma
# connection=mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="",
#   database="schooldb"
#  )
class Student:
   connection=connection
   mycursor=connection.cursor()
   def __init__(self,studentNumber,name,surname,birthday,gender):
      self.studentNumber=studentNumber
      self.name=name
      self.surname=surname
      self.birthday=birthday
      self.gender=gender
   def saveStudent(self):
      sql="INSERT INTO Student(StudentNumber,Name,Surname,Birthday,Gender) VALUES(%s,%s,%s,%s,%s)"
      value=(self.studentNumber,self.name,self.surname,self.birthday,self.gender)
      Student.mycursor.execute(sql,value)
      try:
         connection.commit()
         print(f"{Student.mycursor.rowcount} tane kayit eklendi")
      except mysql.connector.Error as err:
         print("hata:",err)
      finally:
          connection.close()
          print("Database connection kapandi")

   @staticmethod
   def saveStudents(students):
       sql="INSERT INTO Student(StudentNumber,Name,Surname,Birthday,Gender) VALUES(%s,%s,%s,%s,%s)"
       values=students
       Student.mycursor.executemany(sql,values)
       try:
         connection.commit()
         print(f"{Student.mycursor.rowcount} tane kayit eklendi")
       except mysql.connector.Error as err:
         print("hata:",err)
       finally:
          connection.close()
          print("Database connection kapandi")
   @staticmethod
   def StudentInfo():
        # sql = "select * from student"
        # sql = "select * from student LIMIT 3"
        # sql = "select studentnumber,name,surname from student"
        # sql = "select name,surname from student where gender='K'"
        # sql = "select * from student where YEAR(birthdate) = 2003"
        # sql = "select * from student where YEAR(birthdate) = 2005 and name = 'Ali'"
        # sql = "select * from student where name like '%an%' or surname like '%an%'"
        # sql = "select COUNT(id) from student where gender='E'"
        # sql = "select name,surname from student where gender='K' order by name,surname"

        Student.mycursor.execute(sql)

        try:
            results = Student.mycursor.fetchall()
            for result in results:
                print(f'{result}')

        except mysql.connector.Error as err:
            print('hata', err)
        finally:
            Student.connection.close()

   @staticmethod
   def getStudentById(id):
        sql = "select * from student where id=%s"
        value = (id,)

        Student.mycursor.execute(sql,value)

        try:
            obj = Student.mycursor.fetchone()
            return Student(obj[0],obj[1],obj[2],obj[3],obj[4],obj[5])
        except mysql.connector.Error as err:
            print('Error', err)  
   @staticmethod
   def getStudentById(id):
        sql = "select * from student where id=%s"
        value = (id,)

        Student.mycursor.execute(sql,value)

        try:
            obj = Student.mycursor.fetchone()
            return Student(obj[0],obj[1],obj[2],obj[3],obj[4],obj[5])
        except mysql.connector.Error as err:
            print('Error', err)        
    
   def updateStudent(self):
        sql = "update student set studentnumber=%s,name=%s,surname=%s,birthdate=%s,gender=%s where id=%s"
        values = (self.studentNumber,self.name,self.surname,self.birthdate,self.gender,self.id)
        Student.mycursor.execute(sql,values)

        try:
            Student.connection.commit()
            print(f'{Student.mycursor.rowcount} tane kayıt güncellendi')
        except mysql.connector.Error as err:
            print('Hata:',err)
    
   @staticmethod
   def updateStudents(liste):
        sql = "update student set studentnumber=%s,name=%s,surname=%s,birthdate=%s,gender=%s where id=%s"
        values = []
        order = [1,2,3,4,5,0]

        for item in liste:
            item = [item[i] for i in order]
            values.append(item)

        Student.mycursor.executemany(sql,values)

        try:
            Student.connection.commit()
            print(f'{Student.mycursor.rowcount} tane kayıt güncellendi')
        except mysql.connector.Error as err:
            print('Hata:',err)

   @staticmethod
   def getStudentsGender(gender):
        sql = "select * from student where gender=%s"
        value = (gender,)

        Student.mycursor.execute(sql,value)

        try:
            return Student.mycursor.fetchall()
        except mysql.connector.Error as err:
            print('Error', err)    
        
      
    
       
      
# ahmet=Student("3465","Eylul","Kanter",datetime(2005, 5, 17),"E")
# ahmet.saveStudent()

# 3- Aşağıdaki bilgiler için insert sorguları oluşturup kayıtları ekleyiniz.

    # ("301","Ahmet","Yılmaz",datetime(2005, 5, 17),"E"),
    # ("302","Ali","Can",datetime(2005, 6, 17),"E"),
    # ("303","Canan","Tan",datetime(2005, 7, 7),"K"),
    # ("304","Ayşe","Taner",datetime(2005, 9, 23),"K"),
    # ("305","Bahadır","Toksöz",datetime(2004, 7, 27),"E"),
    # ("306","Ali","Cenk",datetime(2003, 8, 25),"E")

ogrenciler = [
    ("3", "Ahmet", "Yılmaz", datetime(2005, 5, 17), "E"),
    ("30", "Ali", "Can", datetime(2005, 6, 17), "E"),
    ("33", "Canan", "Tan", datetime(2005, 7, 7), "K"),
    ("34", "Ayşe", "Taner", datetime(2005, 9, 23), "K"),
    ("35", "Bahadır", "Toksöz", datetime(2004, 7, 27), "E"),
    ("36", "Ali", "Cenk", datetime(2003, 8, 25), "E")
]


Student.saveStudents(ogrenciler)


# 4- Aşağıdaki sorguları yazınız.
#   a- Tüm öğrenci kayıtlarını alınız.
#   b- Tüm öğrencilerin sadece öğrenci no, ad ve soyad bilgilerini alınız.
#   c- Sadece kız öğrencilerin ad ve soyadlarını alınız.
#   d- 2003 doğumlu öğrenci bilgilerini alınız. 
#   e- İsmi Ali ve doğum tarihi 2005 olan öğrenci bilgilerini alınız.
#   f- ad veya soyadı içinde 'an' ifadesi geçen kayıtları alınız. 
#   g- Kaç erkek öğrenci vardır ?
#   h- Kız öğrencileri harf sırasına göre getiriniz.


# 5- Aşağıdaki güncelleme sorularını yapınız.
#   a- id' e göre aldığınız bir öğrencinin bilgilerini güncelleyiniz.
#   b- cinsiyet' e göre aldığınız bir öğrencinin bilgilerini güncelleyiniz.
# student = Student.getStudentById(8)

# student.name = 'Çınar'
# student.surname = 'Turan'

# student.updateStudent()


students = Student.getStudentsGender('E')
print(students)

liste = []
for std in students:
    std = list(std)
    std[2] = 'Mr ' + std[2]
    liste.append(std)

Student.updateStudents(liste)