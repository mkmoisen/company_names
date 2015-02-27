#!/usr/bin/python

import random
from os.path import abspath, join, dirname

file_name = abspath(join(dirname(__file__), 'companynames.txt'))
companies = open(file_name).readlines()

#print "File = " + __file__

#companies = ['Cisco','Apple','Google']
email_hosts = ["".join(l for l in x[:-1] if l not in ' !@#$%^\'&*()[];:\|,.<>/?"') + '.com' for x in companies]

def get_name():
    return random.choice(companies)[:-1]

def get_email_host(company_name = None):
    return random.choice(email_hosts) if company_name is None else "".join(l for l in company_name if l not in ' !@#$%^&*()[];:\|,.<>/?"') + '.com'







'''
from bs4 import BeautifulSoup

#pip install beautifulsoup4


file=open('sandp500companytable.html')
soup=BeautifulSoup(file)
table = soup.find('table')
rows = table.findAll('tr')
companies = []
for i, row in enumerate(rows):
	if i:
		companies.append(row.findAll('td')[1](text=True)[0])


email_hosts = ["".join(l for l in x if l not in ' !@#$%^&*()[];:\|,.<>/?"') + '.com' for x in companies]

def get_full_name():
	return random.choice(companies)

def get_email_host():
	return random.choice(email_hosts)

def get_email_host(company_name=None):
    company_name = get_full_name if company_name is None else company_name
    return "".join([l for l in company_name if l not in ' !@#$%^&*()[];:\|,.<>/?"']) + '.com'


import random

def random_line():
    afile = open("companynames.txt")
    line = next(afile)
    for num, aline in enumerate(afile):
        if random.randrange(num + 2): continue 
        line = aline[:-1]
    return line
'''