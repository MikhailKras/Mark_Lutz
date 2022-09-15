class Chinara:
    def __init__(self, name, mood):
        self.name = name
        self.mood = mood
        print('Hello, Chinara!')

    def in_home(self):
        print('Chinara in home!')

    def __del__(self):
        print('Bye, Chinara!')


if __name__ == '__main__':
    chin = Chinara('Chinara', 'nice')
    chin.in_home()
    chin = 2