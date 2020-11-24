import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

coursedeets = []

for x in range(1,25):
    url = 'https://mydentalcourse.com/search/?ct=111111111111111111111111111111111111&wf=11111&rm=11111&sd=2020-11-24&pge='
    url2 = '&items=20'
    r = requests.get(url + str(x)+ url2)

    soup = BeautifulSoup(r.content, 'html.parser')

    content = soup.find_all('div', class_='mdc_result_inner')

    for property in content: 
        provider = property.find('div', class_ = 'mdc_result_provider').text.strip()
        title = property.find('div', class_ = 'mdc_result_title').text.strip()
        price = property.find('div', class_ = 'mdc_result_reg').text.strip()
        date = property.find('div', class_ = 'mdc_result_dates').text.strip()
        Delivery_Method = property.find('div', class_ = 'mdc_result_city').text.strip()
        Loc = property.find('div', class_ = 'mdc_result_city').text.strip()
        creds = property.find('div', class_ = 'mdc_result_ce').text.strip()
        uncutdesc = soup.find_all('div', class_ = 'mdc_result_description')
        uncutwhofor = soup.find_all('div', class_ = 'mdc_result_whofor')
        uncutlink = soup.find_all('div', class_ = 'mdc_result_viewprovider')
        recurring = soup.find_all('div', class_ = 'mdc_repeat_bar')
        multiphase = soup.find_all('div', class_ = 'mdc_series_bar')

        if Delivery_Method.lower() == 'online':
            meth = 'Online'
        elif Delivery_Method.lower() == 'on-demand webinar':
            meth = 'On Demand Webinar'
        elif Delivery_Method.lower() == 'live webinar':
            meth = 'Live Webinar'
        else:
            meth = 'In Person'

        if Delivery_Method.lower() == 'online':
            Delivery = 1
        elif Delivery_Method.lower() == 'on-demand webinar':
            Delivery = 1
        elif Delivery_Method.lower() == 'live webinar':
            Delivery = 1
        else:
            Delivery = 0

        if Loc.lower() == 'online':
            Location = 'N/A'
        elif Loc.lower() == 'on-demand webinar':
            Location = 'N/A'
        elif Loc.lower() == 'live webinar':
            Location = 'N/A'
        else:
            Location = Loc

        for stonks in uncutdesc: 
            description = stonks.find('span').text.strip()
            category = stonks.find('div', class_ = 'mdc_result_coursetype')
    
        for stencil in uncutlink:
            nonlink = stencil.find('a', href = True)
            link = nonlink['href']

        for whodis in uncutwhofor:
            whofor = whodis.find('b').text

        property_info = {
            'Name': title,
            'Location': Location,
            'Provider': provider,
            'Subject': category,
            'Number of CE Credits': creds,
            'Short Description': description,
            'Price': price,
            'Whofor': whofor, 
            'Delivery Method': meth,
            'Online?': Delivery,
            'Recurring?': recurring,
            'Date': date,
            'Link': link,
            }
                
    coursedeets.append(property_info)

print(len(coursedeets))

df = pd.DataFrame(coursedeets)
    
print(df.head())

df.to_csv('test11.csv')
