#!/usr/bin/env python3

# file: driver.py
#

# description: driver program for tgdh scheme
#

# version: 6
# 0: generating a simple tree structure given initial data
# 1: make a tree class to maintain nodes
# 2: use inheritance to organize the node class
# 3: add functionality: TypeAssign method, IDAssign method, FindMe method
# 4: add functionality: join event, leave event, post-run command line instructions; incorporate more built-in anytree functions; key generation
# 5: establish communication protocol; implement networking features
# 6: implement join and leave operations (single-member events)
#

# usage:
#  python3 driver.py -s <initial size> -i <unique member ID>

# import modules
#
import sys
from functs import cmdl_parse, get_instructions, join_protocol, event_check, clear_file
from BinaryTree import BinaryTree
import time

# function: main
#
def main(argv):

    # get command line arguments
    #
    (isize, uid, jstatus, lstatus, ip_addr) = cmdl_parse(argv[1:len(argv)])

    if jstatus:

        # initiate join protocol
        #
        print("########################################")
        print("Joining the group ...")
        btree = join_protocol(ip_addr)
        btree.NewMemberProtocol()
        clear_file("files/events.txt")
        print("Group key: {0}".format(btree.root.key))
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

        # check the events.txt file every few seconds
        #
        try:
            print("Waiting for event ... ")
            while True:
                time.sleep(5)
                (event, ip_addr_send) = event_check()
                if event == 1:
                    btree.JoinEvent(ip_addr_send)
                    print("Group key: {0}".format(btree.root.key))
                    print("Waiting for event ... (")
                elif event == 2:
                    pass
        except KeyboardInterrupt:

            # exit gracefully
            #
            print("Freeing resources and exiting ...")
            return(0)  # exit gracefully

#
# end function: main

# begin gracefully
#
if __name__ == "__main__":
    main(sys.argv)

#
# end file: driver.py
