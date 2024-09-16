from tkinter import *
from gpiozero import LED

#initializing the GPIO pins to the three leds
led1 = LED(17)
led2 = LED(18)
led3 = LED(16)

#Tk method for window initialization
window = Tk(className='LED CONTROL')

#setting the geometery of the window
window.geometry('800x500')
#minimizing the sizie of the window for 800X500 dimension
window.minsize(800,500)
#the exit buttom using lambda expression for adding multiple functions in the command
button=Button(window, text='EXIT',background="#808080",fg="#202020",command=lambda:[window.destroy(),led1.close(),led2.close(),led3.close()])
button.pack(side=BOTTOM)
#label widget for showing instruction
Label(window,text="SELECT THE RADIO BUTTON TO MAKE THE LED GLOW",font='raelway').pack(side=TOP,pady=50)
#variable to store the radio button answers
radar = IntVar()

#functions for on off of light on different cases
def ledON1():
    led1.on()
    led2.off()
    led3.off()
    
def ledON2():
    led2.on()
    led1.off()
    led3.off()
    
def ledON4():
    led3.on()
    led1.off()
    led2.off()
    
#radio button to control the led here pack method is for location setting and display of Led
radio1 = Radiobutton(window,text='Red',variable=radar,value=1,background = "#A42222", command = ledON1).pack(fill = X, ipady = 5)
radio2 = Radiobutton(window,text='Green',variable=radar,value=2,background = "#4C9900", command = ledON2).pack(fill = X, ipady = 5)
radio3 = Radiobutton(window,text='Blue',variable=radar,value=3,background = "#004C99",command = ledON4).pack(fill = X, ipady = 5)

#mainloop to run the aboce functioning till a end request is generated
window.mainloop()