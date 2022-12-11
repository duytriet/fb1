#Code By Khánh Sky and Lộc Wibu
#Lấy Code Nhớ Ghi Nguồn 2 Coder Hộ!!
import requests
import time
import threading
import sys,os
s = requests.Session()
payload = {
	'username': " ",
	'password': " ",
}
r = s.post('http://pagepro.xyz/dang-nhap', data=payload).headers
cookie = r['set-cookie'].split("[")[0].split('; ')[0]
class Main:
	def buff():
		headers = {
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'Accept-Encoding': 'gzip, deflate',
			'Accept-Language': 'en-US,en;q=0.9',
			'Cache-Control': 'max-age=0',
			'Connection': 'keep-alive',
			'Cookie':  cookie,
			'Host': 'pagepro.xyz',
			'Upgrade-Insecure-Requests': '1',
			'User-Agent': 'My User Agent 1.0',
			}
		response = s.get('https://pagepro.xyz/apivippro/index.php?id=47', headers=headers)
		print(response.json())
	def run():
        	threa = 10
        	while True:
            		t = threading.Thread(target=Main.buff)
            		t.start()
            		while threading.active_count() > threa:                       
                		t.join()
if __name__ == "__main__":
	Main.run()
