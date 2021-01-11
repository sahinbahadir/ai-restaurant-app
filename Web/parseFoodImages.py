import requests
from bs4 import BeautifulSoup
import urllib.request
import json

url = 'https://www.yemeksepeti.com/ali-haydar-usta-bahcelievler-sirinevler-mah-istanbul'

html = requests.get(url).content
soup = BeautifulSoup(html, 'html.parser')

categories = soup.select('div[id*=menu_]')

final_dict = {'foods': [], 'categories': []}
csv_dict = {}

food_id = 1
c_id = 1
for cat in categories:
    cat_name = cat.find('h2').text
    if cat_name not in ['Kebaplar', 'Çorbalar', 'Başlangıçlar', 'Izgaralar', 'Dürümler', 'Pideler', 'İçecekler', 'Tatlılar']:
        continue
    products = cat.select('div[class=product]')
    final_dict['categories'].append({
        'id': c_id,
        'categoryName': cat_name,
        'seoURL': ''
    })

    csv_dict[cat_name] = []
    
    for product in products:
        try: 
            img_path = 'http:' + product.find('i').get('data-imagepath')
            img_name = img_path.split('/')[-1][:-8] + '.jpg'
            food_name = product.find_all('a')[-1].text

            if food_name != '  ':
                final_dict['foods'].append({
                    'id': food_id,
                    'categoryId': c_id,
                    'foodName': food_name,
                    'imagePath': img_name
                })

                csv_dict[cat_name].append(food_name)
                food_id += 1
                # urllib.request.urlretrieve(img_path, './images/' + img_name + '.jpg')
        except AttributeError:
            continue
    
    c_id += 1

print(csv_dict)
with open('db.json', 'w', encoding='utf-8') as f:
    json.dump(final_dict, f, ensure_ascii=False, indent=4)