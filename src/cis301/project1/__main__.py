import sys

def main(args=None):
    """
        This program that parses the command line, creates a
        Student, and prints a description of the student to
        standard out by invoking its toString method.
    """
    if args is None:
        args = sys.argv[1:]

    print ("List of arguments: " + args)
    print (f"Missing command line arguments")
    exit(0)

def parse_cli_argv(argv):
    raise NotImplementedError('not implemented yet')
    
if __name__ == "__main__":
    main()