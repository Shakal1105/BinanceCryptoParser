from bs4 import BeautifulSoup
import requests
from tkinter import Tk, Label, Button, X, Y
from tkinter.ttk import Combobox

class Crypto():
    def __init__(self):
        #############parser#################
        self.url = "https://api.binance.com/api/v3/ticker/price"
        #############tkinter################
        self.row = 3
        self.name = ''
        self.price = ""
        self.oldnamecoin=None
        self.timer = -1
        self.prices = 25444
        self.prices = 0

        self.parserURL(button=0)
        self.tkinter()


    def parserURL(self, button):
        site = requests.get(self.url)
        soup = BeautifulSoup(site.text, "lxml")
        quotes = str(soup.find_all("p"))[15:-4]
        pops = ['{', '"', "}", ",", "[", "]", "symbol", "price"]
        for i in pops:
            quotes = quotes.replace(i, '').replace(":", "|")
        self.basa = quotes.split("|")
        self.countmax = len(self.basa)
        self.namebase = []
        for i in self.basa:
            self.num = self.basa.index(i)
            if self.num % 2 == 0:
                self.namebase.append(i)
            else:pass
        if button == 1:
            if self.scrollbar.get() in self.basa:
                self.oldpricecoin = self.scrollbar.get()
                self.index = self.basa.index(self.scrollbar.get())
                self.coinnames["text"] = self.basa[self.index]
                self.praicecoin["text"] = round(float(self.basa[self.index + 1]), 4)
                self.prices = round(float(self.basa[self.index + 1]), 4)
            else:
                self.coinnames["text"] = "ERROR"
                self.praicecoin["text"] = "ERROR"
        elif button == 2:
            if self.scrollbar.get() in self.basa:
                self.razniza = round(float(self.basa[self.index + 1]),4)- float(self.prices)
                if self.razniza >= 0.0:
                    self.index = self.basa.index(self.scrollbar.get())
                    self.praicecoin["text"] = f"{round(float(self.basa[self.index+1]), 4)}(+{round(self.razniza,2)})"
                    self.praicecoin["bg"] = "Green"
                elif self.razniza <= -0.1:
                    self.praicecoin["text"] = f"{round(float(self.basa[self.index+1]), 4)}({round(self.razniza, 2)})"
                    self.praicecoin["bg"] = "red"
                self.prices = round(float(self.basa[self.index+1]), 4)
            else:
                self.coinnames["text"] = "ERROR"
                self.praicecoin["text"] = "ERROR"

    def tkinter(self):
        self.window_crypto = Tk(screenName="Crypto")
        self.window_crypto.title("CryptoCoins")
        x= (self.window_crypto.winfo_screenwidth()-self.window_crypto.winfo_reqwidth())/2
        y= (self.window_crypto.winfo_screenheight() - self.window_crypto.winfo_reqheight())/2
        self.window_crypto.wm_geometry("+%d+%d" % (x,y))
        self.window_crypto.resizable(False, False)
        self.window_crypto.configure(bg="Black")

        Label(self.window_crypto,text="           Пошук крипто валюти на BINANCE           ".upper(), bg='black', fg="white").grid(column=1, row=1, columnspan=3)
        self.button_search = Button(self.window_crypto, text="Search", command=lambda: self.parserURL(button=1), bg="Yellow")
        self.button_search.grid(column=3, row=2)

        self.coinnames = Label(self.window_crypto, text=self.name, bg='black', fg="white")
        self.praicecoin = Label(self.window_crypto, text=self.price, bg='black', fg="white")
        self.button_update = Button(self.window_crypto, text="UPDATE", command=lambda: self.parserURL(button=2),bg='gray')
        self.button_update.grid(column=3, row=3)

        self.praicecoin.grid(column=2, row=self.row, padx=11)
        self.coinnames.grid(padx=30, column=1, row=self.row)

        self.scrollbar = Combobox(self.window_crypto, values=self.namebase, width=10)
        self.scrollbar.grid(padx=30, column=1, row=2)


        self.window_crypto.mainloop()

if __name__ == "__main__":
    Crypto()