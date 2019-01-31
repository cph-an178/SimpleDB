import pickle
import argparse

def run():

    parser = argparse.ArgumentParser()

    parser.add_argument("-a", "--add", help="Add to database", action="store_true")
    parser.add_argument("-g", "--get", help="Get from database", action="store_true")
    parser.add_argument("input", metavar="i",  help="Input for what you want to add or what key you want to search for")

    args = parser.parse_args()
    
    if args.add:
        rv = add_to_dict(args.input)
        print(rv)
    elif args.get:
        rv = get_from_dict(args.input)
        print(rv)

def add_to_dict(value):
    dictionary = load_dict()
    dictionary[len(dictionary)] = value
    save_dict(dictionary)

    return "Your key is {0} and you added {1}".format(len(dictionary) - 1, value)

def get_from_dict(key):
    dictionary = load_dict()
    return dictionary[int(key)]

def save_dict(dictionary):
    with open("db_dump.pkl", "wb") as f:
        pickle.dump(dictionary, f)

def load_dict():
    with open("db_dump.pkl", "rb") as f:
        return pickle.load(f)

if __name__ == "__main__":
    run()