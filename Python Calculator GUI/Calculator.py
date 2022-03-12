from tkinter import*
import math

def btnClick(numbers):
    global operator
    operator += str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator = ""
    text_Input.set("")

def btnEqual():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""
    return sumup

def btnAns():
    global operator
    # a = btnEqual()
    text_Input.set("Ans")


cal = Tk()
blank_space = ""
cal.title(50* blank_space + "Calculator")
operator = ""
text_Input = StringVar()
cal.resizable(width=False, height=False)
cal.geometry("470x480+300+200")

# coverFrame = Frame(cal, bd=20, pady=2, relief=RIDGE)

textdisplay = Entry(cal, font= ('arial', 20, 'bold'), relief = RIDGE, textvariable = text_Input, bd=40,
                    insertwidth=4, bg='powder blue', justify ='right').grid(columnspan=4,)

btn7 = Button(cal, padx=10, bd=5, fg="black", font=('arial', 20, "bold"),text="7",command=lambda:btnClick(7)).grid(row=1, column=1)
btn8 = Button(cal, padx=10, bd=5, fg="black", font=('arial', 20, "bold"),text="8",command=lambda:btnClick(8)).grid(row=1, column=2)
btn9 = Button(cal, padx=10, bd=5, fg="black", font=('arial', 20, "bold"),text="9",command=lambda:btnClick(9)).grid(row=1, column=3)

btn4 = Button(cal, padx=10, bd=5, fg="black", font=('arial', 20, "bold"),text="4",command=lambda:btnClick(4)).grid(row=2, column=1)
btn5 = Button(cal, padx=10, bd=5, fg="black", font=('arial', 20, "bold"),text="5",command=lambda:btnClick(5)).grid(row=2, column=2)
btn6 = Button(cal, padx=10, bd=5, fg="black", font=('arial', 20, "bold"),text="6",command=lambda:btnClick(6)).grid(row=2, column=3)

btn1 = Button(cal, padx=10, bd=5, fg="black", font=('arial', 20, "bold"),text="1",command=lambda:btnClick(1)).grid(row=3, column=1)
btn2 = Button(cal, padx=10, bd=5, fg="black", font=('arial', 20, "bold"),text="2",command=lambda:btnClick(2)).grid(row=3, column=2)
btn3 = Button(cal, padx=10, bd=5, fg="black", font=('arial', 20, "bold"),text="3",command=lambda:btnClick(3)).grid(row=3, column=3)

btn0 = Button(cal, padx=10,pady=10, bd=5, fg="black", font=('arial', 20, "bold"),text="0",command=lambda:btnClick(0)).grid(row=4, column=1)
btn_equal = Button(cal, padx=10,pady=10, bd=5, fg="black", font=('arial', 20, "bold"),text="=",command=btnEqual).grid(row=4, column=2)
btnClear = Button(cal, padx=10,pady=10, bd=5, fg="black", font=('arial', 20, "bold"),text="C",command=btnClearDisplay).grid(row=4, column=3)
# btn00 = Button(cal, padx=10,pady=10, bd=5, fg="black", font=('arial', 20, "bold"),text="00",command=lambda:btnClick(00)).grid(row=5, column=1)
# btnDec = Button(cal, padx=10,pady=10, bd=5, fg="black", font=('arial', 20, "bold"),text=".",).grid(row=5, column=2)
# btnAns = Button(cal, padx=1,pady=10, bd=5, fg="black", font=('arial', 20, "bold"),text="Ans",command=btnAns).grid(row=5, column=3)

btn_add = Button(cal, padx=10, bd=5, fg="black", font=('arial', 20, "bold"),text="+",command=lambda:btnClick("+")).grid(row=1, column=4)
btn_sub = Button(cal, padx=10, bd=5, fg="black", font=('arial', 20, "bold"),text="-",command=lambda:btnClick("-")).grid(row=2, column=4)
btn_multi = Button(cal, padx=10, bd=5, fg="black", font=('arial', 20, "bold"),text="*",command=lambda:btnClick("*")).grid(row=3, column=4)
btn_div = Button(cal, padx=10,pady=16, bd=5, fg="black", font=('arial', 20, "bold"),text="/",command=lambda:btnClick("/")).grid(row=4, column=4)


cal.mainloop()

