class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    print("Hello, my name is " + self.name)

class SpecialPerson(Person):
  pass

  def greet(self):
    super().greet()
    print("I am special person")

p1 = Person("Emil")
p1.greet()

p2 = SpecialPerson("Mary")
p2.greet()