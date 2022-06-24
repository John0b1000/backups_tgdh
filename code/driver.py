#!/usr/bin/env python3

# file: driver.py
#

# description: driver program for tgdh scheme
#

# version: 5
# 0: generating a simple tree structure given initial data
# 1: make a tree class to maintain nodes
# 2: use inheritance to organize the node class
# 3: add functionality: TypeAssign method, IDAssign method, FindMe method
# 4: add functionality: join event, leave event, post-run command line instructions; incorporate more built-in anytree functions; key generation
# 5: establish communication protocol; implement networking features
#

# usage:
#  python3 driver.py -s <initial size> -i <unique member ID>

# import modules
#
import sys
from functs import cmdl_parse, get_instructions
from BinaryTree import BinaryTree

# function: main
#
def main(argv):

    # get command line arguments
    #
    (isize, uid, jstatus, lstatus) = cmdl_parse(argv[1:len(argv)])

    if jstatus:

        # initiate join protocol
        #
        print("########################################")
        print("Multicasting a join message to the group ...")
        print("Multicasting blind key for the sponsor ...")
        print("Waiting for the sponsor to send me the serialized tree ...")
        print("Tree received! Calculating the group key ...")
        print("########################################")

    elif lstatus:

        # initiate leave protocol
        #
        print("########################################")
        print("Multicasting a leave message to the group ...")
        print("Freeing resources and exiting ...")
        print("########################################")

    else: 

        # instantiate a binary tree object
        #
        print("########################################")
        print("Initializing ...")
        btree = BinaryTree(size=isize, uid=uid)
        print("########################################")

        # wait for instructions from the commmand line
        #
        get_instructions(btree)

    # exit gracefully
    #
    return(0)

#
# end function: main

# begin gracefully
#
if __name__ == "__main__":
    main(sys.argv)

#
# end file: driver.py
