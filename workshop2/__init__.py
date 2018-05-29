import os
import argparse
import configparser
import sys

def run():
	parser = argparse.ArgumentParser(description='This is a test package')
	parser.add_argument('--display',help='Prints a statement',default='No display message')
	parser.add_argument('--config',help='Reads a config.ini file.',default=False)
	if len(sys.argv)==1: 
		parser.print_help()
		sys.exit(1)
	arg = parser.parse_args().display
	print arg
	print ("Hello World!")
	os.system("echo hello world in bash!")
	configfile = parser.parse_args().config
	if configfile != False:
		config = configparser.ConfigParser(interpolation = configparser.ExtendedInterpolation())
		config.read(configfile)
		for key in config: 
			for item in config[key]:
				print key, item, config[key][item]
	
