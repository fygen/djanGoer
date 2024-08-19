import subprocess
import sys
import time
import requests
import os
import pyfiglet
import base64
import json

def install_module(module):
    subprocess.check_call([sys.executable, "-m", "pip", "install", module])

def check_module(module):
    try:
        __import__(module)
        print(f"[✓] {module} modülü mevcut.")
    except ImportError:
        print(f"[!] {module} modülü bulunamadı. Yükleniyor...")
        install_module(module)

required_modules = ["requests", "pyfiglet"]

for module in required_modules:
    check_module(module)


print(pyfiglet.figlet_format("Dijvarhack"))

def load_data():
    data = """
    {
        "VP8": {
            "name": "Some Name",
            "age": 30,
            "location": "Some Location"
        }
    }
    """
    return json.loads(data)

data = load_data()
if "VP8" in data:
    print("[✓] @dijvarhack.")
    time.sleep(3)
else:
    print("[!] İzin verilmedi.")
    time.sleep(3)
    raise SystemExit()

os.system("clear")

telno = input("[+] Tel No Gir 0 olmadan: ")
password = input("[+] VF Şifren'i Gir: ")

headers = {
    "User-Agent": "VodafoneMCare/2308211432 CFNetwork/1325.0.1 Darwin/21.1.0",
    "Content-Length": "83",
    "Connection": "keep-alive",
    "Accept-Language": "tr_TR",
    "Accept-Encoding": "gzip, deflate, br",
    "Host": "m.vodafone.com.tr",
    "Cache-Control": "no-cache",
    "Accept": "*/*",
    "Content-Type": "application/x-www-form-urlencoded"
}

url = "https://m.vodafone.com.tr/maltgtwaycbu/api/"

data = {
    "context": "e30=",
    "username": telno,
    "method": "twoFactorAuthentication",
    "password": password
}

response = requests.post(url, headers=headers, data=data)
proid = response.json().get('process_id')
if proid is None:
    print("[x] Şifre veya Numara Yanlış")
    raise SystemExit()
else:
    print("[✓] Şifre Doğrulama Başarılı")

kod = input("[+] SMS ile Gelen Kodu Gir: ")

veri = {
    "langId": "tr_TR",
    "clientVersion": "17.2.5",
    "reportAdvId": "0AD98FF8-C8AB-465C-9235-DDE102D738B3",
    "pbmRight": "1",
    "rememberMe": "true",
    "sid": proid,
    "otpCode": kod,
    "platformName": "iPhone"
}

base64_veri = base64.b64encode(json.dumps(veri).encode('utf-8'))

data2 = {
    "context": base64_veri,
    "grant_type": "urn:vodafone:params:oauth:grant-type:two-factor",
    "code": kod,
    "method": "tokenUsing2FA",
    "process_id": proid,
    "scope": "ALL"
}

response2 = requests.post(url, headers=headers, data=data2)
sonuc2 = response2.json()

o_head = {
    "Accept": "application/json",
    "Language": "tr",
    "ApplicationType": "1",
    "ClientKey": "AC491770-B16A-4273-9CE7-CA790F63365E",
    "sid": proid,
    "Content-Type": "application/json",
    "Content-Length": "54",
    "Host": "m.vodafone.com.tr",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "User-Agent": "okhttp/4.10.0"
}

print("[✓] Giriş Yapıldı")
time.sleep(1)


while True:
    os.system("clear")
    print("[?] Hangi İşlemi Yapmak İstiyorsun: ")
    print("\n[1] 50GB Promo İnternet Al\n")
    sec = input("[#] Seçiminiz: ")
    if sec == "1":
        promo_url = "https://m.vodafone.com.tr/maltgtwaycbu/api/"
        print("[+] İnternet Yapılıyor Ayda 1 kere Yapılır")
        data3 = {
            'method': 'getNetworkPromo',
            'promoType': 'growth',
            'sid': proid
        }
        response_x = requests.post(promo_url, headers=headers, data=data3).json()
        sonuc = response_x.get("result")
        if sonuc == "SUCCESS":
            print("[+] 50GB İnternet Yapıldı")
        else:
            print("×", response_x.get("resultDesc", "Bilinmeyen bir hata oluştu"))
        time.sleep(3)
    else:
        print("[!] Geçersiz seçim, tekrar deneyin.")
        time.sleep(2)
