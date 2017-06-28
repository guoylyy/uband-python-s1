class Monster():
    def __init__(self, name, ability):
        self.name = name
        self.ability = ability

    def describe(self):
        print('{} is a monster, who can {}.'.format(self.name, self.ability))

def main():
    moustar = Monster('liluyao', 'eat everything')
    moustar.describe()

if __name__ == '__main__':
    main()
        