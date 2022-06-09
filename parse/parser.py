import json
import sys

#Get ip only
def get_ip():
    filename = sys.argv[2]
    input_file = open (filename, "r")
    output_file = open("output.txt", "w")
    for line in input_file:
        jsonObj = json.loads(line)
        ip = jsonObj.get ('ip_str')
        output_file.write(f"{ip}\n")

#Get ports only
def get_port():
    filename = sys.argv[2]
    input_file = open (filename, "r")
    output_file = open("output.txt", "w")
    for line in input_file:
        jsonObj = json.loads(line)
        port = jsonObj.get ('port')
        output_file.write(f"{port}\n")

#Get ip:port
def get_ip_port():
    filename = sys.argv[2]
    input_file = open (filename, "r")
    output_file = open("output.txt", "w")
    for line in input_file:
        jsonObj = json.loads(line)
        ip = jsonObj.get ('ip_str')
        port = jsonObj.get('port')
        output_file.write(f"{ip}:{port}\n")


