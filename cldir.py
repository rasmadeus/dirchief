#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
import os
import shutil

def create_parser():
	parser = argparse.ArgumentParser()
	parser.add_argument("path", help="Spicify a path to directory, what you want to clear")
	return parser


def clear_dir(path):
	for file in os.listdir(path):
    		file_path = os.path.join(path, file)
    		try:
        		if os.path.isfile(file_path):
            			os.unlink(file_path)
				print("File was removed: {file}".format(file=file_path))
        		elif os.path.isdir(file_path): 
				shutil.rmtree(file_path)
				print("Directory was removed: {dir}".format(dir=file_path))
    		except Exception as ex:
        		print("Couldn't delete {file} because {ex}".format(file=file_path, ex=ex))


if __name__ == "__main__":
	args = create_parser().parse_args()
	clear_dir(args.path)
