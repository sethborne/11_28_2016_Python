class Animal(object):
    def __init__(self, name):
        # print ('Animal')
        self.name = name
        self.health = 100
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def displayHealth(self):
        print ('Name: {} Health: {}'.format(self.name, self.health))
        return self


# monkey = Animal('George')
# monkey.displayHealth().run().walk().displayHealth()
