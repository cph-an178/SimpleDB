import os
import argparse

def run():

    if not os.path.isfile("db_dump.db"):
        open("db_dump.db", 'a').close()

    parser = argparse.ArgumentParser()

    parser.add_argument("-a", "--add", help="Add to database", action="store_true")
    parser.add_argument("-g", "--get", help="Get from database", action="store_true")
    parser.add_argument("key", metavar="K",  help="Input for what key you want to search for or use to add new object")
    parser.add_argument("value", metavar="V",  help="Input for what value you want to add")

    args = parser.parse_args()
    

def db_set(key, value):
    pass

def db_get(key):
    pass

if __name__ == "__main__":
    run()