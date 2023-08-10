from tkinter import *
from tkinter import ttk
import requests

def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=81ac2177cc3574b6d3c02146c46a9dc6").json()
    c_label1.config(text=data["weather"][0]["main"])
    wd_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=(int(data["main"]["temp"]-273.15)))
    per_label1.config(text=data["main"]["pressure"])


win = Tk()
win.title("GlitcH.Weather")
win.config(bg = "purple")
win.geometry("570x570")

name_label = Label(win,text="GlitcH Weather App",
                   font=("Time New Roman",30,"bold"))
name_label.place(x=50,y=50,height=50,width=400)

city_name = StringVar()
list_name=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]

com = ttk.Combobox(win,text="GlitcH Weather App",values=list_name,
                   font=("Time New Roman",20,"bold"),textvariable=city_name)
com.place(x=25,y=110,height=50,width=450)

c_label = Label(win,text="Weather Climate",
                   font=("Time New Roman",20))
c_label.place(x=25,y=260,height=50,width=210)
c_label1 = Label(win,text=" ",
                   font=("Time New Roman",20))
c_label1.place(x=250,y=260,height=50,width=210)


wd_label = Label(win,text="Weather Description",
                   font=("Time New Roman",17))
wd_label.place(x=25,y=330,height=50,width=220)
wd_label1 = Label(win,text=" ",
                   font=("Time New Roman",18))
wd_label1.place(x=260,y=330,height=50,width=220)


temp_label = Label(win,text="Temperature",
                   font=("Time New Roman",20))
temp_label.place(x=25,y=400,height=50,width=200)
temp_label1 = Label(win,text=" ",
                   font=("Time New Roman",20))
temp_label1.place(x=250,y=400,height=50,width=200)


per_label = Label(win,text="Pressure",
                   font=("Time New Roman",20))
per_label.place(x=25,y=470,height=50,width=200)
per_label1 = Label(win,text=" ",
                   font=("Time New Roman",20))
per_label1.place(x=250,y=470,height=50,width=200)

submit_button = Button(win,text="Submit",
                   font=("Time New Roman",20,"bold"),command=data_get)
submit_button.place(x=200,y=190,height=50,width=110)


win.mainloop()