import pickle

def run():
    i = input("Type 'a' to add something to the db or 'g' to get something \n>")
    
    if i is "a":
        v = input("Type what you want to add\n>")
        rv = add_to_dict(v)
        print(rv)
    elif i is "g":
        k = input("Type the key you want to search for\n>")
        rv = get_from_dict(k)
        print(rv)
    else:
        print("Invalid input")

def add_to_dict(value):
    # TODO load dict and add to dict

    dictionary = load_dict()
    dictionary[len(dictionary)] = value
    save_dict(dictionary)

    return "Your key is {0} and you added {1}".format(len(dictionary) - 1, value)

def get_from_dict(key):
    
    dictionary = load_dict()
    print(dictionary)

    return dictionary[int(key)]

def save_dict(dictionary):
    with open("db_dump.pkl", "wb") as f:
        pickle.dump(dictionary, f)

def load_dict():
    with open("db_dump.pkl", "rb") as f:
        return pickle.load(f)

if __name__ == "__main__":
    run()