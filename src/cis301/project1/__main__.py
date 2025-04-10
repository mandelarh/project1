import sys
def main(args=None):
    """
        This program that parses the command line, creates a
        Student, and prints a description of the student to
        standard out by invoking its toString method.
    """
    if args is None:
        args = sys.argv[1:]

    print ("List of arguments: " , args)
    print (f"Missing command line arguments")
    parse_cli_argv(args)
    exit(0)

def parse_cli_argv(argv):
    #raise NotImplementedError('not implemented yet')
    #process input/args
    #get name
    #process name
    #get gpa
    #get classes
    #instantiating student object
    #ex student = student(arguments)
    #print student
    pass
if __name__ == "__main__":
    main()