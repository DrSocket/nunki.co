from urllib import response
import requests
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By

# with Firefox() as driver comment/uncomment
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
	
	# Firefox driver uncomment
	# driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)

	# Chrome driver uncomment
	driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

	return (driver)

def main():
	keyword = ""
	date = 365
	language = "English"
	limit = 10
	if (len(sys.argv) > 1):
		keyword = sys.argv[1]
	if (len(sys.argv) > 2):
		date = sys.argv[2]
	if (len(sys.argv) > 3):
		language = sys.argv[3]
	if (len(sys.argv) > 4):
		limit = sys.argv[4]

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
	if int(limit) != 10:
		base += f"limit={limit};"
	base += f"period={date};"
	base += f"language={language};"
	print (base)
	response = requests.get(base)
	if response.ok and response is not None:
		try:
			driver = get_selenium()
			driver.get(base)
			print (f"Title: {driver.title}")
			elements = driver.find_elements(By.TAG_NAME, "li")
			for i, e in enumerate(elements):
				print (f"*********Article {i + 1}*********")
				print (e.text)
				print ("\n\n")
				if i > 10:
					break
			driver.quit()
		except Exception as e:
			print(e)
	else:
		print("Error: ", response.status_code)

if __name__ == "__main__":
	if (len(sys.argv) > 1):
		seen = main()
	else:
		print("No arguments provided")
		print("Usage: python3 fe_reverse.py <keywords (If more than 1 please add quotes)> optional: <period: (default: 365)> <language (default: English) <limit>")
		sys.exit(1)