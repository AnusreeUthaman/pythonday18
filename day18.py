#oops

#class
#it is a blueprint of a object
#name start with capital letter eg:Sample
#donot use underscore to name class eg:SampleMethod
#self-parameter in class

#objects
#are created based on properties and attributes/methods
#member of class

#creating class

class Sample:
    x=10
S1=Sample()
S2=Sample()
print(S1.x)
print(S2.x)

class Sample:
    x=10
    
    def func(self):#function inside class is called method
       print("hello")
S1=Sample()#variable can access by an object(creating object)  
S2=Sample()
S1.func()
S1.func()



class SampleMethod2:
    x=10
    
    def func(self):
       x="hi"
       print("value of x is",x)#to access global variable inside methods
a =SampleMethod2()
a.func()



#Modifying object attribute

class SampleMethod3:
    x=10
    
    def func(self):
        x="hi"
        print("value of x is",x)
s1=SampleMethod3()       
s1.x="python"#updated variable value outside method
#s1=SampleMethod3()
print(s1.x)#accessing object attribute    
s1.func()



#accessing parameter to method
class Student:
    def details(self,name,age):
        self.n =name
        self.a =age
s1=Student()
s2=Student()
s1.details("john",21)
s2.details("james",20)
print(s1.n)
print(s1.a)
print(s2.n)
print(s2.a)

class Student2:
    def details(self,name,age):
        self.n =name
        self.a =age
    def display(self):
        print("name is",self.n)
        print("age is",self.a)
s1=Student2()
s1.details("john",35)
s1.display()

class SampleMethod3:
    x=10
    
    def func(self):
        x="hi"
        print("value of x is",x)
s1=SampleMethod3()       
s1.x="python"#updated variable value outside method
print(s1.x)#accessing object attribute    
s1.func()
