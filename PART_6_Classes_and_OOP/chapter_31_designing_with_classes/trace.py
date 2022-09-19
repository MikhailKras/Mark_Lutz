class Wrapper:
    def __init__(self, obj):
        self.obj = obj

    def __getattr__(self, item):
        print('Trace: ' + item)
        return getattr(self.wrapped, item)
        