# my_module.py

def greet(name):
    """A function that greets a given name."""
    return f"Hello, {name}!"

def main():
    """The main function to be executed when the script is run directly."""
    print("Running my_module.py directly.")
    print(greet("World"))

if __name__ == "__main__":
    main()

print(f"The value of __name__ is: {__name__}")
