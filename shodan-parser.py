import json
import sys
from parse import parser
try:
    if sys.argv[1] == "-I":
        parser.get_ip()
    elif sys.argv[1] == "-P":
        parser.get_port()
    elif sys.argv[1] == "-IP":
        parser.get_ip_port()
    else:
        print ("""Usage: shodan-parser.py [ARG] [FILENAME]
    ARGs:
    -I get only ip
    -P get only ports
    -IP get ip:port
    """)

except:
    print ("""Usage: shodan-parser.py [ARG] [FILENAME]
    ARGs:
    -I get only ip
    -P get only ports
    -IP get ip:port
    """)