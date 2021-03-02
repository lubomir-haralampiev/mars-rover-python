#!/usr/bin/env python

filename = "input.txt"

if __name__ == "__main__":
    file = open(filename, "r")
    lines = [line.strip() for line in file]
    print(lines)
    file.close()
