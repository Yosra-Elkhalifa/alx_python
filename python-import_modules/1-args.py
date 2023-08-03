import sys

def main():
    argv = sys.argv[1:] #let list start from index 1 as index 0 is reserved for script name
    num_arguments = len(argv)
    # print number of arguments followed by : or . 
    if num_arguments < 1:
        print("{} arguments.".format(num_arguments))
    elif num_arguments == 1:
        print("{} argument.".format(num_arguments))
    else:
        print("{} arguments:".format(num_arguments))

    # print list content
    counter = 1
    for arg in argv:
        print("{} : {}".format(counter, arg))
        counter += 1



if __name__ == "__main__":
    main()