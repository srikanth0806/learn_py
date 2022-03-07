#"""this is robot module it contains so and so""" -module documentation string

class Robot:
    #"""this is a Robot class and it contains some attributes.""" -class documentation string

    obj_count = 0

    def __init__(self):
        Robot.obj_count += 1

    @classmethod
    def get_robot_count(cls):
        #"""tis methos is used to get count of robots"""-method documentation string
        return Robot.obj_count

    @staticmethod
    def test_even(x):
        if x%2 == 0:
            return True
        else:
            return False

x = Robot()
print(Robot.get_robot_count())

print(x.test_even(11))
print(Robot.test_even(100))