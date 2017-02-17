#!/usr/bin/env python

from subprocess import call

file_name = "dependencies"

file_object = open(file_name, "r")

current_dependency = "dummy text for first loop check"

while (current_dependency):
  current_dependency = file_object.readline()
  current_dependency = current_dependency.rstrip()
  call(["git", "clone", current_dependency])

# EOF
