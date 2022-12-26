import random
from abc import ABC, abstractmethod

# class parent
class RobotModel:
    def __init__(self, name, color, id):
        self.name = name
        self.color = color
        self.id = id

    def walk(self):
        print("i can walk now")

    def say_something(self):
        raise NotImplementedError

    # methode magique
    def __str__(self):
        return f"My name is {self.name}, i'm a {self.color} robot, and my id is : {self.id}"

    def __repr__(self):
        return f"My name is {self.name}, i'm a {self.color} robot, and my id is : {self.id}"


# class enfant
class RobotFigther(RobotModel):
    def fight(self):
        print("i fight !")

    def say_something(self):
        print("Hello Sir, Please show me your ID")


# class enfant
class RobotFireFigther(RobotModel):
    def put_out_a_fire(self):
        print("i fight the fire !")

    def say_something(self):
        print("We are there to protect you. Please stay behind the line")


# class enfant
class RobotCook(RobotModel):
    def cook(self):
        print("i can cook something")

    def say_something(self):
        print("What can I cook for you today?")


class RobotFactory(ABC):
    # @staticmethod est utilisé
    # pour appeller cette methode de facon static
    # c'est à dire sans avoir besoin d'instancier
    # la classe RobotFactory
    # @staticmethod
    # @classmethod
    # permet de définir une methode en "classmethod"
    # s'utilise avec cls et le mettre partout.
    # ca permet de ne pas avoir à instancer Robotfactory
    # et de l'utiliser quand meme.
    def set_caracteristic():
        name_list = ["robert", "paul", "andersson", "nicolas"]
        color_list = ["red", "green", "black", "blue", "yellow"]
        id_list = [i for i in range(1000)]
        return (
            random.choice(name_list),
            random.choice(color_list),
            random.choice(id_list),
        )

    def create_robot_in_batch(number_of_robot):
        # * sert a dépacker les données retournées par
        # la methode set_carac...
        return [
            RobotFigther(*RobotFactory.set_caracteristic())
            for i in range(number_of_robot)
        ]


my_robot_army: list = []
robot_identities = [
    ["jack", "blue", "123"],
    ["robert", "red", "345"],
    ["paulette", "green", "000"],
]

for elem in robot_identities:
    my_robot_army.append(RobotFigther(name=elem[0], color=elem[1], id=elem[2]))

print(RobotFactory.create_robot_in_batch(number_of_robot=1000))
