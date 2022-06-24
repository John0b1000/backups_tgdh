# file: functs.py
#

# description: contains functions for tgdh driver program
#

# import modules
#
import sys
import argparse

# function: cmdl_parse
#
def cmdl_parse(alist):
    
    # parse the command line arguments
    #
    parser = argparse.ArgumentParser(description='Generate a Binary Key Tree')
    parser.add_argument('-s', metavar='isize', type=int, help='the initial size of the group')        
    parser.add_argument('-i', metavar='uid', type=int, help='unique member id')
    parser.add_argument('-j', metavar='join', default=False, help='indicate a joining member')
    parser.add_argument('-l', metavar='leave', default=False, help='indicate a leaving member')
    if len(alist) == 0:
        print("**> Error: Insufficient number of arguments specified.")
        parser.print_help(sys.stderr)        
        sys.exit(1)
    else:
        args = parser.parse_args(alist)

    # return in a tuple
    #
    return(args.s, args.i, args.j, args.l)

#
# end function: cmdl_parse

# function: get_instructions
#
def get_instructions(btree):

    # receive command line input
    #
    while True:
        print("########################################")
        instruct = input(">> Enter event here: ")
        print("########################################")
        if instruct == "join" or instruct == "j":
            btree.JoinEvent() 
        elif instruct == "leave" or instruct == "l":
            lmem = int(input(">> Enter leaving member ID: "))
            print("\tMember " + str(lmem) + " is leaving ...")
            print("---------------//---------------")
            btree.LeaveEvent(lmem)
        elif instruct == "q" or instruct == "quit":
            print("Freeing resources and exiting ...")
            return(True)  # exit gracefully
        elif instruct == "f" or instruct == "find":
            ans = input(">> Would you like to find a member or node? ")
            if ans == "m" or ans == "member":
                iden = input(">> Enter the member ID: ")
                fmem = btree.FindNode(iden, True)
                fmem.PrintAttributes()
            elif ans == "n" or ans == "node":
                iden = input(">> Enter node index (l,v): ")
                fnode = btree.FindNode(iden, False)
                fnode.PrintAttributes()
            else: print("**> Error: Invalid response!")
        elif instruct == "p" or instruct == "print":
            btree.TreePrint()
        elif instruct == "vp" or instruct == "verbose print":
            btree.TreePrint()
            btree.VerboseNodePrint()
        elif instruct == "u" or instruct == "update":
            btree.TreePrepEvent()
            btree.TreeRefresh()
        elif instruct == "pg" or instruct == "print_group_key":
            print("Group Key is: " + str(btree.root.key))
        else:
            print("**> Error: Invald input!")

#
# end function: get_instructions

# function: parse_config
#
def parse_config(line):

    # split the line into parts
    #
    parts = line.split('=')
    if parts[0] == 'groups':
        parts[1] = parts[1].split(',')
        parts[1] = [part.rstrip('\'').lstrip('\'') for part in parts[1]]
    else:
        parts[1] = parts[1].rstrip('\'').lstrip('\'')
    return(parts)

#
# end function: parse_config

# function: fread_config
#
def fread_config(fp):

    # read the file line by line using a buffer
    #
    mcast_params = {}
    for line in fp:
        line = line.rstrip('\n')
        if line != "[Settings]" and line != '\n':
            param = parse_config(line)
            mcast_params[param[0]] = param[1]
    return(mcast_params)
    
#
# end function: fread_config

# function: fread_keys
#
def fread_keys(fp):

    # read the file line by line using a buffer
    #
    for line in fp:
        line = line.rstrip('\n')
        return(line.split('/'))
    
#
# end function: fread_keys

# function: clear_file
#
def clear_file(path):

    # clear a file with a specified path
    #
    f = open(path, 'w')
    f.close()

#
# end function: clear_file

#
# end file: functs.py
