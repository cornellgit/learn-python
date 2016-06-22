import multiprocessing
import os
import subprocess

# 1. run linux shell and grab it's output
print(subprocess.getoutput('date -u'))
# this only return standard output as byte type
print(subprocess.check_output(['date', '-u']))

# use piping
print(subprocess.getoutput('date -u | wc'))
# show exit status
print(subprocess.getstatusoutput('date -u'))

# 2. run command and track exit status only
print(subprocess.call('date -u', shell=True))
print(subprocess.call(['date', '-u']))


# 3. run multiple independent processes concurrently
def do_it(param):
    print('pid: %s param: %s' % (os.getpid(), param))


for i in range(4):
    p = multiprocessing.Process(target=do_it, args=(i,))
    p.start()



