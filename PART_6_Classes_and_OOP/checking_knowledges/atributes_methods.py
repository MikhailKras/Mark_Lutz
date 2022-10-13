class Attrs:
    def __getattr__(self, item):
        print(f'get {item}')

    def __setattr__(self, key, value):
        print(f'set {key, value}')


x = Attrs()
x.asdasd
x.sdgjkansdfglasd= 123124