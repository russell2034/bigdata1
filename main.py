import os
import argparse
from src.bigdata2.api import data_get

APP_KEY = os.environ['APP_KEY']
#  connect to  our  source
if __name__ == '__main__':
	# define parser to pass arguments for our function
	parser = argparse.ArgumentParser(description='Retrieving OCPV Data')
	parser.add_argument('--page_size',type = int, help = "Size of a page" )
	parser.add_argument('--num_pages', type = int, default= -1, help = 'Number of Pages')
	parser.add_argument('--output', type = str, default= 'print', help = 'Use only if you want to write in file. 4 print - leave out')
	args = parser.parse_args()

	data_get(APP_KEY,args.page_size,args.num_pages,args.output)