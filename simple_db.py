import os

class SimpleDB():
    def __init__(self, db_file="database.db"):
        # Checking if the database exist
        if not os.path.isfile(db_file):
            # If not it creates the database
            open(db_file, "a").close()

        # Set class variables 
        self.db_file = db_file
        self.bytes_offset = {} # this is a python dictionary = Hash map

        # Opening the database with 'read binary' as bytefile
        with open(db_file, "rb") as bytefile:
            # Starting byte offset
            byte_pos = 0
            # For eact line in the bytefile
            for line in bytefile:
                # Finding the byte position for where the key ends
                key_end = line.find(b':')
                # Decodes the key from binary to string
                key = line[:key_end].decode('UTF-8')
                # Adding key and byte offset to dictionary
                self.bytes_offset[key] = byte_pos
                # Changing the byte offset to start of next line
                byte_pos = line.find(b'\n') + 1
    
    def get(self, key):
        # TODO add comments
        byte_start = self.bytes_offset[key]
        with open(self.db_file, 'rb') as f:
            f.seek(byte_start)
            line = f.readline()
            key_end = line.find(b':')
            return line[key_end + 1:].decode('UTF-8')

    def add(self, key, value):
        # TODO add comments
        with open(self.db_file, "ab") as f:
            offset = 0
            if self.bytes_offset:
                offset = f.seek(0, os.SEEK_END)
            self.bytes_offset[key] = offset
            str_text = "{0}:{1}\n".format(key, value)
            f.write(str.encode(str_text))
            
            
        
