from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("fever report")
root.geometry("400x400")

q1=Label(root,text="do you have headache and sore throat")
q1.place(relx=0.5,rely=0.1,anchor=CENTER)

q1rb=StringVar(value="0")
q1r1=Radiobutton(root,text="yes",variable=q1rb,value="yes")
q1r1.place(relx=0.3,rely=0.2,anchor=CENTER)

q1r2=Radiobutton(root,text="no",variable=q1rb,value="no")
q1r2.place(relx=0.6,rely=0.2,anchor=CENTER)

q2=Label(root,text="is your body temperature high")
q2.place(relx=0.5,rely=0.4,anchor=CENTER)

q2rb=StringVar(value="0")
q2r1=Radiobutton(root,text="yes",variable=q2rb,value="yes")
q2r1.place(relx=0.3,rely=0.5,anchor=CENTER)

q2r2=Radiobutton(root,text="no",variable=q2rb,value="no")
q2r2.place(relx=0.6,rely=0.5,anchor=CENTER)


q3=Label(root,text="are there any symptoms of eye redness")
q3.place(relx=0.5,rely=0.7,anchor=CENTER)

q3rb=StringVar(value="0")
q3r1=Radiobutton(root,text="yes",variable=q3rb,value="yes")
q3r1.place(relx=0.3,rely=0.8,anchor=CENTER)

q3r2=Radiobutton(root,text="no",value="no",variable=q3rb)
q3r2.place(relx=0.6,rely=0.8,anchor=CENTER)

def score():
    s=0
    if(q1rb.get()=="yes"):
        s=s+20
    if(q2rb.get()=="yes"):
        s=s+20
    if(q3rb.get()=="yes"):
        s=s+20
        
    if(s<=20):
        messagebox.showinfo("report","you do not need to visit doctor")
    elif(s>20  and s<=40):
        messagebox.showinfo("report","you need to take precaution")
    else:
        messagebox.showwarning("report","you must go to the doctor")
    

btn=Button(root,text="click to show",command=score)
btn.place(relx=0.5,rely=0.9,anchor=CENTER)


root.mainloop()