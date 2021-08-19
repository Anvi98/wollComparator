from bs4 import BeautifulSoup
import requests
from brands import brands

class WollPlatz:
  def __init__(self, baseUrl):
      self.baseUrl = baseUrl
  
  # Check available brand on the website and returns among the base list, which brand is available on the website
  def checkBrands(self):
    brands_url = f'{self.baseUrl}wolle/herstellers'
    source = requests.get(brands_url).text
    soup = BeautifulSoup(source, 'lxml')

    present = []
    allBrands = []
    for brand in soup.find_all('h2', class_='productlist-title'):
      brandHtml = brand.a.text
      allBrands += [brandHtml]

    for brand in brands:
      if(brand in allBrands):
        present += [brand]
    return present
  
  # Take the list of available brands on the website and returns active links to access specific items
  def getUrlProducts(self, listBrand):
    self.listBrand = listBrand
    urls = []
    for brand in listBrand:
      extend = []
      if (type(brands[brand]) is str):
        o = brands[brand].split(' ')
        for i,word in enumerate(o):
          extend += ["%20"]
          extend += [o[i]]
        extend = ''.join(extend)
        url = f'https://www.wollplatz.de/suche.html?s={brand}{extend}'
        urls += [url]
      else:
        for i,word in enumerate(brands[brand]):
          o = brands[brand][i].split(' ')
          extend =[]
          for i,word in enumerate(o):
            extend += ["%20"]
            extend += [o[i]]
          extend = ''.join(extend)
          url = f'https://www.wollplatz.de/suche.html?s={brand}{extend}'
          urls += [url]

    return urls

  # get name of product
  def getName(self, soup):
    self.soup = soup
    name = soup.find('h1', id='pageheadertitle').text
    return name

  #get Image Link
  def getImage(self, soup):
    self.soup = soup
    img_url = soup.find('div', class_='pdetail-mainphotoholder pdetail-mainphotoholderleft').a['href'] 
    return img_url
  
  #get Price of product
  def getPrice(self, soup):
    self.soup = soup
    containPriceInfo = soup.find('span', class_='product-price')
    spanCurrency = containPriceInfo.find('span', class_='product-price-currency').text
    spanPrice = containPriceInfo.find('span', class_='product-price-amount').text
    totalPrice = spanCurrency + spanPrice
    
    return totalPrice
  
  #get Delivery time
  def getDeliveryTime(self, soup):
    self.soup = soup
    contain = soup.find('div', class_='innercmsuspholder')
    lis = []
    for li in contain.find_all('li'):
      lis += [li]

    return lis[2].text
  
  #get Needle size
  def getNeedleSize(self, soup):
    self.soup = soup
    details = soup.find('div', id='pdetailTableSpecs')
    tableDetails = details.find('table')
    trs = []
    for tr in tableDetails.find_all('tr'):
      trs += [tr]
    NeedlesInfo = trs[4]
    tds = []
    for td in NeedlesInfo.find_all('td'):
        tds += [td.text]

    return tds[1]

  #get Composition of product
  def getComposition(self, soup):
    self.soup = soup
    details = soup.find('div', id='pdetailTableSpecs')
    tableDetails = details.find('table')
    trs = []
    for tr in tableDetails.find_all('tr'):
      trs += [tr]
    CompositionInfo = trs[3]
    tds = []
    for td in CompositionInfo.find_all('td'):
        tds += [td.text]

    return tds[1]

  #get Needle Size Double Knit 
  def getNeedleDK(self, soup):
    details = soup.find('div', id='pdetailTableSpecs')
    tableDetails = details.find('table')
    trs = []
    for tr in tableDetails.find_all('tr'):
      trs += [tr]
    NeedlesInfo = trs[3]
    tds = []
    for td in NeedlesInfo.find_all('td'):
        tds += [td.text]
    return tds[1]
  
  #get Composition of product for Double Knit
  def getCompositionDK(self, soup):
    self.soup = soup
    details = soup.find('div', id='pdetailTableSpecs')
    tableDetails = details.find('table')
    trs = []
    for tr in tableDetails.find_all('tr'):
      trs += [tr]
    CompositionInfo = trs[2]
    tds = []
    for td in CompositionInfo.find_all('td'):
        tds += [td.text]

    return tds[1]    
  
  def getInfos(self, urls):
    listPrices = []
    listDeliveries = []
    listNeedlesSizes = []
    listCompostions = []
    listNames = []
    listImgs = []
    products = []

    for url in urls:
      getter = requests.get(url).text
      soup = BeautifulSoup(getter, 'lxml')
      if(url != urls[3] and url != urls[4]):

        listPrices = self.getPrice(soup)
        listDeliveries = self.getDeliveryTime(soup)
        listNeedlesSizes = self.getNeedleSize(soup)
        listCompostions = self.getComposition(soup)
        listNames = self.getName(soup)
        listImgs = self.getImage(soup)

        product = {
          "name": f"{listNames}",
          "price": f"{listPrices}",
          "delivery": f"{listDeliveries}",
          "needleSize": f"{listNeedlesSizes}",
          "composition": f"{listCompostions}",
          "image": f"{listImgs}"
        }
        products += [product]

      else:
        divs = []
        try:
          container = soup.find('div', class_= "productlist-mainholder")

          for div in container.find_all('div', class_="productlistholder productlist25"):
            divs += [div]
  
          special_url = divs[1].a['href']
          getter = requests.get(special_url).text
          soup = BeautifulSoup(getter, 'lxml')

          ## Get Price
          listPrices = self.getPrice(soup)

          ## Get Delivery Time
          listDeliveries =  self.getDeliveryTime(soup)

          ## Get Needles Infos Special_caseDK
          listNeedlesSizes = self.getNeedleDK(soup)

          ## Get Composition
          listCompostions = self.getCompositionDK(soup)

          ## Get Name of Products
          listNames = self.getName(soup)

          ## Get Image link
          listImgs = self.getImage(soup)

          product = {
            "name": f"{listNames}",
            "price": f"{listPrices}",
            "delivery": f"{listDeliveries}",
            "needleSize": f"{listNeedlesSizes}",
            "composition": f"{listCompostions}",
            "image": f"{listImgs}"
          }
          products += [product]        
        except Exception as e:
          pass
        
    return products