from streams import Processor


class Uppercase(Processor):
    def converter(self, data):
        return data.upper()


if __name__ == '__main__':
    import sys
    obj = Uppercase(open('test'), sys.stdout)
    obj.process()
