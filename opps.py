#opps allows to write code slightly different and simple
#class is real word object
# how it works in python

# student={"name":"Nitin","grades":(28,98,89,47)}

# def average(sequence):
#     return sum(sequence)/len(sequence)


# print(average(student["grades"]))

##upper program in class aproach

# from typing import TextIO


# class student:
#     def __init__(self):
#         self.name="Nitin" # . notation is allows us to access inside of it
#         self.grades=(90,25,88,79)
    
#     def avg(self):
#         return sum(self.grades)/len(self.grades)

#     def print_name(self):
#         return self.name

# std=student()
# print(std.name)
# print(std.grades)
# # print(student.avg(std))
# # print(student.print_name(std)) # working aspacts of function inside of class
# print(std.avg())
# print(std.print_name()) #simple aproach to follow is more easier than upper one


# ## __str__ and __rpr__ both are use to string representation of an object
# # use only one at a time
# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
    
#     # def __str__(self):
#     #     return f"Name is {self.name} and age is {self.age} years."

#     def __repr__(self):
#         return f"<person('{self.name}', {self.age})>"

# out=person("Lalit", 26)
# print(out) #without __str__ method it will give strinhg qrepresentation as main object


#exercise
class store:
    def __init__(self,name):
        self.name=name
        self.items=[]

    def add_item(self,name,price):
        item={"name":name, "price":price}
        self.item.append(item)
    def stock_price(self):
        # total=0
        # for item in self.items:
        #     total+=item["price"]
        # return total
        return sum([item["price"] for item in self.items])

    def stock_price(self):
        Total=0
        for item in self.items:
            Total+=item['price']
        return Total

    @classmethod
    def franchise(cls,store):
        return cls(store.name + " - franchise")

    @staticmethod
    def store_details(store):
        return '{}, total stock price {}'.format(store.name, int(store.stock_price()))

    
out=store("nitin")
out.stock_price()
print(out)