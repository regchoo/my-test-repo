#!/usr/bin/env python

f = open("evillist.txt", "a")
for x in range(0,9999999999):
    f.write("%010d\n" % x)
    f.flush()
f.close()
