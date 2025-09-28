from tkinter import *
import speedtest

sp = Tk()
sp.title("speedtest")
sp.geometry("500x500")
sp.config(bg="pink")

def speedcheck():
	st = speedtest.Speedtest()
	st.get_servers()
	down = str(round(st.download()/(10**6),2))+"Mbps"
	up = str(round(st.upload()/(10**6),2))+"Mbps"
	lab_down.config(text=down)
	lab_up.config(text = up)


lab = Label(sp, text="Speed test",bg="white")
lab.place(x=50,y=40,height="50",width="380")

lab = Label(sp, text="Download",bg="white")
lab.place(x=50,y=100,height="50",width="380")

lab_down = Label(sp, text="00",bg="white",fg="red")
lab_down.place(x=50,y=160,height="50",width="380")

lab = Label(sp, text="Upload",bg="white")
lab.place(x=50,y=220,height=50,width=380)

lab_up = Label(sp, text="00",bg="white",fg="red")
lab_up.place(x=50,y=280, height=50,width=380)

button = Button(sp, text="Check Speed",bg="red" , command=speedcheck)
button.place(x=50,y=350, height=50,width=380)


sp.mainloop()