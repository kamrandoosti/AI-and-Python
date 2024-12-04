#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 18:13:40 2024

@author: kamran
"""

import sys
import subprocess as subprocess
pythonversion= sys.version
# print(pythonversion)
# platform=sys.platform
# print(platform)
# varsize=sys.getsizeof(platform)
# print(varsize)

# defaultencodin=sys.getdefaultencoding()
# print(defaultencodin)

# firstarg=sys.argv[1]
# secondarg=sys.argv[2]

# print(firstarg,secondarg)  

#use argv in practice
ip=sys.argv[1]
count=sys.argv[2]
print(subprocess.run(['ping',ip,'-c',count]))





