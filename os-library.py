#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 20:21:38 2024

@author: kamran
"""
# print working directory
import os
import subprocess as subprocess
import signal
# print(subprocess.getoutput('ls -alh'))
# print(os.getcwd())
# print('===================================')
# # change working directory
# os.chdir('/home/kamran/git-test')
# print(os.getcwd())
# print(subprocess.getoutput('ls -alh'))

# return list of files and directories

# print('==========cl

#os.mkdir('testdir')

# os.rmdir('testdir')
# working with environment variables

print(os.environ)

# retrieves the value of specific environment variable
print('------------------------')
print(os.environ.get('HOME'))

# set an environment value

os.environ['test']='hello'
print(os.environ.get('test'))

# run a command usin os library

os.system("ls")

# rename a file or directory

# os.rename('test4', 'test4')

# remove a file

# os.remove('test4')

# make dirs recursively

os.makedirs('/home/kamran/git-test/test1/test2/test3', exist_ok=True)
# os.removedirs('/home/kamran/git-test/test1/test2/test3')


# CHECK THE FILE/DIRECTORY EXISTENCE

print(os.path.exists('/home/kamran'))

# check the file type

print(os.path.isfile('/home/kamran'))

# check the directory size

print(os.path.getsize('/home/kamran'))


# get system platform

print(os.name)

print(os.uname())

print(os.getpid())
print(os.getlogin())

#print(os.kill(2537, signal.SIGTERM))
