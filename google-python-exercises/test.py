import sys

#defines a hello() function that prints hello and the argument 'name'
def hello(name):
    if name == "Will":
        print ("shiiiii what's up my slime")
    else:
        print("Hello" , name)

# Defines a main() function that calls hello() and  prints the first argument
def main():
    hello(sys.argv[1])

if __name__ == '__main__':
    main()
