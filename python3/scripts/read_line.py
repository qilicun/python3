#!/usr/bin/env python
import re
import numpy as np
import argparse

#parser = argparse.ArgumentParser(description="Read special keyword")
#parser.add_argument('-f', '--filen', help="Name of file", default=None, required=True)
#parser.add_argument('')
def read_to_dict(filen):
    dm = {}
    string = ""
    data = []
    with open(filen, 'r') as f:
        for line in f.readlines():
            line = line.strip()
            if not len(line):
                continue
            if re.match("^-", line):
                continue
            pattern = '[A-Z]'
            if re.match(pattern, line):
                string = line
                continue
            line = line.split()
            print line
            if line[-1] != "/":
                data += line
            else:
                data += line[0:-1]
                dm[string] = data
                data = []
    return dm

def get_keywords_value(dm, string):
    return dm[string]

def convert_to_ndarray(dm):
    for key in dm:
        dm[key] = np.array(dm[key]).reshape(len)


filen = "test.dat"

dm=read_to_dict(filen)

print "PVTO"
print dm["PVTO"]
print "================================="
print "SWOF"
print dm["SWOF"]
