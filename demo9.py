def abc():
    for i in  range(10):
        print("function ",i);
abc();

class Demo:
    def __init__(self,uid,name,age):
        for i in range(10):
            print("constructor : ",uid,name,age);

    def display(self,salary,design):
         for i in range(10):
             print("Method : ",i,salary,design);


d=Demo(100,"Dileep",25);
d.display(50000,'clerk');
