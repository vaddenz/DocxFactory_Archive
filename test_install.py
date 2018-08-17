#!/usr/bin/python3
# -*- coding: utf-8 -*-

try:
	from docxfactory import WordProcessingCompiler

except ImportError as e:
	print('\nDocxFactory python3 module WAS NOT installed correctly! Error:')
	print('-' * 30)
	print(e)
	print('-' * 30)
	print('TIPS: there might be something missing during DocxFactory installation,')
	print('      read the error msg above and install the missing dependencies.')
	print('      For example: you may be missing "libXext" library, install it by "yum install libXext".\n')

else:
	print('DocxFactory is successfully installed!')

try:
	compiler = WordProcessingCompiler.get_instance()
	
	compiler.compile(
		'/opt/DocxFactory/exercises/templates/top_level_items.docx',
		'/opt/DocxFactory/exercises/templates/top_level_items.dfw'
	)

	print('DocxFactory works as expected!\n')

except Exception as e:
	print('DocxFactory NOT work as expected. Error:')
	print('-' * 30)
	print(e)
	print('-' * 30)
	print('TIPS: you may need to read the DocxFactory tutorial manual for troubleshooting.\n')


