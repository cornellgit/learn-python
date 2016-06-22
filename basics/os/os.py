# ref https://developers.google.com/edu/python/utilities#file-system----os-ospath-shutil

import os
import sys
import urllib
import subprocess


# 1. access files
def printdir(dir):
    filenames = os.listdir(dir)
    for fn in filenames:
        print(fn)
        # relative to current dir
        print(os.path.join(dir, fn))
        # get absolute file path
        print(os.path.abspath(os.path.join(dir, fn)))


# printdir('./')
# for more, dir(os), help(os)


# 2. HTTP
def wget(url):
    try:

        ufile = urllib.request.urlopen(url)
        print('base url:' + ufile.geturl())
        print(ufile.read())
    except IOError:
        sys.stderr.write('problem reading:' + url)

# wget("https://www.google.com")


# 3. running command
def listdir(dir):
    res = subprocess.run(['ls', '-l', dir], stdout=subprocess.PIPE)
    print(res.stdout)

listdir('./')
