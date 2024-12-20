import scapy.all as scapy
import requests
import time
import json

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    clients_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list

def post_to_sheet(clients_list, url):
    # 全クライアントデータをJSON形式で送信
    data = json.dumps({'clients': clients_list})
    headers = {'Content-Type': 'application/json'}  # JSON形式であることを指定
    try:
        response = requests.post(url, data=data, headers=headers)
        print(response.text)
    except requests.exceptions.RequestException as e:
        print("HTTP Request failed: {}".format(e))

def main():
    url = 'https://script.google.com/macros/s/AKfycbw8ELPS1hr05mcC8n_5lVssYIS5Z2BbP4xGDqICWA5wAWrfJQLbbNbX8RIop2dEvc6VYw/exec'  # ここにGoogle Apps ScriptのWebアプリURLを入れる
    print("Scanning...")
    clients_list = scan("192.168.0.1/24") 
    print(clients_list)
    print("send") # ローカルネットワークの範囲を指定
    post_to_sheet(clients_list,url)
       
if __name__ == "__main__":
    main()
