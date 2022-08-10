#!/usr/bin/env python3


## Creating a list of items 
my_list = [ "192.168.0.5", 5060, "UP" ]

# display the input back to the user, but displaying based on list position
print("The first item in the list (IP): " +  my_list[0] )
print("The second item in the list (port): " + str(my_list[1]) )
print("The last item in the list (state): " + my_list[2] )


iplist = [ 5030, "80", 66, "10.0.0.1", "10.20.30.1", "ssh" ]

print("IP addresses: ", iplist[3], ", and", iplist[4])
