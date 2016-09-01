#!/usr/bin/python

import requests
import re
from bs4 import BeautifulSoup
import random
import time
import os

def crawl_data(url, element, attr):
	r = requests.get(url)
	content = r.text
	soup = BeautifulSoup(content, 'html.parser')
	data = soup.find_all(element, attrs=attr)
	return data
	

#import pdb;pdb.set_trace()


def download_random_wallpaper():
	# visit web page with random wallpapers
	url = 'http://www.hdwallpapers.in/'
	data = crawl_data(url + 'random_wallpapers.html', 'div',{'class' : 'thumb'})
	wallpaper_link = random.choice(data).find('a').get('href')
	
	# visit wallpaper
	data = crawl_data(url + wallpaper_link, 'a', {'class' : 'wallpaper-thumb'})
	wallpaper_link = data.pop().get('href')
	r = requests.get(url + wallpaper_link)
	f = open('/home/ladakis/Pictures/background.jpg', 'wb')
	f.write(r.content)
	f.close	

if __name__ == "__main__":

	while (True):
		download_random_wallpaper()
		os.system("gsettings set org.gnome.desktop.background picture-uri \"file:///home/ladakis/Pictures/background.jpg\"")
		time.sleep(60)

