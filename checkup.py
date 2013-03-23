#!/usr/bin/env python3
import json
import urllib.request
from urllib.error import *
from socket import timeout

# methods
def check_all_sites():
	all_sites = get_all_sites()
	failed_sites = []
	
	for site in all_sites:
		status = check_site(site)
		
		if (not(status['up'])):
			failed_sites.append({
				'site': site,
				'failed_urls': status['failed_urls']
			})
	
	if (len(failed_sites) > 0):
		print('Some sites are down:')
		
		for site in failed_sites:
			print("\t{} ({}/{} URLs failed)".format(site['site']['title'], len(site['failed_urls']), len(site['site']['urls'])))
	else:
		print('All sites were up.')


def get_all_sites():
	file = open('sites.json')
	return json.load(file)

def check_site(site):
	print("Now checking site {}...".format(site['title']))
	failed_urls = []
	
	for url in site['urls']:
		print("\tChecking: {}...".format(url), end = '')
		
		if (url_up(url)):
			print("up!")
		else:
			print("down!")
			failed_urls.append(url)
	
	if (len(failed_urls) > 0):
		return {
			'up': False,
			'failed_urls': failed_urls
		}
	else:
		return {'up': True}

def url_up(url):
	try: 
		urllib.request.urlopen(url, None, 10)
	except (HTTPError) as error: # soft error
		return False
	except (URLError) as error: # hard error
		return False
	except (timeout, IOError):
		return False
	else:
		return True

def alert_site_down(urls, site):
	print("")
	
# main program
check_all_sites()
