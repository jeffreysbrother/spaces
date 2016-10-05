#!/usr/bin/python
import os

#this script will replace all spaces with hyphens and convert all uppercase characters to lowercase
path  = os.getcwd()
filenames = os.listdir(path)
for filename in filenames:
    os.rename(os.path.join(path, filename), os.path.join(path, filename.replace(' ', '-').lower()))
