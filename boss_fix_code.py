import requests
import pandas as pd

def send_telegram_alert(lazy_employees_1):
    #standardized alert sending function . take a number  as input
    TOKEN = "8646167058:AAEYkAIe9YteGrMNKJ-1wOm82S8ef7uWTxE"
    
    CHAT_ID = "6297429333"
    
    #flexible message using input
    
    msg = f"Warn : Found {lazy_employees_1} lazy employees don't work"
    
    url_bot = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    
    pay_load = {"chat_id":CHAT_ID , "text":msg}
    
    response_bot = requests.post(url_bot , json=pay_load)
    
    if response_bot.status_code == 200:
        
        print("✅ Đã bắn báo cáo Telegram thành công!")
    
    else:
        
        print (f"❌ Cảnh báo thất bại! Lỗi máy chủ Telegram: {response_bot.status_code}")
if __name__ == "__main__":
    API_URL = "https://jsonplaceholder.typicode.com/todos"
    try:
        print("Craw Data")
        response =requests.get(API_URL)
        
        if response.status_code == 200:
            
            raw_data = response.json()
            
            data_frame = pd.DataFrame(raw_data)
        #filter lazy employees
            lazy_employees = data_frame[data_frame["completed"] == False]
            
            lazy_employees.to_csv("lazy_employees.csv",index= False)
            
            quantity = len(lazy_employees)
            print(f"total of Lazy employees {quantity}")
            #send to telegram 
            send_telegram_alert(quantity)
        else:
            print(f"Sever refuse connection API {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"capble international crash {e}")
        
        