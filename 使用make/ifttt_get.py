
import time
import network
import urequests as requests

ssid = 'Robert_iPhone'
password = '0926656000'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

#等待連線或失敗
#status=0,1,2正在連線
#status=3連線成功
#<1,>=3失敗的連線

max_wait = 10
send = True

while max_wait > 0:
    status = wlan.status()
    if status < 0 or status >= 3:
        break
    max_wait -= 1
    print("等待連線")
    time.sleep(1)

#處理錯誤
if wlan.status() != 3:
    raise RuntimeError('連線失敗')
else:
    print('連線成功')
    status = wlan.ifconfig()
    print(f'ip={status[0]}')

# urequests官方網址
# https://makeblock-micropython-api.readthedocs.io/en/latest/public_library/Third-party-libraries/urequests.html

while True:
    #取得sensor的資料  
    url = 'https://maker.ifttt.com/trigger/receive_notify/with/key/eDqcZfqY_i_BHCZVXCwb6aq7GLPKpdV4q1ePja35Mjq?value1=90&value2=100&value3=110'
    
    #使用try/except傳送資料
    
    if(send):
        send = False
        print("送出資料")
        try:
            response = requests.request('GET',url)
        except:
            print(f"無法連線({wlan.status()})")
            if wlan.status() < 0 or wlan.status() > 3:
                print("嘗試重新連線")
                wlan.disconnect()
                wlan.connect(ssid, password)
                if wlan.status() == 3:
                    print("連線成功")
                else:
                    print("連線失敗")
        else:
            print("server接收") #但要檢查status_code,是否回應成功
            if response.status_code == 200:
                print("成功傳送,status_code==200")
            else:
                print("server回應有問題")
                print(f'status_code:{response.status_code}')
        finally:
            response.close()
            
    
        
        
    time.sleep(10)
 
 
 


