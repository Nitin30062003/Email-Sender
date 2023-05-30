from tkinter import*
import smtplib
mailid=""
password=""
root=Tk()
root.geometry("400x270")
root.resizable(0,0)
root.title("Nitin's Mail Application")
l11=Label(root,text="Mail Application",font="Helvetica 25 bold").place(x=80,y=0)
l21=Label(root,text="From:").place(x=30,y=70)
e11=Entry(root,width="30")
e11.place(x=100,y=70)

l22=Label(root,text="Password:").place(x=30,y=100)
e12=Entry(root,width="30",show="*")
e12.place(x=100,y=100)

l2=Label(root,text="To:").place(x=30,y=130)
e1=Entry(root,width="30")
e1.place(x=100,y=130)
l3=Label(root,text="Message:").place(x=30,y=160)
e2=Entry(root,width="40")
e2.place(x=100,y=160)
l4=Label(root)
l4.place(x=30,y=190)
def sendemail():
    try:
        mailid=str(e11.get())
        password=str(e12.get())
        recipnt=str(e1.get())
        msg=str(e2.get())
        server=smtplib.SMTP('smtp.gmail.com',587)
        
        server.starttls()
        server.login(mailid,password)
        server.sendmail(mailid,recipnt,msg)
        server.quit()
        l4.configure(text="Email sent Succesfully",font="Helvetica 15 bold")
    except:    
        l4.configure(text="Email not sent, failed network",font="Helvetica 10 bold")
    
b1=Button(root,text="Send",command=sendemail,width="12").place(x=170,y=220)

root.mainloop()