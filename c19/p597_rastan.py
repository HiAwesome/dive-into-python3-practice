class Rastan:
    def __getattribute__(self, item):
        raise AttributeError

    def swim(self):
        pass


if __name__ == '__main__':
    hero = Rastan()
    hero.swim()

"""
Traceback (most recent call last):
  File "/Users/moqi/Code/dive-into-python3-practice/c19/p597_rastan.py", line 11, in <module>
    hero.swim()
  File "/Users/moqi/Code/dive-into-python3-practice/c19/p597_rastan.py", line 3, in __getattribute__
    raise AttributeError
AttributeError
"""
