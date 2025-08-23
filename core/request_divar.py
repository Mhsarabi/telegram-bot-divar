import requests
from bs4 import BeautifulSoup
import re


def get_products(query):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    url = f"https://divar.ir/s/tehran?q={query}"
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return None

    soup = BeautifulSoup(response.text, "html.parser")
    results = []

    items = soup.find_all("div", class_="kt-post-card__body")

    for item in items:
        title = item.find("h2", class_="kt-post-card__title")
        price = item.find("div", class_="kt-post-card__description")
        link_tag = item.find_parent("a")  
        
        if title and price and link_tag:
            link = "https://divar.ir" + link_tag['href']
            results.append(f"{title.text.strip()} - {price.text.strip()}\n🔗 {link}")

        if len(results) >= 3:
            break

    return results


def get_avg_price_from_divar(query):
    headers={
    "User-Agent":"Mozila/5.0"
    }

    url=f"https://divar.ir/s/tehran?q={query}"

    response=requests.get(url,headers=headers)

    if response.status_code != 200:
        return None
    
    soup=BeautifulSoup(response.text,"html.parser")

    price_list=[]

    items=soup.find_all("div",class_="kt-post-card__description")

    for item in items:
        text=item.text
        match=re.search(r'(\d[\d,]*)\s*تومان',text)
        if match:
            price_text=match.group(1).replace(",","")
            try:
               price=int(price_text)
               price_list.append(price)
            except:
                continue
            if len(price_list)>=20:
                break

            if not price_list:
                return None
            
            return round(sum(price_list)/len(price_list))