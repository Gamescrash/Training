class Father():
    def gardening(self):
        print("I enjoy gardening")

class Mother():
    def cooking(self):
        print("I love cooking")

class Child(Father,Mother):
    def sports(self):
        print("I enjoy sports")


c = Child()
c.gardening()
c.cooking()
c.sports()