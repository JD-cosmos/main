#==========map+++++++++++
# 
# #multiply numbers using map ?
from itertools import accumulate


my_list = [1, 2, 3, 4, 5]
my_new_list = [i * i for i in my_list]

print(my_new_list)
# using lambda
my_new_list = map(lambda x: x * x, my_list)

print(my_new_list)

# Using the map function
def multiply(i):
 return i * i

x = map(multiply, (3, 5, 7, 11, 13))
print(list(x))

#==============find length using map=====
example = ["Welcome", "to", "Sem 3"]
x = list(map(len, example))
print(x)

#==========Map with lambda
num = (6, 9, 21, 44)
resu = map(lambda i: i + i, num)
print(list(resu))

# map with tupple   convert in upper case+++
def example(s):
 return s.upper()
tuple_exm = ('this','is','map')
upd_tup = map(example, tuple_exm)
print(tuple(upd_tup))

#=======map with dictionary++

car_dict ={'a': 'Mercedes-Benz', 'b': 'BMW', 'c': 'Ferrari', 'd': 'Lamborghini', 'e': 'Jeep'}
# adding an '_' to the end of each value
car_dict = dict(map(lambda x: (x[0], x[1] + '_'), car_dict.items() ))
print('The modified dictionary is : ')
print(car_dict)

#========== map with set+========
def example(i):
 return i%3
set_exm = {33, 102, 62, 96, 44, 28, 227}
upd_itms = map(example, set_exm) # divisible by 3 or not
print(set(upd_itms))
#assingnment
#Triple the numbers given in list  using map ?
nums = (1, 2, 3, 4, 5, 6, 7) 
print("Original list: ", nums)
result = map(lambda x: x + x + x, nums) 
print("\nTriple of said list numbers:")
print(list(result))
# mam's solution 

import math
num=[2,3,4,5,6]
def listTripler(item):
    return math.floor(math.pow(item,3))

resultList=list(map(listTripler,num))
print(resultList)


#Separate even odd number from given list using map function?
nums=[0,1,2,3,4,5,6,7,8,9,10]
def evenList(i):
    if(i%2==0):
        return i
def oddList(i):
    if(i%2!=0):
        return i
evenNumbers=list(filter(lambda
x:x,map(evenList,nums)))
oddNumbers=list(filter(lambda x:x,map(oddList,nums)))
print("Odd numbers : {0}".format(oddNumbers))
print("Even numbers : {0}".format(evenNumbers))

#Print all string in lower case from given tuple
courses=("SOFTWARE","ITITMS","DD","ANIMATION")

output=tuple(map(lambda i:i.lower(),courses))
print(output)

#Print square root of numbers given in list
import math
l3=[24,36,64,25]
output=list(map(lambda i:math.sqrt(i),l3))
print(output)


#Eliminate duplicate letter from given string
import re #regular expression
string = ""
str = "hello world hello"
def findDuplicate(i):
    global string
    if re.search(i,string) == None:
        string += i

ans=map(findDuplicate,str)
print(list(ans)) # you need to print this list formap function as it is mandatory
print("String with unique characters:",string)


#Print table of any number
number=int(input("Enter number for multiplication table :"))
l=int(input("Enter limit till you want to print table:"))

def multiples(i):
    return number*i

limitList=[]
for i in range(1,l+1):
    limitList.append(i)

res =list(map(multiples,limitList))
print("Multiplication Table : ",res)



#Add two list
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
result = map(lambda x, y: x + y, nums1, nums2)
print("Result: after adding two list")
print(list(result))



#Convert all float digits into integer using built in function from given list.
l= [2.5, 2.4, 3.8]
newlist = list(map(lambda i:int(i), l))
print(newlist)


#Add ‘@gmail.com’ to all the values of the given dictionary and convert it to lower case.
names ={'a':'anna','b':'bharat','c':'carlo','d':'dim'}
gmail = dict(map(lambda
x:(x[0],x[1]+'@gmail.com'),names.items()))
print(gmail)


#===========================filter++++++++++++++++++++++++

#Using filter() function filter the list so that only negative numbers are left.
l=[10,-20,-5,6,-8,55,-4]
def filterNegativeNum(i):
    if(i<0):
        return i
output=list(filter(filterNegativeNum,l))
print(output)


#Using filter function, filter the even numbers so that only odd numbers are passed to the new list.
numbers = (1,2,3,4,5,6,7,8)
def oddNumFilter(i):
    if i%2!=0:
        return True
    return False
check_odd = list(filter(oddNumFilter,numbers))
print("Odd Numbers : ",check_odd)    

# Using filter() and list() functions and .lower() method filter all the vowels in a given string.
string = "Hello World"
lowerCharacters = list(filter(lambda x: True if
x.lower() in "aeiou" else False, string))
print(lowerCharacters)

#. This time using filter() and list() functions filter all the positive integers in the string.
str="Winter Olympics in 2022 will take place in Beijing China"
lst=lst = list(filter(lambda x: True if x in "0123456789" else False, str))
print(lst)

#Convert a number to positive if it's negative in the list. Only pass those that are converted from negative to positive to the new list.[Try using map inside filter]
lst=[-1000, 500, -600, 700, 5000, -90000, -17500]
num = list(filter(lambda x: True if x>0 else False,
map(lambda x: x*-1, lst)))
print(num)



#========================EXCEPTION HANDLING===========================

#example1
try:
 print('try block')
 x = int(input("Enter number"))
 y = int(input("Enter another number"))
 z = x/y
except ZeroDivisionError:
 print("except ZeroDivisionError block")
 print("Division by 0 not accepted")
else:
 print("else block")
 print("Division = ", z)
finally:
 print("finally block")
 x=0
 y=0
print ("Out of try, except, else and finally blocks." )


#Example2 : Raise an Exception
try:
 x=int(input('Enter a number upto 100: '))
 if x > 100:
    raise ValueError(x)
except ValueError:
 print(x, "is out of allowed range")
else:
 print(x, "is within the allowed range")

 #Below, we have buggy code. Add a try/except clause so the code runs without errors. If a blog post didn’t get any likes, a ‘Likes’ key should be added to that dictionary with a value of 0. CODE : blog_posts = [{'Photos': 3, 'Likes': 21, 'Comments': 2}, {'Likes': 13, 'Comments': 2, 'Shares': 1}, {'Photos': 5, 'Likes': 33, 'Comments': 8, 'Shares': 3}, {'Comments': 4, 'Shares': 2}, {'Photos': 8, 'Comments': 1, 'Shares': 1}, {'Photos': 3, 'Likes': 19, 'Comments': 3}] total_likes = 0
#for post in blog_posts: total_likes = total_likes + post['Likes']


blog_posts = [{'Photos': 3, 'Likes': 21, 'Comments': 2},
{'Likes': 13, 'Comments': 2, 'Shares': 1}, {'Photos': 5,
'Likes': 33, 'Comments': 8, 'Shares': 3}, {'Comments': 4,
'Shares': 2}, {'Photos': 8, 'Comments': 1, 'Shares': 1},
{'Photos': 3, 'Likes': 19, 'Comments': 3}]
total_likes = 0
for post in blog_posts:
    try:
        total_likes = total_likes + post['Likes']
    except:
        post["Likes"]=0



#================= gui =======================
#dice roll

from tkinter import *
import random 
root = Tk() 
diceImage = PhotoImage(file='s1.png') 
#function to generate random number 
def randomDice(): 
    a = random.randint(1,6)  
    imageName = "s"+str(a)+".png" 
    diceImage.config(file=imageName) 
# button to get random dice 
btn = Button(root, text="Random Dice", command=randomDice, 
pady=5) 
btn.pack(pady=5) 
dice = Label(root, image=diceImage)       
dice.pack(padx=10) 


root.mainloop()

#===========List view - Run below code for better 
# understanding.I have modified task 
# for convenience and better performance.

from tkinter import *
window = Tk()
window.title("Form")
#window.config(bg="black")
window.geometry("700x600")
scrollbar=Scrollbar(window,width=20,troughcolor="red"
,background="red")
scrollbar.grid(row=0,column=1,rowspan=4,sticky=N+S)
scrollbar1=Scrollbar(window,width=20,orient=VERTICAL)
scrollbar1.grid(row=0,column=4,rowspan=4,sticky=N+S)
#listbox=Listbox
test=StringVar()
def b1():
    try:
        a=li.get(li.curselection())
        li2.insert(END,a)
        li.delete(li.curselection())
    except Exception:
        print("select value:)")
def b2():
    a = li2.size()
    for i in range(0,li.size()):
        str=li.get(i)
        li2.insert(a+i,str)
        li.delete(0,END)
def b3():
    a = li2.get(li2.curselection())
    li.insert(END, a)
    li2.delete(li2.curselection())
def b4():
    a = li.size()
    for i in range(0, li2.size()):
        str = li2.get(i)
        li.insert(i+a, str)
    li2.delete(0, END)
li=Listbox(window,width=20,height=15,bg="#FCD9AC",font=("Arail",14),
    yscrollcommand=scrollbar.set)
li.grid(row=0,column=0,rowspan=4)
li.insert(1,"Tea")
li.insert(2,"coffee")
li.insert(3,"juice")
li.insert(4,"Alcohol")
li.insert(5,"Water")
li.insert(6,"cold drink")
li.insert(7,"smoothie")
li.insert(8,"shake")
li.insert(9,"soup")
li.insert(10,"cold water")
li.insert(11,"red bull")
li.insert(12,"pepsi")
li.insert(13,"coke")
li.insert(14,"sugarcane juice")
li.insert(15,"kiwi juice")
li.insert(16,"orange juice")
li.insert(17,"mango juice")
li.insert(18,"stawberry juice")
scrollbar.config(command=li.yview,troughcolor="red")
scrollbar1.config(command=li.yview)
b=Button(window,text=">",font=("ArialBold",12),width=7,height=1,bd=3,command=b1)
b.grid(row=0,column=2,padx=20)
b1=Button(window,text=">>",font=("ArialBold",12),width=7,height=1,bd=3,command=b2)
b1.grid(row=1,column=2,padx=40)
b2=Button(window,text="<",font=("ArialBold",12),width=7,height=1,bd=3,command=b3)
b2.grid(row=2,column=2,padx=40)
b3=Button(window,text="<<",font=("ArialBold",12),width=7,height=1,bd=3,command=b4)
b3.grid(row=3,column=2,padx=40)
li2=Listbox(window,width=20,height=15,bg="#40E0D0",font=("Arail",14),yscrollcommand=scrollbar1.set)
li2.grid(row=0,column=3,rowspan=4)
window.mainloop()

# temprature converter ferenhit to celcius
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror

# root window
root = tk.Tk()
root.title('Temperature Converter')
root.geometry('300x70')
root.resizable(False, False)


def fahrenheit_to_celsius(f):
    """ Convert fahrenheit to celsius
    """
    return (f - 32) * 5/9


# frame
frame = ttk.Frame(root)


# field options
options = {'padx': 5, 'pady': 5}

# temperature label
temperature_label = ttk.Label(frame, text='Fahrenheit')
temperature_label.grid(column=0, row=0, sticky='W', **options)

# temperature entry
temperature = tk.StringVar()
temperature_entry = ttk.Entry(frame, textvariable=temperature)
temperature_entry.grid(column=1, row=0, **options)
temperature_entry.focus()

# convert button


def convert_button_clicked():
    """  Handle convert button click event 
    """
    try:
        f = float(temperature.get())
        c = fahrenheit_to_celsius(f)
        result = f'{f} Fahrenheit = {c:.2f} Celsius'
        result_label.config(text=result)
    except ValueError as error:
        showerror(title='Error', message=error)


convert_button = ttk.Button(frame, text='Convert')
convert_button.grid(column=2, row=0, sticky='W', **options)
convert_button.configure(command=convert_button_clicked)

# result label
result_label = ttk.Label(frame)
result_label.grid(row=1, columnspan=3, **options)

# add padding to the frame and show it
frame.grid(padx=10, pady=10)


# start the app
root.mainloop()

## temprature converter celcius to ferenhit
import tkinter as tk
window = tk.Tk()
window.geometry("300x250")
window.config(bg="#A569BD")
window.resizable(width=False,height=False)
window.title('Celsius to Fahrenheit Converter!')

l1 = tk.Label(window,text="Celsius to Fahrenheit Converter",font=("Arial", 15),fg="white",bg="black")
l2= tk.Label(window,text="Enter temperature in Celsius: ",font=("Arial", 10,"bold"),fg="white",bg="#A569BD")
l3= tk.Label(window,text="Temperature in Fahrenheit is: ",font=("Arial", 10,"bold"),fg="white",bg="#A569BD")
 
empty_l1 = tk.Label(window,bg="#A569BD")
empty_l2 = tk.Label(window,bg="#A569BD")
 
e1= tk.Entry(window,font=('Arial',10))
 
btn1 = tk.Button(window,text="Convert to Fahrenheit!",font=("Arial", 10))
btn2 = tk.Button(window,text="Exit application",font=("Arial", 10))
 
t1=tk.Text(window,state="disabled",width=15,height=0)

l1.pack()
l2.pack()
e1.pack()
empty_l1.pack()
btn1.pack()
l3.pack()
t1.pack()
empty_l2.pack()
btn2.pack()

def exit():
    window.destroy()

def convert():
    c = int(e1.get())
    f = ((c*9)/(5))+32
    t1.config(state='normal')
    t1.delete('1.0', tk.END)
    t1.insert(tk.END,f)
    t1.config(state='disabled')

def exit():
    window.destroy()
 
def convert():
    c = int(e1.get())
    f = ((c*9)/(5))+32
    t1.config(state='normal')
    t1.delete('1.0', tk.END)
    t1.insert(tk.END,f)
    t1.config(state='disabled')
 
import tkinter as tk
window = tk.Tk()
window.geometry("300x250")
window.config(bg="#A569BD")
window.resizable(width=False,height=False)
window.title('Celsius to Fahrenheit Converter!')
 
l1 = tk.Label(window,text="Celsius to Fahrenheit Converter",font=("Arial", 15),fg="white",bg="black")
l2= tk.Label(window,text="Enter temperature in Celsius: ",font=("Arial", 10,"bold"),fg="white",bg="#A569BD")
l3= tk.Label(window,text="Temperature in Fahrenheit is: ",font=("Arial", 10,"bold"),fg="white",bg="#A569BD")
 
empty_l1 = tk.Label(window,bg="#A569BD")
empty_l2 = tk.Label(window,bg="#A569BD")
 
e1= tk.Entry(window,font=('Arial',10))
 
btn1 = tk.Button(window,text="Convert to Fahrenheit!",font=("Arial", 10),command=convert)
btn2 = tk.Button(window,text="Exit application",font=("Arial", 10),command=exit)
 
t1=tk.Text(window,state="disabled",width=15,height=0)
 
l1.pack()
l2.pack()
e1.pack()
empty_l1.pack()
btn1.pack()
l3.pack()
t1.pack()
empty_l2.pack()
btn2.pack()
 
window.mainloop()


# select tshirt size 
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# root window
root = tk.Tk()
root.geometry('300x220')
root.resizable(False, False)
root.title('Radio Button Demo')


def show_selected_size():
    showinfo(
        title='Result',
        message=selected_size.get()
    )


selected_size = tk.StringVar()
sizes = (('Small', 'S'),
         ('Medium', 'M'),
         ('Large', 'L'),
         ('Extra Large', 'XL'),
         ('Extra Extra Large', 'XXL'))

# label
label = ttk.Label(text="What's your t-shirt size?")
label.pack(fill='x', padx=5, pady=5)

# radio buttons
for size in sizes:
    r = ttk.Radiobutton(
        root,
        text=size[0],
        value=size[1],
        variable=selected_size
    )
    r.pack(fill='x', padx=5, pady=5)

# button
button = ttk.Button(
    root,
    text="Get Selected Size",
    command=show_selected_size)

button.pack(fill='x', padx=5, pady=5)


root.mainloop()





#formet of Tkinter====
from tkinter import *
window=Tk()
# add widgets here

window.title('Hello Python')
window.geometry("300x200+10+20")
window.mainloop()


#select the gender and game=============================
from tkinter import *
from tkinter.ttk import Combobox
window=Tk()
var = StringVar()
var.set("one")
data=("one", "two", "three", "four")
cb=Combobox(window, values=data)
cb.place(x=60, y=150)

lb=Listbox(window, height=5, selectmode='multiple')
for num in data:
    lb.insert(END,num)
lb.place(x=250, y=150)

v0=IntVar()
v0.set(1)
r1=Radiobutton(window, text="male", variable=v0,value=1)
r2=Radiobutton(window, text="female", variable=v0,value=2)
r1.place(x=100,y=50)
r2.place(x=180, y=50)
                
v1 = IntVar()
v2 = IntVar()
C1 = Checkbutton(window, text = "Cricket", variable = v1)
C2 = Checkbutton(window, text = "Tennis", variable = v2)
C1.place(x=100, y=100)
C2.place(x=180, y=100)

window.title('Hello Python')
window.geometry("400x300+10+10")
window.mainloop()


# factorial number 
import tkinter as tk
from tkinter.colorchooser import *
 
def factorial(n):   
    # single line to find factorial 
    return 1 if (n==1 or n==0) else n * factorial(n - 1);  
 
def calculate():
    result=factorial(int(entryText.get()))
    info.config(text=result)
    
mw = tk.Tk()
mw.title('COLOR ME!!!')
mw.geometry("200x200") 
mw.resizable(0, 0)
 
entryText = tk.Entry(text=1, bg='white', fg='black')
entryText.place(x = 50, y = 25, width=100, height=25)
 
btn = tk.Button(text='Calculate', command=calculate)
btn.place(x = 50, y = 75, width=100, height=25)
 
info = tk.Label(text='result', bg='white', fg='black')
info.place(x = 50, y = 125, width=100, height=25)
 
mw.mainloop()


#example of Button
from tkinter import *
top = Tk()
top. geometry ("200x100")
def fun():
    messagebox.showinfo("Hello”, “Red Button clicked")

# b1 = Button(top,text = "Red",command = fun,activeforeground = "red" activebackground = "pink" ,pady=10)
# b2 = Button(top, text = "Blue",activeforeground = "blue” ,activebackground = "pink",pady=10)
b3 = Button(top, text = "Green",activeforeground = "green" ,activebackground = "pink", pady=10)
b4 = Button(top, text = "Yellow" ,activeforeground = "yellow" ,activebackground = "pink" ,pady=10)

# b1.pack(side = LEFT)
# b2.pack(side = RIGHT)
b3.pack(side = TOP)
b4. pack(side = BOTTOM)
top.mainloop()

 
# pack mathod
from tkinter import *
# creating Tk window
pane = Tk()
b1 = Button(pane, text = "Click me !")
b1.pack(fill=Y, expand = True)
# Button 2
b2 = Button(pane, text = "Click me too")
b2.pack(fill = X, expand = True)
# Execute Tkinter
pane.mainloop()


#place method
# creating Tk window
master = Tk()
# setting geometry of tk window
master . geometry ("200x200")
# button widget
b1 = Button(master, text = "Click me !")
b1.place(relx = 1, x =-2, y = 2, anchor = NE)
# button widget
b2 = Button(master, text = "GFG")
b2.place(relx = 0.5, rely = 0.5, anchor = CENTER)
mainloop()
 


#grid method
from tkinter import *
# creating main tkinter window/topLevel
master = Tk()
# this will create Label widget
11 = Label(maste, text "First:")
12 = Label(master, text = "Second:")
# grid method to arrange Labels in respective
# rows and columns as specified
l1.grid(row = 0, column = 0, sticky = W, pady = 2)
l2.grid(row = 1, column = 0, sticky = W, pady = 2)
mainloop()


#lable example
#EXAMPLE - 1 
from tkinter import *
window = Tk() 
l1 - Label (window, text='Gujrat University!' ,font="Arial Bold", 20))
 window.geometry('350x200) 
l1. grid (column=0, row=0)
window.mainloop() 



#EXAMPLE - 2
from tkinter import *
root = Tk()
logo = root.PhotoImage(file='test.png')
w1 = Label(root, image=logo).pack(side="right")
msg = “””Welcome semester 3.”””
W2 = Label(root,justify=tk. LEFT, padx = 10,text=msg).pack(side="left") 
root.mainloop()


#entry wedge
import tkinter as tk
root=tk.Tk()
root.geometry("600x400")
name_var=tk.StringVar()
passw_var=tk.StringVar()
def submit():
    name=name_var.get()
    password=passw_var.get()
    print("The name is : " + name)
    print("The password is : " + password)
    name_var.set("")
    passw_var.set("")
name_label = tk.Label(root, text = 'Username', font=('Arial',10, 'bold'))
name_entry = tk.Entry(root,textvariable = name_var, font=('Arial',10,'normal'))
passw_label = tk.Label(root, text = 'Password', font = ('Arial',10,'bold'))
passw_entry=tk.Entry(root, textvariable = passw_var, font = ('Arial',10,'normal'), show = '*')
sub_btn=tk.Button(root,text = 'Submit', command = submit)
name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)
passw_label.grid(row=1,column=0)
passw_entry.grid(row=1,column=1)
sub_btn.grid(row=2,column=1)
root.mainloop()


#check buttone
from tkinter import *
root = Tk() 
root. geometry("300x200")
W = Label(root, text ='Gujrat University', font = "50").pack()
Checkbutton1 = tk.IntVar()
Checkbutton2 = tk.IntVar() 
Checkbutton3 = tk.IntVar()
Button1 = Checkbutton(root, text = "Tutorial", variable = Checkbutton1,
onvalue = 1, offvalue = 0,height = 2,width = 10)
Button2 = Checkbutton(root, text = "Student", variable = Checkbutton2,
onvalue = 1, offvalue = 0,height = 2,width = 10)
Button3 = Checkbutton (root, text = "Courses", variable = Checkbutton3,
onvalue = 0,offvalue = 0,height = 2,width = 10)
Button1.pack() 
Button2.pack() 
Button3.pack()
root.mainloop()
 
#check box
from tkinter import *
import tkinter
root = Tk() 
root. geometry("300x200")
w = Label(root, text ='Gujrat University', font = "50").pack()
Checkbutton1 = tkinter.IntVar()
Checkbutton2 = tkinter.IntVar() 
Checkbutton3 = tkinter.IntVar()
Button1 = Checkbutton(root, text = "Tutorial", variable = Checkbutton1,
onvalue = 1, offvalue = 0,height = 2,width = 10)
Button2 = Checkbutton(root, text = "Student", variable = Checkbutton2,
onvalue = 1, offvalue = 0,height = 2,width = 10)
Button3 = Checkbutton (root, text = "Courses", variable = Checkbutton3,
onvalue = 0,offvalue = 0,height = 2,width = 10)
Button1.pack() 
Button2.pack() 
Button3.pack()
root.mainloop()


#List box
from tkinter import * 
import tkinter as tk
top = Tk()
lb = Listbox(top,height=5,width=15,bg=”grey”,activestyle=”dotbox”,font=”Helvetica”,fg=”yellow”)
top.geometry(“300x200”)
l = Label(top,text = “Food Items”)
lb.insert(1,”Nachos”)
lb.insert(2,”Pizza”)
lb.insert(3,”Maggi”)
lb.insert(4,”Dosa”)
l.pack()
lb.pack()
top.mainloop()


#example 2
from tkinter import * 
import tkinter as tk
from tkinter import messagebox
top = Tk()
top.geometry("400x300")
var=StringVar()
def showSelected():
    countries=[]
    cname=lb.curselection()
    for i in cname():
        opt = lb.get(i)
        countries.append(op)
    for val in countries:
        print(val)
lb = Listbox(top,selectmode="multiple",width=10)
lb.pack(padx=10,pady=10,expand=YES,fill=BOTH)
x = ["India","USA","UK","Australia"]

for item in range(len(x)):
    lb.insert(END,x[item])
    lb.itemconfig(item,bg="#bdc1d6")
Button(top,text="Show Selected",command=showSelected).pack()
top.mainloop()



#massage box
from tkinter import * 
import tkinter as tk
from tkinter import messagebox
top = Tk()
top.geometry("300x200")
l = Label(top,text = "Message boxes",font=50)
l.pack()
messagebox.showinfo("showinfo", "Information")
messagebox.showwarning("showwarning", "Warning")
messagebox.showerror("showerror", "Error")
messagebox.askquestion("askquestion", "Are you sure?")
messagebox.askokcancel("askokcancel", "Want to continue?")
messagebox.askyesno("askyesno", "Find the value?") 
messagebox.askretrycancel("askretrycancel", "Try again?") 
top.mainloop()


#redio buttone
from tkinter import * 
import tkinter as tk
top = Tk()
top.geometry("300x200")
var = StringVar()
l = Label(top,text = "")
l.pack()
def printSelection():
    l.config(text="You have selected"+var.get())
r1 = Radiobutton(top,text="Male",variable=var,value="Male",command=printSelection)
r1.pack()
r2 = Radiobutton(top,text="Female",variable=var,value="Female",command=printSelection)
r2.pack()
r3 = Radiobutton(top,text="Other",variable=var,value="Other",command=printSelection)
r3.pack()
top.mainloop()


#scale wedge
from tkinter import * 
import tkinter as tk
top = Tk()
top.geometry("300x200")
v = DoubleVar()
l = Label(top)
l.pack()
def showVal():
    sel="Horizontal scale value - "+str(v1.get())
    l.config(text=sel,font=("Arial",14))
s1 = Scale(top,variable=v,from_=1,to=200,orient=HORIZONTAL)
s1.pack(anchor=CENTER)
Button(top,text="Show Selected",command=showVal,bg="yellow").pack()
top.mainloop()


#scroll wedge
from tkinter import * 
import tkinter as tk
top = Tk()
sb = Scrollbar(top)
sb.pack(side=RIGHT,fill=BOTH)
mylist = Listbox(top,yscrollcommand=sb.set)
for line in range(20):
    mylist.insert(END,"Num"+line)
mylist.pack(side=LEFT)
sb.config(command=mylist.yview)
top.mainloop()


#text wedge
from tkinter import * 
import tkinter as tk
top = Tk()
top.title("Python text widget")
top.geometry("400x300")
message = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy textever since the 1500s"
f = Frame(top)
tb = Text(f,height=13,width=20,wrap='word')
tb.insert(END,message)
tb.pack(side=LEFT,expand=YES)
sb=Scrollbar(f)
sb.pack(side=RIGHT,fill=BOTH)
tb.config(yscrollcommand=sb.set)
sb.config(command=tb.yview)
f.pack(command=True)
top.mainloop()

 

