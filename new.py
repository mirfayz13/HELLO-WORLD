


from collections  import namedtuple

#1
Person = namedtuple('Person',['name','surname','age','height','nationality','address','email'])
person1 = Person('John','Joshua',23,178,'uzbek','izzat street','mirfayzmad@gmail.com')
print(person1)

#2
Car = namedtuple('Car',['company','model','year','size','weight','colour','country'])
car1 = Car('Bmw','M5',2024,200,560,'black','Germany')
print(car1)

#3
Student = namedtuple('Student',['name','surname','age','id','email','address','field','course'])
student1 = Student('Mirfayz','Zaripov',19,15973,'mirfayzmad@gmail.com','izzat 58/7','finance',3)
print(student1)

#4
Phone = namedtuple('Phone',['brand','model','year','colour','camera','storage','height'])
phone1 = Phone('iphone',12,2021,'black','hp',64,13)
print(phone1)

#5
Book = namedtuple('Book',['title','author','published_date','pages','sold_products'])
book1 = Book('Python for Data Analysis','Mck',2002,560,2000000)
print(book1)