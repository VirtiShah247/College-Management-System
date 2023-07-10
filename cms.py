import os

# Login
class Login:
  def __init__(self):
    self.uname=input("Enter username: ")
    self.pwd=input("Enter password: ")
    # self.person=input("Enter type of user faculty or student or admin? ")

# Sign In
class Sign:
  def __init__(self):
    self.uname=input("Enter username: ")
    self.pwd=input("Enter password: ")
    self.person=input("Enter type of user faculty or student or admin? ")
  def check(self):
    SpecialSym =['$', '@', '#', '%']
    val = True
     
    if len(self.pwd) < 6:
      print('length should be at least 6')
      val = False
         
    if len(self.pwd) > 12:
      print('length should be not be greater than 12')
      val = False
         
    if not any(char.isdigit() for char in self.pwd):
      print('Password should have at least one numeral')
      val = False
         
    if not any(char.isupper() for char in self.pwd):
      print('Password should have at least one uppercase letter')
      val = False
         
    if not any(char.islower() for char in self.pwd):
      print('Password should have at least one lowercase letter')
      val = False
         
    if not any(char in SpecialSym for char in self.pwd):
      print('Password should have at least one of the symbols $@#')
      val = False
    # print(val)
    return val

# Person Super Class
class Person:
  def __init__(self,user,opt):
    self.opt=opt
    val=True
    while(val==True):
      ch=int(input('''
    Enter 1 to add a person's details
    Enter 2 to update a person's details
    Enter 3 to search a person's details
    Enter 4 to delete a person
    Enter 5 to display a person's details
    Enter 6 to exit
    ''' ))
      if(ch==1):
        self.add()
      elif(ch==2):
        self.update()
      elif(ch==3):
        self.search()
      elif(ch==4):
        self.delete()
      elif (ch==5):
        self.display()
      else:
        val=False
 
#  Add details
  def add(self):
    self.id=int(input("Enter id: "))
    self.name=input("Enter Full name: ")
    self.email=input("Enter email id: ")
    self.phone=int(input("Enter mobile no: "))
    self.age=int(input("Enter age: "))
    if((user=='admin' and self.opt==3) or (user=='faculty' and self.opt==2)):
      # self.course=[]
      # self.stud_course[self.id]=[int(item) for item in input("Enter the course id's under this student : ").split()]
      
      self.stud_course={}
      self.stud_course[self.id]=input("Enter the course id's under this student : ")
    if(user=="admin"):
      if(self.opt==1):
        f=open("admin.txt","a+")
      elif(self.opt==2):
        f=open("faculty.txt","a+")
      elif(self.opt==3):
        f=open("student.txt","a+")
        fsc=open("stud_course.txt","a+")
        fsc.write(str(self.id)+":"+str(self.stud_course[self.id])+"\n")
        fsc.close()
    elif(user=="faculty"):
      if(self.opt==1):
        f=open("faculty.txt","a+")
      elif(self.opt==2):
        f=open("student.txt","a+")
        fsc=open("stud_course.txt","a+")
        fsc.write(str(self.id)+":"+str(self.stud_course[self.id])+"\n")
        fsc.close()
    elif(user=="student"):
      f=open("student.txt","a+")
    f.write(str(self.id)+" "+self.name+" "+self.email+" "+str(self.phone)+" "+str(self.age)+"\n")
    # fsc.write(str(self.id)+":"+str(self.stud_course[self.id])+"\n")
    f.seek(0)
    print(f.read())
    f.close()
    # fsc.close()
  # Update details
  def update(self):
    if(user=="admin"):
      if(self.opt==1):
        id=int(input("Enter ur id: "))
        f=open("admin.txt","r")
        data=f.readlines()
        f=open("admin.txt","w")
      elif(self.opt==2):
        id=int(input("Enter faculty id: "))
        f=open("faculty.txt","r")
        data=f.readlines()
        f=open("faculty.txt","w")
      elif(self.opt==3):
        id=int(input("Enter student id: "))
        f=open("student.txt","r")
        data=f.readlines()
        f=open("student.txt","w")
        # fsc=open("stud_course.txt","r")
    elif(user=="faculty"):
      if(self.opt==1):
        id=int(input("Enter faculty id: "))
        f=open("faculty.txt","r")
        data=f.readlines()
        f=open("faculty.txt","w")
      elif(self.opt==2):
        id=int(input("Enter student id: "))
        f=open("student.txt","r")
        data=f.readlines()
        f=open("student.txt","w")

        # fsc=open("stud_course.txt","r")
    elif(user=="student"):
      id=int(input("Enter student id: "))
      f=open("student.txt","r")
      data=f.readlines()
      f=open("student.txt","w")

    u=input("Enter what u want to update? ")
    u=u.lower()

    # f1=open("temp.txt","w")

    dict={}
    flag=0
    for line in data:
      l = line.strip().split()
      # dict[l[0]] = [l[1],l[2],l[3],l[4]]
      if(int(l[0])==id):
        flag=1
        if(u=='name'):
          self.name=input("Enter new Full name: ")
          # dict[id]=[self.name,l[2],l[3],l[4]]
          f.write(l[0]+" "+self.name+" "+l[2]+" "+l[3]+" "+l[4]+"\n")
        elif(u=='email'):
          self.email=input("Enter new email id: ")
          # dict[id]=[l[1],self.email,l[3],l[4]]
          f.write(l[0]+" "+l[1]+" "+self.email+" "+l[3]+" "+l[4]+"\n")
        elif(u=='phone'):
          self.phone=input("Enter new mobile no: ")
          # dict[id]=[l[1],l[2],self.phone,l[4]]
          f.write(l[0]+" "+l[1]+" "+l[2]+" "+(self.phone)+" "+l[4]+"\n")
        elif(u=='age'):
          self.age=input("Enter new age: ")
          # dict[id]=[l[1],l[2],l[3],self.age]
          f.write(l[0]+" "+l[1]+" "+l[2]+" "+l[3]+" "+(self.age)+"\n")
        else:
          f.write(l[0]+" "+l[1]+" "+l[2]+" "+l[3]+" "+l[4]+"\n")
      else:
        f.write(l[0]+" "+l[1]+" "+l[2]+" "+l[3]+" "+l[4]+"\n")
    # f.seek(0)
    # print(f.read())
    f.close()
    # f1.close()
    if(u=='course' and ((user=='admin' and self.opt==3) or (user=='faculty' and self.opt==2))):
      fsc=open("stud_course.txt","r")
      # ftc=open("temp_course.txt","w")
      fsc.seek(0)
      data=fsc.readlines()
      fsc=open("stud_course.txt","w")
      dict={}
      flag=0
      for line in data:
        l = line.strip().split(":")
        if(int(l[0])==id):
          flag=1
          # list=l[1].strip().split()
          # print(list,type(list))
          # self.stud_course={}
          # self.stud_course[id]=list.append([int(item) for item in input("Enter new course id's under this student : ").split()])
          # list.extend([int(item) for item in input("Enter new course id's under this student : ").split()])
          # print(list)
          new=input("Enter new course id's under this student : ")
          l[1]=l[1].split(" ")
          new=new.split(" ")
          # print(l[1],type(l[1]))
          # print(new,type(new))
          # print(set(l[1]+(new)))
          new_str=" ".join(set(l[1]+new))
          fsc.write(l[0]+":"+new_str+"\n")
        else:
          fsc.write(l[0]+":"+l[1]+"\n")
      # f.seek(0)
      # print(f.read())
      fsc.close()
      fsc.close()

    if(flag==0):
        print("There is no such user with entered id!!")

  
  # Search details
  def search(self):
    
    try:
      if(user=="admin"):
        if(self.opt==2):
          id=int(input("Enter faculty id: "))
          f=open("faculty.txt","r")
        elif(self.opt==3):
          id=int(input("Enter student id: "))
          f=open("student.txt","r")
      elif(user=="faculty"):

        if(self.opt==2):
          id=int(input("Enter student id: "))
          f=open("student.txt","r")

      data=f.readlines()
      flag=0
      for line in data:
        l = line.strip().split()
        # dict[l[0]] = [l[1],l[2],l[3],l[4]]
        if(int(l[0])==id):
          print("Id= ",l[0])
          print("Name= ",l[1])
          print("Email= ",l[2])
          print("Mobile No: ",l[3])
          print("Age= ",l[4])
          flag=1
          break
      f.close()
      if(flag==0):
        print("There is no such user with entered id!!")
    except:
      print("U can't access this method!!")
  
  # Delete details
  def delete(self):
    try:
      if(user=="admin"):
        if(self.opt==2):
          id=int(input("Enter faculty id: "))
          f=open("faculty.txt","r")
        elif(self.opt==3):
          id=int(input("Enter student id: "))
          f=open("student.txt","r")
          # fsc=open("stud_course.txt","r")
      elif(user=="faculty"):
        if self.opt==2:
          id=int(input("Enter student id: "))
          f=open("student.txt","r")
        # fsc=open("stud_course.txt","r")
      if(user=='admin' and self.opt==2):
        choice=1
      elif((user=='admin' and self.opt==3) or (user=='faculty' and self.opt==2)):
        choice=int(input('''
        Enter 1 to delete person's details
        Enter 2 to delete course from student
        '''))

      if(choice==1):
        f1=open("temp.txt","w")
        data=f.readlines()

        # print(data)
        flag=0
        for line in range(len(data)):
          l = data[line].strip().split()
          # dict[l[0]] = [l[1],l[2],l[3],l[4]]
          if(int(l[0])!=id):
            f1.write(l[0]+" "+l[1]+" "+l[2]+" "+l[3]+" "+l[4]+"\n")
          else:
            flag=1
        f.close()
        f1.close()
        if(flag==0):
          print("There is no such user with entered id!!")
        if((user=='admin' and self.opt==2)):
          os.remove("faculty.txt")
          os.rename("temp.txt","faculty.txt")
        elif((user=='admin' and self.opt==3) or (user=='faculty' and self.opt==2)):
          os.remove("student.txt")
          os.rename("temp.txt","student.txt")
      if(choice==2):
        fsc=open("stud_course.txt","r")
        f1=open("temp_course.txt","w")
        fsc.seek(0)
        data=fsc.readlines()
        dict={}
        flag=0
        for line in data:
          l = line.strip().split(":")
          if(int(l[0])==id):
            flag=1

            new=input("Enter course id to delete : ")
            # new_str = ''.join(letter for letter in l[1] if letter!=new)
            length=l[1].find(new)
            new_str=l[1][0:length]+l[1][length+2:]
            f1.write(l[0]+":"+new_str+"\n")
          else:
            f1.write(l[0]+":"+l[1]+"\n")
        # f.seek(0)
        # print(f.read())
        if(flag==0):
          print("There is no user with enter id")
        fsc.close()
        f1.close()
        os.remove("stud_course.txt")
        os.rename("temp_course.txt","stud_course.txt")
    except:
      print("U can't access this method!!")
  
  # Display details
  def display(self):
    
    if(user=="admin"):

      if(self.opt==1):
        id=int(input("Enter ur id: "))
        f=open("admin.txt","r")
      elif(self.opt==2):
        # id=int(input("Enter faculty id: "))
        f=open("faculty.txt","r")
      elif(self.opt==3):
        # id=int(input("Enter student id: "))
        f=open("student.txt","r")
        # fsc=open("stud_course.txt","r")
    elif(user=="faculty"):
      
      if(self.opt==1):
        id=int(input("Enter ur id: "))
        f=open("faculty.txt","r")
      elif(self.opt==2):
        # id=int(input("Enter student id: "))
        f=open("student.txt","r")
        # fsc=open("stud_course.txt","r")
    elif(user=="student"):
      id=int(input("Enter ur id: "))
      f=open("student.txt","r")
      # fsc=open("stud_course.txt","r")
    data=f.readlines()

    # data1=fsc.readlines()
    flag=0
    for index in range(len(data)):
      l = data[index].strip().split()
      # dict[l[0]] = [l[1],l[2],l[3],l[4]]
      if(self.opt==1 or user=='student'):
        fsc=open("stud_course.txt","r")
        data1=fsc.readlines()

        if(id==int(l[0])):
          print("Id= ",l[0])
          print('Name= ',l[1])
          print('Email= ',l[2])
          print('Mobile no= ',l[3])
          print('Age= ',l[4])
          for i in data1:
            l=i.strip().split(":")
            if(id==int(l[0])):
              print("courses= ",end="")
              list=l[1].strip().split()
              f2=open("course.txt","r")
              data2=f2.readlines()
              for j in data2:
                l1=j.strip().split()
                if(l1[0] in list):
                  print(l1[1],end=" ")
          print() 
          flag=1
          fsc.close()

      else:
        print("Id= ",l[0])
        print('Name= ',l[1])
        print('Email= ',l[2])
        print('Mobile no= ',l[3])
        print('Age= ',l[4])
        if((user=='admin' and self.opt==3) or (user=='faculty' and self.opt==2)):
          fsc=open("stud_course.txt","r")
          data1=fsc.readlines()
          i=data1[index]
          l=i.strip().split(":")
          print("courses= ",end="")
          list=l[1].strip().split()
          f2=open("course.txt","r")
          data2=f2.readlines()
          for j in data2:
            l1=j.strip().split()
            if(l1[0] in list):
              print(l1[1],end=" ")
          f2.close()
        print()
    f.close()
    flag=1
    if(flag==0):
      print("There is no such user with entered id!!")

# Course Super Class
class Course:
  def __init__(self):
    val=True
    while(val==True):
      ch=int(input('''
    Enter 1 to add course details
    Enter 2 to update  course details
    Enter 3 to search course details
    Enter 4 to delete a course 
    Enter 5 to display course details
    Enter 6 to exit
    ''' ))
      if(ch==1):
        self._add_c()
      elif(ch==2):
        self._update_c()
      elif(ch==3):
        self.search_c()
      elif(ch==4):
        self._delete_c()
      elif (ch==5):
        self.display_c()
      else:
        val=False

  # Add Course
  def _add_c(self):
    self.id=int(input("Enter course id: "))
    self.name=input("Enter name of course: ")
    self.duration=int(input("Enter duration of course: "))
    self.faculty=input("Enetr faculty teaching this course: ")
    f=open("course.txt","a+")
    f.write(str(self.id)+" "+self.name+" "+str(self.duration)+" "+self.faculty+"\n")
    f.seek(0)
    print(f.read())
    f.close()
  
  # Update Course
  def _update_c(self):
    id=int(input("Enter id of course: "))
    u=input("Enter what u want to update? ")
    u=u.lower()
    f=open("course.txt","r")
    # f1=open("temp.txt","w")
    data=f.readlines()
    f=open("course.txt","w")
    dict={}
    flag=0
    for line in data:
      l = line.strip().split()
      # dict[l[0]] = [l[1],l[2],l[3],l[4]]
      if(int(l[0])==id):
        flag=1
        if(u=='name'):
          self.name=input("Enter new course name: ")
          # dict[id]=[self.name,l[2],l[3],l[4]]
          f.write(l[0]+" "+self.name+" "+l[2]+" "+l[3]+"\n")
        elif(u=='duration'):
          self.email=input("Enter duration of course: ")
          # dict[id]=[l[1],self.email,l[3],l[4]]
          f.write(l[0]+" "+l[1]+" "+str(self.duration)+" "+l[3]+"\n")
        elif(u=='faculty'):
          self.phone=input("Enter new faculty name: ")
          # dict[id]=[l[1],l[2],self.phone,l[4]]
          f.write(l[0]+" "+l[1]+" "+l[2]+" "+self.faculty+"\n")
      else:
        f.write(l[0]+" "+l[1]+" "+l[2]+" "+l[3]+"\n")
    # f.seek(0)
    # print(f.read())
    f.close()
    if(flag==0):
        print("There is no such course with entered id!!")
  
  # Search Course
  def search_c(self):
    id=int(input("Enter id of course to search= "))
    f=open("course.txt","r")
    data=f.readlines()
    flag=0
    for line in data:
      l = line.strip().split()
      # dict[l[0]] = [l[1],l[2],l[3],l[4]]
      if(int(l[0])==id):
        print("Course id= ",l[0])
        print("Course Name= ",l[1])
        flag=1
        break
    f.close()

    if(flag==0):
        print("There is no such course with entered id!!")
  
  # Delete Course
  def _delete_c(self):
    id=int(input("Enter id of course to delete= "))
    f=open("course.txt","r")
    f1=open("temp.txt","w")
    data=f.readlines()
    # dict={}
    flag=0
    for line in data:
      l = line.strip().split()
      # dict[l[0]] = [l[1],l[2],l[3],l[4]]
      if(int(l[0])!=id):
        f1.write(l[0]+" "+l[1]+" "+l[2]+" "+l[3]+"\n")
      else:
        flag=1
    # f.seek(0)
    # print(f.read())
    f.close()
    f1.close()
    os.remove("course.txt")
    os.rename("temp.txt","course.txt")
    if(flag==0):
      print("There is no such course with entered id!!")
    else:
      F=open("stud_course.txt","r")
      f1=open("temp_course.txt","w")
      F.seek(0)
      data=F.readlines()
      dict={}
      flag=0
      for line in data:
        l = line.strip().split(":")
        if(str(id) in (l[1])):
          flag=1
          # list=l[1].strip().split()
          # print(list,type(list))
          # self.stud_course={}
          # self.stud_course[id]=list.append([int(item) for item in input("Enter new course id's under this student : ").split()])
          # list.extend([int(item) for item in input("Enter new course id's under this student : ").split()])
          # print(list)
          new=str(id)
          # new_str = ''.join(letter for letter in l[1] if letter!=new)
          length=l[1].find(new)
          new_str=l[1][0:length]+l[1][length+2:]
          f1.write(l[0]+":"+new_str+"\n")
        else:
          f1.write(l[0]+":"+l[1]+"\n")
      # f.seek(0)
      # print(f.read())
      F.close()
      f1.close()
      os.remove("stud_course.txt")
      os.rename("temp_course.txt","stud_course.txt")
  
  # Display Course
  def display_c(self):
    f=open("course.txt","r")
    data=f.readlines()
    for line in data:
      l = line.strip().split()
      # dict[l[0]] = [l[1],l[2],l[3],l[4]]
      print("Id= ",l[0])
      print('Name= ',l[1])
      print('duration= ',l[2])
      print('faculty name= ',l[3])
      print()
    f.close()
    # print('Name= ',self.name)
    # print('Duration= ',self.duration)
    # print('Faculty= ',self.faculty)

# Admin sub class
class Admin(Person,Course):
  def __init__(self):
    while(True):
      ch=int(input('''
      Enter 1 to manage his/her details
      Enter 2 to manage faculty details
      Enter 3 to manage student details
      Enter 4 to manage Course details
      Enter 5 to exit
      '''))
      if(ch==1):
        Person.__init__(self,"admin",1)
      elif(ch==2):
        Person.__init__(self,"faculty",2)
      elif(ch==3):
        Person.__init__(self,"student",3)
      elif(ch==4):
        Course.__init__(self)
      else:
        break

# Faculty sub class
class Faculty(Person,Course):
  def __init__(self):
    while(True):
      ch=int(input('''
      Enter 1 to manage his/her details
      Enter 2 to manage student details
      Enter 3 to manage Course details
      Enter 4 to exit

      '''))
      if(ch==1):
        Person.__init__(self,"faculty",1)
      elif(ch==2):
        Person.__init__(self,"student",2)
      elif(ch==3):
        Course.__init__(self)
      else:
        break

# Student sub class
class Student(Person):
  def __init__(self):
    while(True):
      ch=int(input('''
      Enter 1 to manage ur details
      Enter 2 to Search course name
      Enter 3 to display all courses
      Enter 4 to exit

      '''))
      if(ch==1):
        Person.__init__(self,"student",1)
      elif(ch==2):
        Course.search_c(self)
      elif(ch==3):
        Course.display_c(self)
      else:
        break


# l=[]
# s={}
# print("Do u want to login or register?")

# Main Body
ch=int(input('''
Enter 1 to sign up
Enter 2 to login'''))
if (ch==1):
  S=Sign()
  while((S.check()==False)):
    S=Sign()
  # s[S.uname]=S.pwd
  if(S.person=="admin"):
    f=open("admin_sign.txt","a+")
  elif(S.person=="faculty"):
    f=open("faculty_sign.txt","a+")
  elif(S.person=="student"):
    f=open("student_sign.txt","a+")
  file=S.person
  f.write(S.uname+":"+S.pwd+"\n")
  f.seek(0)
  print(f.read())
  f.close()
elif (ch==2):
  user=input('''
  Enter ur role:
  admin
  faculty
  student
  ''')
  if(user=="admin"):
    f=open("admin_sign.txt","a+")
  elif(user=="faculty"):
    f=open("faculty_sign.txt","a+")
  elif(user=="student"):
    f=open("student_sign.txt","a+")
  file=user
  f.seek(0)
  data = f.readlines()
  # print(data)
  f.close()
  s = {}
  for line in data:
    l = line.strip().split(":")
    s[l[0]] = l[1]
  # print(s)
  flag=0
  count=0
  while(count<5):
    L=Login()
    if(L.uname in s  and L.pwd==s[L.uname]):
      print("Succesfully login")
      flag=1
      break
    else:
      print("Incorrect login details!! pls. enter again")
      count+=1
      print("You have ",5-count," more trials to login")
      flag=0

if(count<5):
  if(file=='admin'):
    a=Admin()
  elif(file=='faculty'):
    f=Faculty()
  if(file=='student'):
    s=Student()
else:
  print("Pls. contact admin to login!!")