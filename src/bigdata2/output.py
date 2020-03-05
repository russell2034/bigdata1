import json
def get_output(output,data):
	if output=='print':
		for m in data:
			print(m,'\n')
	else:
		try:
			with open(output, 'a') as newfile:
				for m in data:
					newfile.write(json.dumps(m)+'\n')
		except:
			if output =='':
				print('Please specify your output')
