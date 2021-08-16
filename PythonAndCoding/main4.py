# class PlayerCharacter:
#     # membership = True
#     def __init__(self, name='Anonymous',age=0):
#         if (age>=18): # if (self.membership): # # (PlayerCharacter.membership)
#             self.name = name
#             self.age = age
#         else: print("You are underage")
#     def run(self):
#         print('Run')
#         return 'Done' 
#     def say(self):
#         print(f'My name is {self.name}')
#         return 'Done' 
# player1=PlayerCharacter('Baby',25)
# player2=PlayerCharacter()
# player1.attack = 500
# print(player1.age)
# print(player1.run())
# print(player1.membership)
# print(player1.attack)
# print(player1.say())
# print(PlayerCharacter('Boobooooo',24).name)

#class PlayerCharacter:
#    membership = True
#    def __init__(self, name, age):
#        self.name = name #attributes
#        self.age = age
#    def shout(self):
#        print(f'My name is {self.name}')
#    @classmethod
#    def add_things(cls, num1, num2):
#        return cls('Tod', num1 + num2)#return num1+num2
#    @staticmethod
#    def ADD_things(Num1, Num2):
#        return Num1+Num2
#player1 = PlayerCharacter('Bob', 20)#player1 = PlayerCharacter('Bob', 20)
#player2 = PlayerCharacter.add_things(8,10)
#print(player1.ADD_things(10,8))#print(PlayerCharacter.add_things(9,9))
#print(player2.age)

#class PlayerCharacter:
#    def __init__(self, name, age):
#        self.name = name
#        self.age = age
#player1 = PlayerCharacter('Anni',125)
#print(player1.name)
#print(player1.age)
#player2={'name':'Anni','age':125}
#print(player2['name'])
#print(player2['age'])

#class User():
#    def __init__(self, email='xyz@gmail.com'):
#        self.email = email
#    def sign_in(self):
#        return 'Logged in'
#class Wizard(User):
#    def __init__(self, name='XYZ', power=0, email='xyz@gmail.com'):
#        super().__init__(email)#User.__init__(self, email)
#        self.name = name
#        self.power = power
#    def attack(self):
#        print(f'Attacking with the power of {self.power}')
#class Archer(User):
#    def __init__(self, name='XYZ', arrows=0):
#        self.name = name
#        self.arrows = arrows
#    def check_arrows(self):
#        print(f'Attacking with arrows: Arrows left({self.arrows})')
#    def run(self):
#        return 'Ran really fast'
#class Hybrid(Wizard,Archer):
#    def __init__(self, name='XYZ', power=0, arrows=0):
#        Wizard.__init__(self, name, power)
#        Archer.__init__(self, name, arrows)
#hyb = Hybrid('BigBoy',50,100)
#print(hyb.sign_in())
#wizard1=Wizard('Zeus',50, 'zeus@gmail.com')
#archer1=Archer('Athena',100)
#wizard1.attack()
#print(wizard1.email)
#print(isinstance(wizard1,Wizard))
#print(dir(wizard1))

#class Toy():
#    def __init__(self, color, age):
#        self.color = color
#        self.age = age
#        self.my_dict = {'name':'Bobo','pets':'None'}
#    def __str__(self):
#        return f'{self.color}'
#    def __len__(self):
#        return 10
#    def __call__(self):
#        return 'Yes?'
#    def __getitem__(self, i):
#        return self.my_dict[i]
#action_fig = Toy('red', 0)
#print(action_fig.__str__())
#print(str(action_fig))
#print(len(action_fig))
#print(len('123456789'))
#print(action_fig())
#print(action_fig['name'])

#class SuperList(list):
#    def __len__(self):
#        return 100
#super_list1 = SuperList()
#print(super_list1.__len__())
#super_list1.append(5)
#print(super_list1[0])
#print(issubclass(SuperList, list))