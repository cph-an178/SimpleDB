import os

class SimpleDB():
    def __init__(self, db_file="database.db"):
        if not os.path.isfile(db_file):
            open(db_file, "a").close()

        self.db_file = db_file
        self.bytes_offset = {}

        with open(db_file, "rb") as bytefile:
            byte_pos = 0
            for line in bytefile:
                key_end = line.find(b':')
                key = line[:key_end].decode('UTF-8')
                self.bytes_offset[key] = byte_pos
                byte_pos = line.find(b'\n') + 1

    def get(self, key):
        byte_start = self.bytes_offset[key]
        with open(self.db_file, 'rb') as f:
            f.seek(byte_start)
            line = f.readline()
            key_end = line.find(b':')
            return line[key_end + 1:].decode('UTF-8')

    def add(self, key, value):
        # TODO add key and value to bytefile
        byte_start = list(self.bytes_offset.values())[-1]
        with open(self.db_file, "wb") as f:
            f.seek(byte_start)
            str_text = "{0}:{1}".format(key, value)
            f.write(str_text.encode('ascii'))
