class Lifecycle:
    def __init__(self, name):
        self.name = name
        print(f"Object {self.name} has been created.")

    def __del__(self):
        print(f"Object {self.name} is being destroyed.")
