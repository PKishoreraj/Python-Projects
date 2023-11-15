from Tkinter import *
from PLI import ImageTk,Image
import pytz
import time
root=Tk()
root.geomentry("600x450")
clock_image=ImageTk,PhotoImage(Image.open("clock.jpg"))
India_label=Label(root,text="India")
India_label.place(relx=0.2,rely=0.85,anchor=CENTER)
India_clock=Label(root)
India_clock["image"]=clock_image
India_clock.place(relx=0.2,rely=0.35,anchor=CENTER)
india_time=Label(root)
india_time.place(relx=0.2,rely=0.65,anchor=CENTER)
usa_label=Label(root,text="USA")
usa_label.place(relx=0.7,rely=0.05,anchor=CENTER)
usa_clock=Label(root)
usa_clock["image"]=clock_image
usa.place(relx=0.7,rely=0.65,anchor=CENTER)
usa=time=label(root)
usa_time.place(relx=0.7,rely=0.65,anchor=CENTER)
class India():
    def times(self):
        home=pytz.timezone('Aisa/Kolkata')
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S")
        india_time["text"]="Time:"+current_time
        india_time.after(200,self.times)
class USA():
        home=pytz.timezone('US/Central')
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S")
        usa_time["text"]="Time:"+current_time
        usa_time.after(200,self.times)
obj_india=India()
obj_usa=USA()
India_btn=Button(root,text="show time",command=obj_india.times)
India_btn.place(relx=0.2,rely=0.8,anchor=CENTER)
usa_btn=Button(root,text="show time",command=obj_usa.times)
usa_btn.place(relx=0.7,rely=0.8,anchor=CENTER)
clock_image=ImageTk,PhotoImage(Image.open("clock.jpg"))
India_label=Label(root,text="India")
India_label.place(relx=0.2,rely=0.85,anchor=CENTER)
India_clock=Label(root)
India_clock["image"]=clock_image
India_clock.place(relx=0.2,rely=0.35,anchor=CENTER)
india_time=Label(root)
india_time.place(relx=0.2,rely=0.65,anchor=CENTER)
usa_label=Label(root,text="USA")
usa_label.place(relx=0.7,rely=0.05,anchor=CENTER)
usa_clock=Label(root)
usa_clock["image"]=clock_image
usa.place(relx=0.7,rely=0.65,anchor=CENTER)
usa=time=label(root)
usa_time.place(relx=0.7,rely=0.65,anchor=CENTER)
class India():
    def times(self):
        home=pytz.timezone('Aisa/Kolkata')
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S")
        india_time["text"]="Time:"+current_time
        india_time.after(200,self.times)
class USA():
        home=pytz.timezone('US/Central')
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S")
        usa_time["text"]="Time:"+current_time
        usa_time.after(200,self.times)
obj_india=India()
obj_usa=USA()
India_btn=Button(root,text="show time",command=obj_india.times)
India_btn.place(relx=0.2,rely=0.8,anchor=CENTER)
usa_btn=Button(root,text="show time",command=obj_usa.times)
usa_btn.place(relx=0.7,rely=0.8,anchor=CENTER)
root.mainloop()