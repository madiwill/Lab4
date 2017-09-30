
import re


txt = open('mbox-short.txt')
num_lst = []
for line in txt:
	line = line.rstrip()
	if re.search('^From ([^ ]*)', line):
		
		vals = re.findall('[0-9]+', line)
		z= re.findall('\s([a-zA-Z0-9.]+)@',line)
		print(z)