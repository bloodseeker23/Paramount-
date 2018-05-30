from tkinter import * 
import time
import random

root=Tk()
root.geometry("1300x750+0+0")
root.title("TOF")

text_input = StringVar()
operator=""




Tops = Frame(root, width=1600,height=50, bg = "powder blue" ,relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width=800,height=700 ,relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width=300,height=700,relief=SUNKEN)
f2.pack(side=RIGHT)

###################time ############################
localtime = time.asctime(time.localtime(time.time()))

############# Info ##############################
lblInfo = Label(Tops, font=('arial',50,'bold'),text="Paramount Intercontinental Pvt Ltd.",fg="Steel Blue",bd=10,anchor='w')
lblInfo.grid(row=0,column=0)
lblInfo = Label(Tops, font=('arial',20,'bold'),text=localtime,fg="Steel Blue",bd=10,anchor='w')
lblInfo.grid(row=1,column=0)

#################about########################

ABOUT_TEXT = """About
Paramount Intercontinental Pvt Ltd.

To calculate thickness of foam you need to enter Dew point,Ambient Temp,Operating temp,Thermal conductivity and Surface Coeff.

To calculate Dew point you need to enter ambient Temp and relative humidity.

To calculate Relative Humidity you need to enter dew point and ambient temp.

To calculate Ambient Temp you need to enter relative humidity and dew point.

For more support email to "kjayesh2302@gmail.com"

****DEVELOPER : Jayesh kedar****

"""

########### Calculator ##########################
def click_abt():
    toplevel = Toplevel()
    label1 = Label(toplevel, text=ABOUT_TEXT, height=0, width=100)
    label1.pack()

    
def btnClick(num):
    global operator
    operator=operator+str(num)
    text_input.set(operator)

def btnClear():
    global operator
    operator =""
    text_input.set("")

def equal():
    global operator
    sumup = str(eval(operator))
    operator =sumup
    text_input.set(sumup)

def calc_dew():
    corf=float(service.get())
    coMq=float(meal.get())

    dew_t=float(((corf/100)**0.125)*(112+0.9*coMq)+(0.1*coMq-112))
    rand.set(dew_t)
def calc_RH():
    cor=float(rand.get())
    coM=float(meal.get())

    RH=float(100*((112-0.1*coM+cor)/(112+0.9*coM))**8)

    service.set(RH)

def calc_AT():
    corf=float(service.get())
    cor=float(rand.get())

    AT=float((cor-112*((corf/100)**0.125)+112)/(0.9*((corf/100)**0.125)+0.1))

    meal.set(AT)
    
def getRef():
    

    cor=float(rand.get())
    cof=float(fries.get())
    com=float(maggie.get())
    coc=float(coffee.get())
    coM=float(meal.get())
    
    
    N_a=float(cor-cof)
    D_a=float(coM-cor)
    j=float(N_a/D_a)
    k=float(j*com)
    p=float((k/coc)*1000)
    tww=int((0.2*p)+p)
    total_cost=float((k/coc)*1000)
    total.set(total_cost)
    GST.set(tww)



def qExit():
    root.destroy()

def reset():
    rand.set("")
    fries.set("")
    maggie.set("")
    coffee.set("")
    meal.set("")
    service.set("")
    total.set("")
    GST.set("")


###################################################################
"""   
txtDisplay = Entry(f2, font=('arial',20,'bold'), textvariable=text_input,bd=30, insertwidth=4, justify='right',bg = "powder blue")
txtDisplay.grid(columnspan=5)

btn1=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
             text="1",bg="powder blue",command = lambda:btnClick(1)).grid(row=1,column=0)
btn2=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
             text="2",bg="powder blue",command = lambda:btnClick(2)).grid(row=1,column=1)
btn3=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
             text="3",bg="powder blue",command = lambda:btnClick(3)).grid(row=1,column=2)
btn4=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
             text="4",bg="powder blue",command = lambda:btnClick(4)).grid(row=2,column=0)


btn5=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
             text="5",bg="powder blue",command = lambda:btnClick(5)).grid(row=2,column=1)
btn6=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
             text="6",bg="powder blue",command = lambda:btnClick(6)).grid(row=2,column=2)

btn7=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
             text="7",bg="powder blue",command = lambda:btnClick(7)).grid(row=3,column=0)

btn8=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
             text="8",bg="powder blue",command = lambda:btnClick(8)).grid(row=3,column=1)
btn9=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
             text="9",bg="powder blue",command = lambda:btnClick(9)).grid(row=3,column=2)
btn0=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
             text="0",bg="powder blue",command = lambda:btnClick(0)).grid(row=4,column=0)


Addition=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
             text="+",bg="powder blue",command = lambda:btnClick("+")).grid(row=1,column=3)
Subtraction=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
             text="-",bg="powder blue",command = lambda:btnClick("-")).grid(row=2,column=3)
multiplication=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
             text="*",bg="powder blue",command = lambda:btnClick("*")).grid(row=3,column=3)
division=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
             text="/",bg="powder blue",command = lambda:btnClick("/")).grid(row=4,column=3)

Equal=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
             text="=",bg="powder blue",command = lambda:equal()).grid(row=4,column=1)
Clear=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
             text="C",bg="powder blue",command = lambda:btnClear()).grid(row=4,column=2)


"""
###########################################################
rand = StringVar()
fries= StringVar()
maggie=StringVar()
coffee=StringVar()
meal=StringVar()




lblReference = Label(f1,font=('arial',16,'bold'),text="Dew Point(C)",bd=16, anchor='w').grid(row=0,column=0)
txtRef= Entry(f1,font=('arial',16,'bold'),textvariable=rand,bd=10,insertwidth=4, justify="right").grid(row=0,column=1)

lblFries = Label(f1,font=('arial',16,'bold'),text="Operating Temperature(C)",bd=16, anchor='w').grid(row=1,column=0)
lblFries = Entry(f1,font=('arial',16,'bold'),textvariable=fries,bd=10,insertwidth=4, justify="right").grid(row=1,column=1)


lblMeal = Label(f1,font=('arial',16,'bold'),text="Ambient Temperature(C)",bd=16, anchor='w').grid(row=2,column=0)
txtMeal= Entry(f1,font=('arial',16,'bold'),textvariable=meal,bd=10,insertwidth=4, justify="right").grid(row=2,column=1)

lblMaggie = Label(f1,font=('arial',16,'bold'),text="Thermal Conductivity(w/mk)",bd=16, anchor='w').grid(row=3,column=0)
txtMaggie= Entry(f1,font=('arial',16,'bold'),textvariable=maggie,bd=10,insertwidth=4,justify="right").grid(row=3,column=1)

lblCoffee = Label(f1,font=('arial',16,'bold'),text="Surface Coff.(w/m^2K)",bd=16, anchor='w').grid(row=4,column=0)
txtCoffee= Entry(f1,font=('arial',16,'bold'),textvariable=coffee,bd=10,insertwidth=4, justify="right").grid(row=4,column=1)


##########################################################
service=StringVar()
total=StringVar()
GST=StringVar()

lblMaggieQ = Label(f1,font=('arial',16,'bold'),text="Relative humidity(%)",bd=16, anchor='w').grid(row=1,column=2)
txtMaggieQ= Entry(f1,font=('arial',16,'bold'),textvariable=service,bd=10,insertwidth=4,justify="right").grid(row=1,column=3)

lblMaggie = Label(f1,font=('arial',16,'bold'),text="margin_safety(20%)",bd=16, anchor='w').grid(row=2,column=2)
txtMaggie= Entry(f1,font=('arial',16,'bold'),textvariable=GST,bd=10,insertwidth=4,justify="right").grid(row=2,column=3)

lblMaggie = Label(f1,font=('arial',16,'bold'),text="Thickness(mm)",bd=16, anchor='w').grid(row=3,column=2)
txtMaggie= Entry(f1,font=('arial',16,'bold'),textvariable=total,bd=10,insertwidth=4,justify="right").grid(row=3,column=3)

lblMaggie1 = Label(f1,font=('arial',16,'bold'),text="Devloped by: kjayesh2302@gmail.com",bd=16, anchor='s').grid(row=10,column=3)
#############################################################
Reset=Button(f1,padx=8,pady=8,bd=8,fg="black",font=('arial',20,'bold'),width=10,
             text="Reset",bg="powder blue",command = lambda:reset()).grid(row=5,column=1)

Total=Button(f1,padx=8,pady=8,bd=8,fg="black",font=('arial',20,'bold'),width=10,
             text="Calc",bg="powder blue",command = lambda:getRef()).grid(row=5,column=2)

Exit=Button(f1,padx=8,pady=8,bd=8,fg="black",font=('arial',20,'bold'),width=10,
             text="Exit",bg="powder blue",command = lambda:qExit()).grid(row=5,column=3)

calc_d=Button(f1,padx=8,pady=8,bd=8,fg="black",font=('arial',20,'bold'),width=16,
             text="Calc Dew Point",bg="powder blue",command = lambda:calc_dew()).grid(row=6,column=1)

calc_R=Button(f1,padx=8,pady=8,bd=8,fg="black",font=('arial',20,'bold'),width=17,
             text="Calc Relative Humidity",bg="powder blue",command = lambda:calc_RH()).grid(row=6,column=2)

calc_A=Button(f1,padx=8,pady=8,bd=8,fg="black",font=('arial',20,'bold'),width=16,
             text="Calc Ambient Temp",bg="powder blue",command = lambda:calc_AT()).grid(row=6,column=3)

button1 = Button(f1, text="INFO.",font=('arial',20,'bold'), width=20, command=click_abt).grid(row=7,column=3)



root.mainloop()

