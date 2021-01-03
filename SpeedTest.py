''' Short-Code to check your internet-speed. 
If you have some problems (on Mac) check out following stackoverflow-post: 
https://stackoverflow.com/questions/56326644/python-speedtest-facing-problems-with-certification-ssl-c1056'''

import speedtest
test = speedtest.Speedtest()
down = test.download()
upload = test.upload()

print(f'Download speed: {down}')
print(f'Uplaod speed: {upload}')
