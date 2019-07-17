class Person():
  def __init__(self, name, year_of_birth):

    self.name = name
    self.year_of_birth = year_of_birth

  def detail(self, name):
    print("Name of the person is {}".format(name))

  def age(self, year_of_birth):
    print("You are {} Years Old".format(year_of_birth))

person = Person('Vihar', 1998)
person.detail('Vihar')
person.age(19)