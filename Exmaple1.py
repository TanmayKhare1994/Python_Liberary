import sys;

# Command line args are in sys.argv[1], sys.argv[2] ...
    # sys.argv[0] is the script name itself and can be ignored
def main():
    print "test google",sys.argv[0],sys.argv[1];

# Standard boilerplate to call the main() function to begin the program.
if __name__=='__main__':
    main()