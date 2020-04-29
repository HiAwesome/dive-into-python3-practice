class SuperDynamo:
    def __getattribute__(self, item):
        if item == 'color':
            return 'PapayaWhip'
        else:
            raise AttributeError


if __name__ == '__main__':
    dyn = SuperDynamo()
    print(dyn.color)
    print()

    dyn.color = 'LemonChiffon'
    print(dyn.color)

"""
PapayaWhip

PapayaWhip
"""
