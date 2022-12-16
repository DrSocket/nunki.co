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
		base = "https://boardreader.com/s/"
		if (len(self.keyword) > 1):
			for i, e in enumerate(self.keyword):
				base += f"{e}"
				if i < len(self.keyword) - 1:
					base += "%2520"
			base += ".html;"
		else:
			base += f"{self.keyword[0]}.html;"
		if int(self.limit) != 10:
			base += f"limit={self.limit};"
		base += f"period={self.date};"
		base += f"language={self.language};"
		return (base)

	# Print response
	def get_response(self):
		response = requests.get(self.create_url())
		if response.ok and response is not None:
			try:
				driver = get_selenium()
				driver.get(self.create_url())
				print (f"Title: {driver.title}\n")
				elements = driver.find_elements(By.TAG_NAME, "li")
				for i, e in enumerate(elements):
					print (f"*********Article {i + 1}*********")
					print (e.text)
					print ("\n\n")
				driver.quit()
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