import csv
from urllib.parse import quote
import pandas as pd
from twilio.rest import Client

msg_list = []
price_range = {"electric%20guitar": "20-150", "bass": "50-200", "amplifier":"0-80"}

def send_message(info, to_number):
    account_sid = 'AC4edaa4f9768eb268b7907e9c2680d55d'
    auth_token = 'd410ace8a2f8e51a3ab05bf7ceabec88'
    client = Client(account_sid, auth_token)

    message = client.messages \
    .create(
    body=f"{info}",
    from_='+13852501338',
    to=to_number
    )
    print('Text message sent successfully')
    
keywords = []
with open('./keywords.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        keywords.append(quote(row[0]).replace(" ","%20"))

for keyword in keywords:
    print (keyword)
    file_name = keyword+'.csv'
    df = pd.read_csv(file_name)
    views_mean = df["views"].mean()
    #print ("views mean", views_mean)
    favorites_mean = df["favorites"].mean()
    #print ("favorites mean", favorites_mean)
    ratio_views_favorites = views_mean/favorites_mean
    #print ("ratio views favorites", ratio_views_favorites)
    price_sum = 0
    count = 0
    for i, j in df.iterrows():
        try:
            #print (j["price"])
            price_sum += float(j["price"][1:].replace(",",""))
            count += 1
            #print(i, j)
        except:
            print ()
            #print (j["price"])
    #print (price_sum)
    #price_mean = price_sum/len(df.index)
    price_mean = price_sum/count
    #print (price_mean)

    start = int(price_range[keyword].split("-")[0])
    end = int(price_range[keyword].split("-")[1])

    print (start, end)
    
    for i, j in df.iterrows():
        if(j["favorites"]!=0):
            try:
                item_price = float(j["price"][1:].replace(",",""))
                if(j["views"]/j["favorites"] > ratio_views_favorites and item_price < price_mean and item_price>start and item_price<end):
                    #print ("Price is good")
                    offer = item_price*0.7
                    offer = int(round(offer/5.0)*5.0)
                    #print (item_price, offer)
                    text = "Hey, " + j["sellerName"] + " Do you still have the " + j["url"] + " ? Could you do " + str(offer) + "?"
                    print (text)
                    print ("Price is Good")
                    print ()
                    to_number = j["sellerPhone"].replace("-","")
                    if (text not in msg_list):
                        msg_list.append(text)
                        #print (to_number)
                        #send_message(text, to_number)
            except:
                #print (j["price"])
                print ()
    
    
