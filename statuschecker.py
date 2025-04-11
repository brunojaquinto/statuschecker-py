import requests

def checkUrl(url, file):
	if not url.startswith('http://') and not url.startswith('https://'):
		url = 'http://' + url

	try:
		response = requests.get(url, timeout=5)

		if response.status_code == 200:
			file.write(f'{url} - 200 OK\n')
		elif response.status_code == 403:
			file.write(f'{url} - 403 Forbidden\n')
		else:
			pass

	except requests.exceptions.RequestException as e:
		print(f'{url} - Error: {e}')


def checkFile(file):
	with open(file, 'r') as f:
		urls = f.readlines()

	with open('status.txt', 'w') as status_file:
		for url in urls:
			url = url.strip()
			if url:
				checkUrl(url, status_file)

file_name = input('File: ')

checkFile(file_name)
