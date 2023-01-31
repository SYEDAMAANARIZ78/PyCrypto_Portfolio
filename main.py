from tkinter import *
from PIL import ImageTk, Image
import requests
import json 

PyCrypto = Tk()
 
#Frame = Frame(PyCrypto, width= 200, height= 100)
#Frame.pack()
#Frame.place(anchor='center', relx =0.5, rely = 0.5)
#img = ImageTk.PhotoImage(Image.open("poertfolio.jpg"))
#label = Label(Frame, image=img)
#label.pack()


PyCrypto.title("Crypto Portfolio")
PyCrypto.iconbitmap('favicon.ico')

def font_color(amount):
    if amount >= 0:
        return "green"
    else:
        return "red"

def portfolio():
    
    api_request = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=5000&convert=USD&CMC_PRO_API_KEY=7d50433b-780d-4983-aac8-017de02c03bc")

    api = json.loads(api_request.content)

    print("----------------")
    print("----------------")
 
    coins = [
            {
            "symbol":"BTC",
            "amount_owned": 20,
            "price_per_coin": 3200,  
            },
            {
            "symbol":"ETH",
            "amount_owned": 1000,
            "price_per_coin": 2200,  
            },
            {
            "symbol":"USTD",
            "amount_owned": 100,
            "price_per_coin": 200,  
            },
            {
            "symbol":"BNB",
            "amount_owned": 50,
            "price_per_coin": 208,  
            },
            {
            "symbol":"USDC",
            "amount_owned": 90,
            "price_per_coin": 10,  
            },
            {
            "symbol":"XRP",
            "amount_owned": 500,
            "price_per_coin": 15,  
            },
            {
            "symbol":"BUSD",
            "amount_owned": 250,
            "price_per_coin": 70,  
            },
            {
            "symbol":"ADA",
            "amount_owned": 700,
            "price_per_coin": 20,  
            },   
        ]

    total_pl = 0
    coin_row = 1
    total_curr_val = 0
    
    for i in range(0,300):
        for coin in coins:
            if api["data"][i]["symbol"] == coin["symbol"]:
                  total_paid = coin["amount_owned"] * coin["price_per_coin"]
                  current_value = coin["amount_owned"] * api["data"][i]["quote"]["USD"]["price"]
                  pl_percoin = api["data"][i]["quote"]["USD"]["price"] - coin["price_per_coin"]
                  total_pl_coin = pl_percoin * coin["amount_owned"]
      
                  total_pl = total_pl + total_pl_coin
                  total_curr_val = total_curr_val + current_value
              
                  name = Label(PyCrypto, text=api["data"][i]["symbol"], bg="#F3F4F6", fg="black",font="Lato 12", padx="2",pady="2",borderwidth="2",relief="groove")
                  name.grid(row=coin_row,column=0,sticky=N+S+E+W)

                  price = Label(PyCrypto, text="${0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]), bg="#F3F4F6", fg="black",font="Lato 12", padx="2",pady="2",borderwidth="2",relief="groove")
                  price.grid(row=coin_row,column=1,sticky=N+S+E+W)

                  no_coins = Label(PyCrypto, text=coin["amount_owned"], bg="#F3F4F6", fg="black",font="Lato 12", padx="2",pady="2",borderwidth="2",relief="groove")
                  no_coins.grid(row=coin_row,column=2,sticky=N+S+E+W)

                  amount_paid = Label(PyCrypto, text="${0:.2f}".format(total_paid), bg="#F3F4F6", fg="black",font="Lato 12", padx="2",pady="2",borderwidth="2",relief="groove")
                  amount_paid.grid(row=coin_row,column=3,sticky=N+S+E+W)

                  current_val = Label(PyCrypto, text="${0:.2f}".format(current_value), bg="#F3F4F6", fg=font_color(float("{0:.2f}".format(current_value))),font="Lato 12", padx="2",pady="2",borderwidth="2",relief="groove")
                  current_val.grid(row=coin_row,column=4,sticky=N+S+E+W)

                  pl_coin = Label(PyCrypto, text="${0:.2f}".format(pl_percoin), bg="#F3F4F6", fg=font_color(float("{0:.2f}".format(pl_percoin))),font="Lato 12", padx="2",pady="2",borderwidth="2",relief="groove")
                  pl_coin.grid(row=coin_row,column=5,sticky=N+S+E+W)

                  totalpl = Label(PyCrypto, text="${0:.2f}".format(total_pl_coin), bg="#F3F4F6", fg=font_color(float("{0:.2f}".format(total_pl_coin))),font="Lato 12", padx="2",pady="2",borderwidth="2",relief="groove")
                  totalpl.grid(row=coin_row,column=6,sticky=N+S+E+W)
              
                  coin_row = coin_row + 1
                  
    totalpl = Label(PyCrypto, text="${0:.2f}".format(total_pl), bg="#F3F4F6", fg=font_color(float("{0:.2f}".format(total_pl))),font="Lato 12", padx="2",pady="2",borderwidth="2",relief="groove")
    totalpl.grid(row=coin_row,column=6,sticky=N+S+E+W)
    
    totalcv = Label(PyCrypto, text="${0:.2f}".format(total_curr_val), bg="#F3F4F6", fg="black",font="Lato 12", padx="2",pady="2",borderwidth="2",relief="groove")
    totalcv.grid(row=coin_row,column=4,sticky=N+S+E+W)
    
    update = Button(PyCrypto, text="Update", bg="#201B9E", fg="white",command = portfolio,font="Lato 12", padx="2",pady="2",borderwidth="2",relief="groove")
    update.grid(row=coin_row + 1,column=6,sticky=N+S+E+W)
    
    api = ""
    
name = Label(PyCrypto, text="Coin Name", bg="#201B9E", fg="#FFFFFF", font="Merriweather 12 bold", padx="5",pady="5",borderwidth="2",relief="raised")
name.grid(row=0,column=0,sticky=N+S+E+W)

price = Label(PyCrypto, text="  Price  ", bg="#201B9E", fg="#FFFFFF", font="Merriweather 12 bold", padx="5",pady="5",borderwidth="2",relief="raised")
price.grid(row=0,column=1,sticky=N+S+E+W)

no_coins = Label(PyCrypto, text="Coin Owned", bg="#201B9E", fg="#FFFFFF", font="Merriweather 12 bold", padx="5",pady="5",borderwidth="2",relief="raised")
no_coins.grid(row=0,column=2,sticky=N+S+E+W)

amount_paid = Label(PyCrypto, text="Total Amount Paid", bg="#201B9E", fg="#FFFFFF", font="Merriweather 12 bold", padx="5",pady="5",borderwidth="2",relief="raised")
amount_paid.grid(row=0,column=3,sticky=N+S+E+W)

current_val = Label(PyCrypto, text="Current Value", bg="#201B9E", fg="#FFFFFF", font="Merriweather 12 bold", padx="5",pady="5",borderwidth="2",relief="raised")
current_val.grid(row=0,column=4,sticky=N+S+E+W)

pl_coin = Label(PyCrypto, text="P/L Per Coin", bg="#201B9E", fg="#FFFFFF", font="Merriweather 12 bold", padx="5",pady="5",borderwidth="2",relief="raised")
pl_coin.grid(row=0,column=5,sticky=N+S+E+W)

totalpl = Label(PyCrypto, text="Total P/L with Coin", bg="#201B9E", fg="#FFFFFF", font="Merriweather 12 bold", padx="5",pady="5",borderwidth="2",relief="raised")
totalpl.grid(row=0,column=6,sticky=N+S+E+W)

portfolio()

PyCrypto.mainloop()
print("Program Completed")