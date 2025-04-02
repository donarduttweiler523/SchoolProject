class MyClass:
    def __init__(self):
        self.data = []

    def add_data(self, item):
        self.data.append(item)

    def print_data(self):
        for item in self.data:
            print(item)
