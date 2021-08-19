import unittest
from unittest.mock import patch
from bs4 import BeautifulSoup
import requests
from scraper import WollPlatz

woll = WollPlatz('https://www.wollplatz.de/')

class Tests(unittest.TestCase):
  
  def test_price(self):
    ## Test Price Of Item 1
    getter = requests.get(f"https://www.wollplatz.de/suche.html?s=DMC%20Natura%20XL").text
    soup = BeautifulSoup(getter, 'lxml')
    result1 = woll.getPrice(soup)
    self.assertEqual(result1, '€ 7,92')

    ## Test Price of Item 2
    getter = requests.get(f"https://www.wollplatz.de/suche.html?s=Drops%20Safran").text
    soup = BeautifulSoup(getter, 'lxml')
    result2 = woll.getPrice(soup)
    self.assertEqual(result2, '€ 1,39')

    ## Test Price of Item 3
    getter = requests.get(f'https://www.wollplatz.de/suche.html?s=Drops%20Baby%20Merino%20Mix').text
    soup = BeautifulSoup(getter, 'lxml')
    result3 = woll.getPrice(soup)
    self.assertEqual(result3, '€ 3,10')
  
  def test_delivery(self):

    ## Test Delivery Time of item 1
    getter = requests.get(f"https://www.wollplatz.de/suche.html?s=DMC%20Natura%20XL").text
    soup = BeautifulSoup(getter, 'lxml') 
    result1 = woll.getDeliveryTime(soup)
    self.assertEqual(result1, '14 Tage Widerrufsrecht\r\n')

    ## Test Delivery Time of item 2
    getter = requests.get(f"https://www.wollplatz.de/suche.html?s=Drops%20Baby%20Merino%20Mix").text
    soup = BeautifulSoup(getter, 'lxml') 
    result2 = woll.getDeliveryTime(soup)
    self.assertIsNot(result2, '14 Tage Widerrufsrecht')
  
  def test_needleSize(self):
    ## Test Needle Size of item 1
    getter = requests.get(f"https://www.wollplatz.de/suche.html?s=DMC%20Natura%20XL").text
    soup = BeautifulSoup(getter, 'lxml') 
    result1 = woll.getNeedleSize(soup)
    self.assertEqual(result1, '8 mm')

    ## Test Needle Size of item 2
    getter = requests.get(f"https://www.wollplatz.de/suche.html?s=Drops%20Baby%20Merino%20Mix").text
    soup = BeautifulSoup(getter, 'lxml') 
    result2 = woll.getNeedleSize(soup)
    self.assertIsNot(result2, '5 mm')

  def test_composition(self):
    ## Test Composition of item 1
    getter = requests.get(f"https://www.wollplatz.de/suche.html?s=DMC%20Natura%20XL").text
    soup = BeautifulSoup(getter, 'lxml') 
    result1 = woll.getComposition(soup)
    self.assertEqual(result1, '100% Baumwolle')

    ## Test Composition of item 3
    getter = requests.get(f"https://www.wollplatz.de/suche.html?s=Drops%20Baby%20Merino%20Mix").text
    soup = BeautifulSoup(getter, 'lxml') 
    result2 = woll.getComposition(soup)
    self.assertEqual(result2, '100% Merinowolle')


if __name__ == '__main__':
  unittest.main()