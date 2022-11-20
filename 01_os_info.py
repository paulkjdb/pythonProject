import platform
import sys

Import ...
    info = 'OS info is \n {} \n\nPython version is {}{}'.format (
        platform.uname(),sys.version, platform.architecture())
    )
with open('os info.txt','w') as ff:
    ff.write(info)