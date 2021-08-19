from scraper import WollPlatz
import json


woll = WollPlatz('https://www.wollplatz.de/')
available_brands = woll.checkBrands()
urls = woll.getUrlProducts(available_brands)
print(urls)
pro = woll.getInfos(urls)
print(pro)

with open("products.json", "w", encoding='utf-8') as out_file:
    json.dump(pro, out_file, ensure_ascii=False, indent = 6) 

