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
                byte_pos = byte_pos + line.find(b'\n') + 1
    
    def get(self, key):
        # Get the byte offset from the dictionary
        byte_start = self.bytes_offset[key]
        # Open the file with 'read binary' as f
        with open(self.db_file, 'rb') as f:
            # Change file pointer to to the byte offset
            f.seek(byte_start)
            # Read the line
            line = f.readline()
            # Find where the key ends
            key_end = line.find(b':')
            # Return everythin after ':' decoded to UTF-8
            return line[key_end + 1:].decode('UTF-8')

    def add(self, key, value):
        # Open the file with 'append binary' as f 
        with open(self.db_file, "ab") as f:
            # If it's the first time something gets added, the byte offset is 0 
            offset = 0
            # If theres elements in the dictionary
            if self.bytes_offset:
                # The offset becomes the last line in the file
                offset = f.seek(0, os.SEEK_END)
            # Add new key and offset to dictionary
            self.bytes_offset[key] = offset
            # Format key and value to a string
            str_text = "{0}:{1}\n".format(key, value)
            # Write the string encoded to binary to the file
            f.write(str.encode(str_text))
            
            
        
