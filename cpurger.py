#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import argparse
import os
import glob

# Defualt path
dir_path = os.path.dirname(os.path.realpath(__file__))

def create_parser ():
    parser = argparse.ArgumentParser(description='Tool for revoming useless files')
    parser.add_argument('file_types', metavar='T', type=str, nargs='+', help='Types of files for the removing')
    parser.add_argument ('-s', '--show', action='store_true', help='Show information')
    parser.add_argument ('-r', '--recursion', action='store_true', help='Enable recursion')
    parser.add_argument ('-p', '--path', nargs='?', default=dir_path, help='Path to search')
    parser.add_argument ('-f', '--force', action='store_true', help='Disable confirmation')
    return parser

def get_files(types, recurse, dir_path):
	files = []
	try:
		if recurse:
			for type_search in types:
				files.extend(glob.glob(dir_path+'/**/*.'+type_search, recursive=True))
		else:
			for type_search in types:
				files.extend(glob.glob(dir_path+'/*.'+type_search))
	except Exception as e:
		raise
		sys.exit()
	return files

def smart_purge(file_types, show=False, recursion=False, path=dir_path, force=True):
	files=get_files(file_types, recursion, path)

	if len(files) == 0:
		print("Not found")
		return

	if show:
		print("Found files in", dir_path)
		for file_type in namespace.file_types:
			files_filtered = [x for x in files if (x.endswith('.'+file_type))]
			print('\t' + file_type + ':', len(files_filtered))

	if force:
		for file in files:
			os.remove(file)
		print('Successful', len(files), 'was deleted')
	else:
		if input('Deletion '+str(len(files))+' files. Are you sure? [Y/N] ').upper() != 'N':
			for file in files:
				os.remove(file)
			print('Successful', len(files), 'files was deleted')
		else:
			print('Operation was canceled')

def smart_purge_muted(file_types, path=dir_path, recursion=False):

	files=get_files(file_types, recursion, path)

	if len(files) == 0:
		return

	for file in files:
		os.remove(file)

if __name__ == "__main__":
	parser = create_parser()
	namespace = parser.parse_args(sys.argv[1:])
	smart_purge(namespace.file_types, namespace.show, namespace.recursion, namespace.path, namespace.force)