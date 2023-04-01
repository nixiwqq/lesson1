import time
class Person:
  age = 14
  height = 155
  isFemale = True
  money = 0
  name = 'Nika' # добавили клас персон

  def __init__(self, name, age):
    self.name = name
    self.age = age 
    
  def work(self, days):
    while days != 0:
      time.sleep(1)
      self.money += 2 
      days -= 1

  def rest(self, days):
    while days != 0:
      time.sleep(1)
      self.money -= 1
      days -= 1
      

me = Person('Nika', 14)
friend = Person('Vlad', 13)

print(me.money)
# me.work()



print(me.money)
me.work(3)
print(me.money)
#print(friend.age)
# friend.name = "Vlad"
# print(friend.name)