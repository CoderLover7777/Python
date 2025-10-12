class student:
    grade = 7
    name = "Adit"
    place = "U.A.E"
    def introduction(self):
        print("Hi I am a student")
    def details(self):
        print("My name is", self.name)
        print("I study in Grade", self.grade)
        print("I live in the", self.place)
ob = student()
ob.introduction()
ob.details()