#!/usr/bin/env python3
#_*_ coding:utf-8 _*_

import subprocess 
import base64

result = subprocess.run('./AquesTalkPi "　　こんにちは"',shell=True,check=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=False)

print(base64.b64encode(result.stdout))
