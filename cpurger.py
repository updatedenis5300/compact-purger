#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import argparse
import os
import glob

dir_path = os.path.dirname(os.path.realpath(__file__))

def createParser ():
    parser = argparse.ArgumentParser(description='Tool for revoming useless files')
    parser.add_argument('file_types', metavar='T', type=str, nargs='+', help='Types of files for the removing')
    parser.add_argument ('-s', '--show', action='store_true', help='Show files')
    parser.add_argument ('-r', '--recursion', action='store_true', help='Enable recursion')
    parser.add_argument ('-p', '--path', nargs='?', default=dir_path, help='Path to search')
    parser.add_argument ('-f', '--force', action='store_true', help='Disable confirmation')
    return parser

def getFiles(types, recurse, dir_path):
	files = []
	try:
		if recurse:
			for type_search in types:
				files.extend(glob.glob(dir_path+'/**/*.'+type_search, recursive=True))
		else:
			for type_search in types:
				files.extend(glob.glob(dir_path+'/*.'+type_search))
	except Exception as e:
		print("Something is wrong, exception...")
		sys.exit()
	return files



def smartPurge(file_types, show=False, force=False, recursion=False, path=dir_path):

	files=getFiles(file_types, recursion, path)

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

if __name__ == "__main__":
	parser = createParser()
	namespace = parser.parse_args(sys.argv[1:])
	smartPurge(namespace.file_types, namespace.show, namespace.force, namespace.recursion, namespace.path)