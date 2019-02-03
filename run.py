import argparse
from simple_db import SimpleDB

def run():
    # TODO implement SimpleDB and make it run with argparse

    sb = SimpleDB()

    parser = argparse.ArgumentParser()

    parser.add_argument("-r", "--run", help="Run the program", action="store_true")
    parser.add_argument("-d", "--dictionary", help="Get the byte offset dictionary", action="store_true")

    args = parser.parse_args()

    if args.run:
        # TODO Run program with inputs
        while True:
            print("Type 'a' or 'add' to add a key and value to the database")
            print("Type 'g' or 'get' to search for a key and return a value")
            print("Type 'q' or 'quit' to quit the program")
            input_1 = input(">")
            if input_1 in ["a", "add"]:
                key = input("Your key\n>")
                value = input("Your value\n>")
                sb.add(key, value)
                print(sb.bytes_offset)
            elif input_1 in ["g", "get"]:
                key = input("Key\n>")
                result = sb.get(key)
                if result == None:
                    print("Couldn't find key: '{0}'".format(key))
                else:
                    print(result)
                    print(sb.bytes_offset)
            elif input_1 in ["q", "quit"]:
                break
            else:
                print("Invalid input")
        
    elif args.dictionary:
        print(sb.bytes_offset)
    

if __name__ == "__main__":
    run()