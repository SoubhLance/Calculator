import tkinter as tk
from math import *
from tkinter.messagebox import askyesno
import tkinter.messagebox as tmsg
import webbrowser


calculation=""


def add_to_calculation(symbol):
    global calculation
    calculation+=str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try: 
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)

    except:
        clear_field()
        text_result.insert(1.0, "Error")


def clear_field():
    global calculation
    calculation= ""
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)


def Confirm():
    ans=askyesno(title="Exit", message="Do you Want to Exit?" )
    if ans:
        root.destroy()

def about_me():
    tmsg.showinfo('About Project','This is a scientific Calculator created using Tkinter and python')

def send_feedback():
    ans = tmsg.askquestion('Feedback', 'Was your experience good with it?')
    if ans == 'yes':
        tmsg.showinfo('Feedback','Thanks for Your feedback')
    else:
        tmsg.showinfo('Feedback','Please Specify where it was wrong')
        tmsg.showinfo('Feedback','Email Me at studysadhu2022@gmail.com')
        webbrowser.open("www.gmail.com")




#GUI
root=tk.Tk()
root.geometry("612x400")
root.title("Calculator")
root.resizable(0,0)
root.configure(bg="light grey")


text_result= tk.Text(root,height=2,width=22,font=("Lucida 35 bold",24),relief="groove", fg='black', bg='white', borderwidth=5)
text_result.grid(columnspan=5)

#Menu
my_menu = tk.Menu(root)
m1 = tk.Menu(my_menu, tearoff=0, fg='blue')
m1.add_command(label = 'About Project', command = about_me)
m1.add_command(label = 'Send Feedback', command = send_feedback)
 
root.config(menu=my_menu)
my_menu.add_cascade(label='About', menu=m1)
my_menu.add_command(label='Exit', command=quit)


#Buttons
btn_1 = tk.Button(root,text="1", command=lambda: add_to_calculation(1), width=8, height=2, font=("Arial",14),foreground="black",background="sky blue")
btn_1.grid(row=2, column=0)
btn_2 = tk.Button(root,text="2", command=lambda: add_to_calculation(2), width=8, height=2, font=("Arial",14),foreground="black",background="sky blue")
btn_2.grid(row=2, column=1)
btn_3 = tk.Button(root,text="3", command=lambda: add_to_calculation(3), width=8, height=2, font=("Arial",14),foreground="black",background="sky blue")
btn_3.grid(row=2, column=2)
btn_4 = tk.Button(root,text="4", command=lambda: add_to_calculation(4), width=8, height=2, font=("Arial",14),foreground="black",background="sky blue")
btn_4.grid(row=3, column=0)
btn_5 = tk.Button(root,text="5", command=lambda: add_to_calculation(5), width=8, height=2, font=("Arial",14),foreground="black",background="sky blue")
btn_5.grid(row=3, column=1)
btn_6 = tk.Button(root,text="6", command=lambda: add_to_calculation(6), width=8, height=2, font=("Arial",14),foreground="black",background="sky blue")
btn_6.grid(row=3, column=2)
btn_7 = tk.Button(root,text="7", command=lambda: add_to_calculation(7), width=8, height=2, font=("Arial",14),foreground="black",background="sky blue")
btn_7.grid(row=4, column=0)
btn_8 = tk.Button(root,text="8", command=lambda: add_to_calculation(8), width=8, height=2, font=("Arial",14),foreground="black",background="sky blue")
btn_8.grid(row=4, column=1)
btn_9 = tk.Button(root,text="9", command=lambda: add_to_calculation(9), width=8, height=2, font=("Arial",14),foreground="black",background="sky blue")
btn_9.grid(row=4, column=2)
btn_0 = tk.Button(root,text="0", command=lambda: add_to_calculation(0), width=8, height=2, font=("Arial",14),padx=2,pady=6,foreground="black",background="sky blue")
btn_0.grid(row=5, column=1)
btn_plus = tk.Button(root,text="+", command=lambda: add_to_calculation("+"), width=8, height=2, font=("Arial",14),foreground="black",background="light blue")
btn_plus.grid(row=4,column=3)
btn_minus = tk.Button(root,text="-", command=lambda: add_to_calculation("-"), width=8, height=2, font=("Arial",14),foreground="black",background="light blue")
btn_minus.grid(row=3,column=3)
btn_mul = tk.Button(root,text="*", command=lambda: add_to_calculation("*"), width=8, height=2, font=("Arial",14),foreground="black",background="light blue")
btn_mul.grid(row=2,column=3)
btn_div = tk.Button(root,text="/", command=lambda: add_to_calculation("/"), width=8, height=2, font=("Arial",14),foreground="black",background="light blue")
btn_div.grid(row=1,column=3)
btn_open = tk.Button(root,text="(", command=lambda: add_to_calculation("("), width=8, height=2, font=("Arial",14),foreground="black",background="light blue")
btn_open.grid(row=1,column=1)
btn_dot = tk.Button(root,text=".", command=lambda: add_to_calculation("."), width=8, height=2, font=("Arial",14),padx=2,pady=6,foreground="black",background="grey")
btn_dot.grid(row=5,column=0)
btn_close = tk.Button(root,text=")", command=lambda: add_to_calculation(")"), width=8, height=2, font=("Arial",14),foreground="black",background="light blue")
btn_close.grid(row=1,column=2)
btn_equals = tk.Button(root,text="=", command=evaluate_calculation, width=17, height=2, font=("Arial",14),foreground="white",background="blue",relief="groove",padx=2,pady=6)
btn_equals.grid(row=5,column=2,columnspan=2)
btn_clear = tk.Button(root,text="C", command=clear_field, width=8, height=2, font=("Arial",14),foreground="white",background="red",relief="groove")
btn_clear.grid(row=1,column=0)
btn_exp= tk.Button(root,text="exp", command=lambda: add_to_calculation("**"), width=8, height=2, font=("Arial",14),foreground="black",background="light grey")
btn_exp.grid(row=4, column=6)
btn_per= tk.Button(root,text="%", command=lambda: add_to_calculation("*100"), width=8, height=2, font=("Arial",14),foreground="black",background="light grey")
btn_per.grid(row=4, column=5)
btn_sin= tk.Button(root,text="sin", command=lambda: add_to_calculation("sin"), width=8, height=2, font=("Arial",14),foreground="black",background="light grey")
btn_sin.grid(row=2, column=5)
btn_cos= tk.Button(root,text="cos", command=lambda: add_to_calculation("cos"), width=8, height=2, font=("Arial",14),foreground="black",background="light grey")
btn_cos.grid(row=3, column=5)
btn_tan= tk.Button(root,text="tan", command=lambda: add_to_calculation("tan"), width=8, height=2, font=("Arial",14),foreground="black",background="light grey")
btn_tan.grid(row=1, column=5)
btn_sin1= tk.Button(root,text="cosec", command=lambda: add_to_calculation("cosec"), width=8, height=2, font=("Arial",14),foreground="black",background="light grey")
btn_sin1.grid(row=2, column=6)
btn_cos1= tk.Button(root,text="sec", command=lambda: add_to_calculation("sec"), width=8, height=2, font=("Arial",14),foreground="black",background="light grey")
btn_cos1.grid(row=3, column=6)
btn_tan1= tk.Button(root,text="cot", command=lambda: add_to_calculation("cot"), width=8, height=2, font=("Arial",14),foreground="black",background="light grey")
btn_tan1.grid(row=1, column=6)
btn_log= tk.Button(root,text="log10", command=lambda: add_to_calculation("log"), width=8, height=2, font=("Arial",14),foreground="black",background="light grey",padx=2,pady=8)
btn_log.grid(row=0, column=5)
btn_sq= tk.Button(root,text="^2", command=lambda: add_to_calculation("**2"), width=8, height=2, font=("Arial",14),foreground="black",background="light grey",padx=2,pady=8)
btn_sq.grid(row=0, column=6)
btn_sqroot= tk.Button(root,text="√", command=lambda: add_to_calculation("**0.5"), width=8, height=2, font=("Arial",14),foreground="black",background="light grey",padx=2,pady=6)
btn_sqroot.grid(row=5, column=5)
btn_pi= tk.Button(root,text="π", command=lambda: add_to_calculation(3.14), width=8, height=2, font=("Arial",14),foreground="black",background="light grey",padx=2,pady=6)
btn_pi.grid(row=5, column=6)




root.protocol("WM_DELETE_WINDOW",Confirm)
root.mainloop()
