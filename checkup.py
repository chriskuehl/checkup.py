#!/usr/bin/env python3
import json
import urllib.request

# methods
def check_all_sites():
	all_sites = get_all_sites()
	
	for site in all_sites:
		check_site(site)
			
def get_all_sites():
	file = open('sites.json')
	return json.load(file)

def check_site(site):
	print("Now checking site {}...".format(site['title']))
	
	for url in site['urls']:
		print("\tChecking: {}...".format(url), end = '')
		
		if (url_up(url)):
			print("up!")
		else:
			print("down!")

def url_up(url):
	urllib.request.urlretrieve(url)

# main program
check_all_sites()
