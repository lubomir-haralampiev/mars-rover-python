#!/usr/bin/env python

from os import path
from mars_rover import process_lines

# folder structure adopted from https://realpython.com/python-application-layouts/

filename = "input.txt"
file_path = path.join(path.dirname(__file__), "", "data", filename)

if __name__ == "__main__":
    file = open(file_path, "r")
    lines = [line.strip() for line in file]
    print(lines)
    file.close()
    process_lines.main(lines)
