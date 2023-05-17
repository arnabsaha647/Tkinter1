from tkinter import *   #it is a python liberary
from tkinter import ttk   #for combobox   ttk=class


import requests    #requests modules(when we use any api in python project that time the "requests" module is needed)


def data_get(): #to get all information from api and put all data in variables
    city=city_name.get()
    #api(when we hit/target any api or url that time we use get function) (api name and api key)
    data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=5983c5ea6cbaa75948aeba66d4527a26").json()
    w_label1.config(text=data["weather"][0]["main"])
    wb_label1.config(text=data["weather"][0]["description"])
    tem_label1.config(text=str(int(data["main"]["temp"]-273.15)))   #-273.15 for convert temperature
    per_label1.config(text=data["main"]["pressure"])
    








win = Tk()
win.title("Weather Tech")
win.config(bg = "steelblue")
win.geometry("500x570")

name_label = Label(win,text='Weather App',font=('times new roman',30,'bold'))
name_label.place(x=25,y=50,height=50,width=450)

city_name=StringVar()

#combobox for show all list(states name) data
list_name=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com=ttk.Combobox(win,text='Weather App',values=list_name,font=('times new roman',20,'bold'),textvariable=city_name)
com.place(x=25,y=120,height=50,width=450)





w_label = Label(win,text='Weather Climate',font=('times new roman',20))
w_label.place(x=25,y=260,height=50,width=200)
w_label1 = Label(win,text='',font=('times new roman',20))
w_label1.place(x=250,y=260,height=50,width=200)



wb_label = Label(win,text='Weather Description',font=('times new roman',18))
wb_label.place(x=25,y=330,height=50,width=200)
wb_label1 = Label(win,text='',font=('times new roman',18))
wb_label1.place(x=250,y=330,height=50,width=200)



tem_label = Label(win,text='Temperature',font=('times new roman',20))
tem_label.place(x=25,y=400,height=50,width=200)
tem_label1 = Label(win,text='',font=('times new roman',20))
tem_label1.place(x=250,y=400,height=50,width=200)



per_label = Label(win,text='Pressure',font=('times new roman',20))
per_label.place(x=25,y=470,height=50,width=200)
per_label1 = Label(win,text='',font=('times new roman',20))
per_label1.place(x=250,y=470,height=50,width=200)


done_button=Button(win,text='Done',font=('times new roman',20,'bold'),command=data_get)
done_button.place(x=150,y=190,height=50,width=200)





win.mainloop
