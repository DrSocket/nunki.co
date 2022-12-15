import requests
from torrequest import TorRequest

def requestTor(port):
	payload = {
		"token": "zc9M7jMyI0VbCK1XdHVLsg",
		"data": {
		"name": "nameFirst",
		"email": "internetEmail",
		"phone": "phoneHome",
		"_repeat": 1
		}
	}

	# Create a TorRequest instance
	tr = TorRequest(proxy_port=port, password='VeryEasy2@')

	# Set the URL of the mocked API on fakejson
	url = 'https://app.fakejson.com/q'

	# getCurrentIp(tr)
	iptest = tr.get('http://ipecho.net/plain')
	print (f'Fake TOR Ip: {iptest.text}')

	# Use the tor requests module to make a HTTPS request to the API
	response = tr.post(url, json = payload)

	# Print the response from the API
	print(response.text)

	# Reset the Tor identity
	tr.reset_identity()

if __name__ == "__main__":
	iptest = requests.get('http://ipecho.net/plain')
	print (f'Original Ip: {iptest.text}')
	torPorts = [9050]
	while 1:
		for port in torPorts:
			requestTor(port)