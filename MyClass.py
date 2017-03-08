""" A sample module"""
class MyClass:
    """ A sample class"""

    def __init__(self):
        self.name = ""

    def getName(self):
        """ A sample function"""
        return self.name

    def setName(self, name):
        self.name = name

a = MyClass()
a.setName("Tanaka")

print(a.getName())

print (MyClass.__doc__)
print (MyClass.getName.__doc__)