class Animal(object):
    owner = 'jack'
    def __init__(self, name):
        self._name = name
    def get_name(self):
        return self._name
    def set_name(self,value):
        self._name = value
    def make_sound(self):
        pass
    @classmethod
    def get_owner(cls):
        return cls.owner
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self,value):
        if isinstance(value,int):
            self._age = value
        else:
            raise ValueError

class Dog(Animal):
    def make_sound(self):
        print(self.get_name() + ' is making sound wang wang wang...')

class Cat(Animal):
    def make_sound(self):
        print(self.get_name() + ' is making sound miu miu miu...')

#dog = Dog('wangcai')
#cat = Cat('Kitty')
#dog.make_sound()
#cat.make_sound()
animals = [Dog('wangcai'),Cat('kitty'),Dog('laifu'),Cat('betty')]
for animal in animals:
    animal.make_sound()

print(Animal.get_owner())
print(Cat.get_owner())

animals[0].age = 3
print(animals[0].age)

