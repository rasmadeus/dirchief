#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
import os

def create_parser():
	parser = argparse.ArgumentParser()
	parser.add_argument("path", help="Spicify a path to file or dir what you want to create")
	parser.add_argument("--is_file", help="If this flag setted a file will be created", action="store_true")
	return parser


def touch(path):
	try:
		open(path, "a").close()
	except Exception as ex:
		print("Couldn't create file because: {ex}".format(ex=ex))


def mkdir(path):
	import os
	try:
		os.mkdir(path)
	except Exception as ex:
		print("Couldn't create dir because: {ex}".format(ex=ex))


if __name__ == "__main__":
	args = create_parser().parse_args()
	if args.is_file:
		touch(args.path)
	else:
		mkdir(args.path)	

