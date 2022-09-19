from typing import TextIO


class Processor:
    def __init__(self, reader: TextIO, writer: TextIO):
        self.reader = reader
        self.writer = writer

    def process(self):
        while True:
            data = self.reader.readline()
            if not data:
                break
            data = self.converter(data)
            self.writer.write(data)

    def converter(self, data):
        assert False, 'converter must be defined'
