# Assignment 1 - Simple DB with Hashmap-based Index

This is the first assignmet for Software Development cource Databases.

I've wrote this project in Python, and you need Python3 to run it correctly.

This project uses one Standard Library, `argparse`. So there shouldn't be a need to install anything with pip.  

## How to run the program

In your terminal in the project directory, write `python3 run.py -r` to run the program.

When you're in the program you have 3 options:

1. Type 'a' or 'add' and you'll be asked to first type a key, then an value. **Keys must be unique**, or else it will overwrite the the previos byte offset to the new value.
2. Type 'g' or 'get' and you'll be asked to type a key, then it will print the value if it matches with a key in the dictionary.
3. Type 'q' or 'quit' to quit the program.

 
You can also write `python3 run.py -d` to get the byte offset dictionary or `python3 run.py -h` to get help text.

