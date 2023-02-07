import getopt
import sys

opts, args = getopt.getopt(sys.argv[1:], "hle:t:p:cu:", ["help" , "listen" ,"exeute" ,"target" , "port" , "command" , "upload"]) 

print(opts)
print(args)
