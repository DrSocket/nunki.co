from urllib import response
import requests
import sys
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

def get_selenium():
	fireFoxOptions = Options()
	fireFoxOptions.add_argument("--headless")
	fireFoxOptions.binary = "./geckodriver"
	# fireFoxOptions.set_headless()
	driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=fireFoxOptions)
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
		try:
			driver = get_selenium()
			driver.get(base)
			print (driver.title)
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
		seen = main()
	else:
		print("No arguments provided")
		print("Usage: python3 fe_reverse.py <keywords (If more than 1 please add quotes)> optional: <period: (default: 365)> <language (default: English)>")
		sys.exit(1)