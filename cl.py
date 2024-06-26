from tkinter import *
import sys
import requests
import html5lib
import bs4

root = Tk()
root.title("Web-Scrapping-Tool")
root.geometry('645x400')
root.config(background='black')
def scrapping():
    url = requests.get(URL.get())
    res = bs4.BeautifulSoup(url.text,"html.parser")

    savefile1 = open("Web_Text.txt",'a')
    for i in res.select('p'):
        savefile1.write(i.getText())
    savefile1.close()

    savefile2 = open("Web_CODE.txt",'a')
    for i in res.select('p'):
        savefile2.write(res.prettify())
    savefile2.close()

var = StringVar()
var.set("WEBSITE SCRAPPER TOOL")

Label_of_Web = Label(root, textvariable=var,bd=8,bg='black',fg='#0096DC',font=("Helvetica",35)).grid(row=0,column=0)
URL= StringVar()
E1 = Entry(root,bd=5,font=7,textvariable=URL).grid(row=2,column=0,ipadx=100)
button = Button(root,text='Scrap it!!!',bd=5,command = scrapping).grid(row=4,column=0,padx=8,pady=4)
root.mainloop()