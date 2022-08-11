#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   For - Using a file's lines as a source for the for-loop"""

# open file in read mode
with open("dnsservers.txt", "r") as dnsfile:

    # loop over lines
    for svr in dnsfile:
        svr = svr.rstrip('\n')

        if svr.endswith('org'):
            with open("org-domain.txt", "a") as srvfile:
                srvfile.write(svr + "\n")

        elif svr.endswith('com'):
            with open("com-domain-txt", "a") as srvfile:
                srvfile.write(svr + "\n")


