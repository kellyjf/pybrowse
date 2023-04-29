#!/usr/bin/python3
from argparse import ArgumentParser as ap

import sqlalchemy
from app_browser import getBrowser

import re
a=re.compile(".*")
b=a.match("Anything")

getBrowser(b)


if __name__ == "__main__":
	parser=ap()
	parser.add_argument("--list","-l", action="store_true", help="List Database")
	args=parser.parse_args()




