from bs4 import BeautifulSoup
import lxml, requests, json

headers = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.124 YaBrowser/22.9.4.863 Yowser/2.5 Safari/537.36'
}

url = 'https://tnt-online.ru/series'
response = requests.get(url, headers=headers)
src = response.text

all_serials = {}

serials = BeautifulSoup(src, 'lxml').find('div', class_='serials_box').find_all('a')
for serial in serials:
    
    serial_url = serial.get('href')
    res = requests.get(serial_url, headers=headers)
    src_serial = res.text
    try:
        kolvo = BeautifulSoup(src_serial, 'lxml').find(class_='kolvo').text
    except:
        kolvo = 'no information'
    serial_text = serial.text.strip() + '(' +kolvo + ')'
    all_serials[serial_text] = serial_url

with open('all_serials.json', 'w') as file:
    json.dump(all_serials, file, indent=4, ensure_ascii=False)