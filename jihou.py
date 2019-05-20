#!/usr/bin/env python3

import os
import time
from datetime import datetime
import sys
import math
import random
import threading

meigen = ["隣の客は、良く、柿食う客だ。","すいへいりーべ、ぶくの船、ななまがり、しっぷす、くらーくか","天は人の上に人を造らず、人の下に人を造らず","天才は、99％の努力と、1％のひらめきである。トーマス・エジソン"]

def seconds(sH,sM,sS):
	h = int(sH)
	m = int(sM)
	s = int(sS)

	return (h * 60 * 60 + m * 60 + s)



done = -1
hhhh = []
mmmm = []
ssss = []
tttt = []
jihou = []
for ii in range(1,25):
	hhhh += [("0"+str(ii))[-2:]]
	mmmm += ["00"]
	ssss += ["00"]
	jihou += [True]
	if ii == 12:
		tttt += ["               えええーと。ラズパイが、正午をお知らせします。"]
	elif ii == 25:
		tttt += ["えええええええと。ラズパイが、真夜中をお知らせします。"]
#	elif ii == 6:
#		tttt += ["えええええええええと。おはようございます。六時になりました。起きる時間です。"+meigen[math.floor(random.random()*3)]]
	else:
		tttt += ["         えーーーーと。ラズパイが"+str(ii)+"時を、お知らせします。"]
flag = False
while True:
	try:
		hh = datetime.now().strftime("%H")			
		mm = datetime.now().strftime("%M")			
		ss = datetime.now().strftime("%S")			
		for ii in range(len(hhhh)):
			now = seconds(hh,mm,ss)
			purpose = seconds(hhhh[ii],mmmm[ii],ssss[ii])
			if now  < (purpose - 5):
				if now > (purpose - 10):
					if done != ii:
						done = ii
						os.system('/home/pi/src/aquestalkpi/AquesTalkPi {} | aplay'.format(tttt[ii]))
						if jihou[ii]:
							count=0
							ps = ["57","58","59","00"]
							while True:
								ss = datetime.now().strftime("%S")			
								if ss == ps[count]:
									if ps[count] == "00":
										th = threading.Thread(target=os.system('/home/pi/src/aquestalkpi/AquesTalkPi {} | aplay'.format("　　　　　　ポーーーーーン")),name="poon",args=())
										th.start()
									else:
										th = threading.Thread(target=os.system('/home/pi/src/aquestalkpi/AquesTalkPi {} | aplay'.format("　　　　　　ポ")),name="po",args=())
										th.start()
									count += 1
									if count > (len(ps)-1):
										flag = True
										break
								


		if flag:
			break
		else:
			time.sleep(0.1)

	except KeyboardInterrupt:
		break

