#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Apple:
  pass
class Apple:
 color = ""
 flavor = ""
jonagold = Apple()
jonagold.color = "red"
jonagold.flavor = "sweet"
print(jonagold.color)
print(jonagold.flavor)


# In[4]:


print(jonagold.color.upper())


# In[8]:


golden = Apple()
golden.color = "yellow"
golden.flavor = "soft"
print(golden.color)
print(golden.flavor)


# In[12]:


class Flower:
    color = 'unknown'
rose = Flower()
rose.color = "red"
violet = Flower()
violet.color = "blue"
this_pun_is_for_you = "Rimla"
print("Roses are {},".format(rose.color))
print("violets are {}".format(violet.color))
print(this_pun_is_for_you)


# In[14]:


class Cat:
    def speak(self):
        print("meow meow meow....")
myCat = Cat()
myCat.speak()


# In[18]:


myLuna = Cat()
myLuna.name = "Luna"
myLuna.speak()


# In[20]:


class Cat:
    name = ""
    def speak(self):
        print("Meow! i'm {}! Meow".format(self.name))
myLuna = Cat()
myLuna.name = "Luna"
myLuna.speak()
myBella = Cat()
myBella.name = "Bella"
myBella.speak()


# In[24]:


class Cat:
    year = 0
    def age (self):
        return self.years * 12
myLuna = Cat()
myLuna.years = 2
myLuna.age()


# In[27]:


class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
jonagold = Apple("red", "sweet")
print(jonagold.color)


# In[33]:


class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
    def __str__(self):
        return "This Apple is {} and its flavor is {}".format(self.color, self.flavor)

jonagold = Apple("red", "sweet")
print(jonagold)


# In[32]:


jonagold = Apple("red", "sweet")
print(jonagold)


# In[39]:


class Person:
    def __init__(self, name):
        self.name = name
    def greeting(self):
        print("Hello! My name is {name}.".format(name=self.name))
help(Person)


# In[40]:


class Clothing:
    material = ""
    def __init__(self,name):
        self.name = name
    def checkmaterial(self):
        print("This {} is made of {}".format(self.name,self.material))
class Shirt (Clothing):
    material="Cotton"
polo = Shirt("Polo")
polo.checkmaterial()


# In[41]:


class Repository:
    def __init__(self):
        self.packages = {}
    def add_package(self, package):
        self.packages[package.name] = package
    def total_size(self):
        result = 0
        for package in self.packages.values():
            result += package.size
        return result
    


# In[ ]:




