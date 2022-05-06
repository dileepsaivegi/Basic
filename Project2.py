import sys
class Clerk:
  def __init__(self):
     self.name = input("Enter  Name : ")
     self.age = int(input('Enter  Age : '))
     self.salary=int(input('Enter Salary :'));
     self.designation=input('Enter Designation:');
  def insert(self):
        f=open("Employee.txt",'a');
        '''f.write(self.name);
        f.write(str(self.age));
        f.write(str(self.salary));
        f.write(self.designation);
        f.write("\n");
        f.close()'''
        records= [self.name,str(self.age),str(self.salary),self.designation]
        for line in records:
           f.write(line)
           f.write("\t")
        f.write("\n");
        f.close() 
class Programmer:
  def __init__(self):
     self.name = input("Enter  Name : ")
     self.age = int(input('Enter  Age : '))
     self.salary=int(input('Enter Salary :'));
     self.designation=input('Enter Designation:');
  def insert(self):
        f=open("Employee.txt",'a');
        '''f.write(self.name);
        f.write(str(self.age));
        f.write(str(self.salary));
        f.write(self.designation);
        f.write("\n");
        f.close()'''
        records= [self.name,str(self.age),str(self.salary),self.designation]
        for line in records:
           f.write(line)
           f.write("\t")
        f.write("\n");
        f.close() 
class Manager:
  def __init__(self):
     self.name = input("Enter  Name : ")
     self.age = int(input('Enter  Age : '))
     self.salary=int(input('Enter Salary :'));
     self.designation=input('Enter Designation:');
  def insert(self):
        f=open("Employee.txt",'a');
        '''f.write(self.name);
        f.write(str(self.age));
        f.write(str(self.salary));
        f.write(self.designation);
        f.write("\n");
        f.close()'''
        records= [self.name,str(self.age),str(self.salary),self.designation]
        for line in records:
           f.write(line)
           f.write("\t")
        f.write("\n");
        f.close() 
while True:
  print("1.Create")
  print("2.Display")
  print("3.Raise Salary")
  print("4.Exit\n")
  choose = 0
  choice=0;
  while (choose < 1) or (choose > 4):
    choice = int(input("Enter your choice choic 1 \n"))
    break
  if choice==1:
        while True:
           
            print("............................")
            print("1.Clerk")
            print("2.Programmer")
            print("3.Manager")
            print("4.Exit\n")
            while (choose < 1) or (choose > 4):
                  choose = int(input("Enter your choice\n"))
                  if choose == 1:
                      c = Clerk();
                      c.insert();
                      break;
                  elif choose == 2:
                      p = Programmer();
                      c.insert();
                      break;
                  elif choose == 3:
                      m = Manager();
                      c.insert();
                      break;
                  elif choose == 4:
                      print("Thank you")
            break;
  if choice== 2:
                print(" You Enterd 2 ")
                f = open("Employee.txt", "r")
                for x in f:
                    print(x);
                f.close()
  if choice== 3:
                print(" You Enterd 3 ")
                print(" This is for to raise salary  ")

  if choice == 4:
      print("Thank you Using this application ")
      sys.exit();
