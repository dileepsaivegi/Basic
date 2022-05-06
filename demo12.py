class Demo:
    def __init__(self):
        try:
            a=int(input("enter a value: "))
            b=int(input("enter b value: "))
            c=a/b;
            print("result: ",c)
        except:
             print("cant divide with zero")
        finally:
             print("thank you")
d=Demo();
