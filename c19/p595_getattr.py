class Dynamo:
    def __getattr__(self, item):
        if item == 'color':
            return 'PapayaWhip'
        else:
            raise AttributeError


if __name__ == '__main__':
    dyn = Dynamo()
    print(dyn.color)
    print()

    dyn.color = 'LemonChiffon'
    print(dyn.color)

"""
PapayaWhip

LemonChiffon
"""
