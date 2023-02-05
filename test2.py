class Person():
    def __init__(self, fullName='имя', age='возраст'):
        self.name = fullName
        self.age = age

    def move(self):
        print(f'{self.name} двигается')
    
    def talk(self):
        print(f'{self.name} говорит')


pers1 = Person()
pers2 = Person("Иван", 17)
pers1.move()
pers2.talk()