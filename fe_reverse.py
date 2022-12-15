from urllib import response
import requests
import scrapy
from bs4 import BeautifulSoup
import sys
from selenium import webdriver
import csv
import os
from selenium.webdriver.common.keys import Keys
import time

def get_selenium():
	options = webdriver.ChromeOptions()
	# options.add_argument('--headless')
	driver = webdriver.Chrome(options=options)
	return (driver)

def main():
	keyword = ""
	date = 365
	language = "English"
	if (len(sys.argv) > 1):
		keyword = sys.argv[1]
	if (len(sys.argv) > 2):
		date = sys.argv[2]
	if (len(sys.argv) > 3):
		language = sys.argv[3]

	keywords = keyword.split(" ")
	
	base = "https://boardreader.com/s/"
	if (len(keywords) > 1):
		for i, e in enumerate(keywords):
			base += f"{e}"
			if i < len(keywords) - 1:
				base += "%2520"
		base += ".html;"
	else:
		base += f"{keyword}.html;"
	if date:
		base += f"period={date};"
	if language:
		base += f"language={language};"
	print (base)
	response = requests.get(base)
	if response.ok and response is not None:
		driver = get_selenium()
		driver.get(base)
		print ("coucou")
		# w.until(EC.presence_of_element_located((By.CLASS_NAME, 'mdl-list')))
		# driver.execute_script("window.stop();")
		# print (driver.title)
		driver.quit()
		# options = Options()
		# options.add_argument("--headless")
		# options.headless = True
		# options.add_argument("start-maximized")
		# yield scrapy.Request(url=base, callback=parse)
		# driver.get("https://www.google.com")
		# chromeOptions = Options()
		# chromeOptions.headless = True
		# browser = webdriver.Chrome(executable_path="./driver/chromedriver", options=chromeOptions)
		# driver.get(base)
		# print("Title: %s" % driver.title)
		# driver.quit()
	# 	try:
	# 		html = BeautifulSoup(response.text, "html.parser")
	# 		# print(html.select(".mdl-list").text)
	# 		print (html.find_all('div', {'id': 'angular-content'}))
	# 		# for para in html.find_all("li", {"class": "mdl-list__item"}):
	# 			# print(para.text)
	# 	except Exception as e:
	# 		print(e)
	# else:
	# 	print("Error: ", response.status_code)
	# print(response.text)

if __name__ == "__main__":
	if (len(sys.argv) > 1):
		seen = main()
	else:
		print("No arguments provided")
		print("Usage: python3 fe_reverse.py <keywords (If more than 1 please add quotes)> optional: <period: (default: 365)> <language (default: English)>")
		sys.exit(1)