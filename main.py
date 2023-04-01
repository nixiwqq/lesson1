class Person:
  age = 14
  height = 155
  isFemale = True
  name = 'Nika' # добавили клас персон

  def __init__(self, name, age):
    self.name = name
    self.age = age 

me = Person(Nika, 14)
friend = Person(Vlad, 13)

print(me.age)
friend.name = "Vlad"
print(friend.name)