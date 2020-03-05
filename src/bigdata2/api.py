from sodapy import Socrata
from src.bigdata2.output import get_output

def data_get(APP_KEY,page_size,num_pages,output):
	client = Socrata('data.cityofnewyork.us', APP_KEY)
	if num_pages== -1:
		nump=client.get('nc67-uf89',SELECT='COUNT(*)')/page_size
		for i in range(nump):
			data = client.get('nc67-uf89',limit = page_size, offset=i*page_size)
			get_output(output,data)
	else:
		with open(output, 'a') as newfile:			
			for i in range(num_pages):
				data = client.get('nc67-uf89',limit = page_size, offset=i*page_size)
				get_output(output,data)