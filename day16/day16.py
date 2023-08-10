class Student:
    def __init__(self, name, group):
        self.name = name
        self.group = group

    def show(self):
        print(self.name, self.group)

    def __del__(self):
        print("I've been died!")


student1 = Student("Matvey", "LightCode")
student1.show()
del student1