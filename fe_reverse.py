from urllib import response
import requests
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By

## with Firefox() as driver comment/uncomment
# from selenium.webdriver.firefox.service import Service
# from selenium.webdriver.firefox.options import Options
# from webdriver_manager.firefox import GeckoDriverManager

# with Chrome() as driver comment/uncomment
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


from bs4 import BeautifulSoup
import re
import json

def get_selenium():
	options = Options()
	# options.page_load_strategy = 'normal'
	options.add_argument("--headless")
	options.add_argument("--blink-settings=imagesEnabled=false")
	options.add_argument("--no-sandbox")
	# options.add_argument("--disable-dev-shm-usage")

	## Firefox driver comment/uncomment
	# driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)

	# Chrome driver comment/uncomment
	driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

	return (driver)

class BoardReader:
	def __init__(self, keyword=None, date=None, language=None, limit=None):
		self.keyword = keyword or ""
		self.date = date or 365
		self.language = language or "English"
		self.limit = limit or 10

	# Create url
	def create_url(self):
		base = "https://boardreader.com/return.php?query="
		for i, e in enumerate(self.keyword):
			base += e
			if i < len(self.keyword) - 1:
				base += "%20"
		if int(self.limit) != 10:
			base += f"&limit={self.limit};"
		if int(self.date) != 365:
			base += f"&period={self.date};"
		if self.language != "English":
			base += f"&language={self.language};"
		base += f"&session_id={self.get_session_id()}"
		return (base)

	def get_session_id(self):
		response = requests.get("https://boardreader.com/")
		if response.ok and response is not None:
			# pattern = re.compile(r'\.setItem\("([^@]+@[^@]+\.[^@]+)"\);', re.MULTILINE | re.DOTALL)
			soup = BeautifulSoup(response.text, "html.parser")
			script_tag = soup.findAll("script")
			for e in script_tag[8]:
				index = e.find("localStorage.setItem('currentSessionId'")
				if index > 0:
					id = e[index + 42:index + 97]
					return (id)
		else:
			print("Error: ", response.status_code)
			return (None)

	def readable(self, str):
		res = str.replace('[Keyword]', '')
		res = res.replace('[/Keyword]', '')
		res = res.replace('&quot', '"')
		res = res.replace('&amp', '&')
		res = res.replace('&lt', '<')
		res = res.replace('&gt', '>')
		res = res.replace('&nbsp', ' ')
		res = res.replace('&apos', "'")
		res = res.replace('&#039;s', "'s")
		return (res)

	# Print response
	def get_response(self):
		response = requests.get(self.create_url())
		if response.ok and response is not None:
			try:
				r = response.json()
				r = r['SearchResults']
				for i, e in enumerate(r):
					print(f"Article {i + 1}")
					print (r)
					# print (type(e['Subject']))
					print (f"Subject: {self.readable(e['Subject'])}")
					print (f"Thread Title: {self.readable(e['ThreadTitle'])}")
					print (f"{self.readable(e['Text'])}")
			except Exception as e:
				print(e)
		else:
			print("Error: ", response.status_code)

if __name__ == "__main__":
	if (len(sys.argv) > 1):
		bReader = BoardReader()
		if (len(sys.argv) > 1):
			bReader.keyword = sys.argv[1].split(" ")
		if (len(sys.argv) > 2):
			bReader.date = sys.argv[2]
		if (len(sys.argv) > 3):
			bReader.language = sys.argv[3]
		if (len(sys.argv) > 4):
			bReader.limit = sys.argv[4]
		bReader.get_response()
	else:
		print("No arguments provided")
		print("Usage: python3 fe_reverse.py <keywords (If more than 1 please add quotes)> optional: <period: (default: 365)> <language (default: English)> <limit>")
		sys.exit(1)