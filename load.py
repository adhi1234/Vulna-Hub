import requests
import re
import sys,time



def load_nvd():
	r = requests.get('https://nvd.nist.gov/vuln/data-feeds#JSON_FEED')
	for filename in re.findall("nvdcve-1.0-[0-9]*\.json\.zip",r.text):
		print(filename)
		r_file = requests.get("https://static.nvd.nist.gov/feeds/json/cve/1.0/" + filename, stream=True)
		with open("nvd/" + filename, 'wb') as f:
			for chunk in r_file:
				f.write(chunk)

def loadingAnimation():

	animation = "|/-\\"

	for i in range(100):
		time.sleep(0.1)
		sys.stdout.write("\r" + animation[i % len(animation)])
		sys.stdout.flush()
		
	print("Receiving data feeds")


