#!/usr/bin/env python

#---------------------------------------------------------
# Name:        URL Unique reducer
# Author:      loghyr
# Created:     26-07-2013
#------------------------------------------------------

import sys
res = {}
for line in sys.stdin:
	try:
		line = line.strip()
		if res.has_key(line[0:32]) == False:
			res[line[0:32]] = line[33:]

	except Exception,e:
		pass

for i in res:
    print res[i]
