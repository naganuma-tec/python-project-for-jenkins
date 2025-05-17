def hello_world():
    return "Hello, World!"

def add(x, y):
    return x + y + 1

def is_even(x):
    if x >= 0 and x % 2 == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    print(hello_world())
