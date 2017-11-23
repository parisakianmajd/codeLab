#Python class properties
# The Pythonic way is to define attributes public

# "@property" decorates the getter function
# "@x.setter" decorates the setter
class P(object):
    def __init__(self,x):
        self.x = x

    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x

    @x.deleter
    def x(self):
        del self.__x


# Javaesque way 
class P2:

    def __init__(self,x):
        self.set_x(x)

    def get_x(self):
        return self.__x

    def set_x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x
p1 = P(1001)
print p1.x
p1.x = -12
print p1.x

p1 = P2(1001)
print p1.get_x()
p1.set_x(-12)
print p1.get_x()



# more about property
###
class Person(): 
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
 
    @property
    def full_name(self):
        return "%s %s" % (self.first_name, self.last_name)


person = Person('John', 'Doe')
print person.full_name
