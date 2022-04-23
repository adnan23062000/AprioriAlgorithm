import tkinter as tk
from tkinter import *

window=Tk()


n = 0
data = []

# for x in range(0, n):
#     list2 = ['T'+str(x+1), list(map(str, input("Enter items of Transaction " + str(x+1) + " => ").strip().split(' ')))]
#     data.append(list2)

class MyWindow:
    def __init__(self, win):
        label = tk.Label(window, text="Welcome to Apriori App", font=("Arial", 25), pady=60, padx=30, fg='#000').pack()
        self.lbl1=Label(win, text='Enter no. of Transactions: ')
        self.lbl2=Label(win, text='Enter Items')
        self.lbl3=Label(win, text='Result')
        self.t1=Entry(bd=3)
        self.t2=Text(window, width=20, height=3)
        self.t3=Entry()
        self.btn1 = Button(win, text='Add')
        self.btn2=Button(win, text='Subtract')
        self.lbl1.place(x=100, y=150)
        self.t1.place(x=280, y=150)
        self.lbl2.place(x=100, y=200)
        self.t2.place(x=280, y=200)
        self.b1=Button(win, text='submit', command=self.add)
        self.b1.place(x=320, y=280)
        self.lbl3.place(x=100, y=330)
        self.t3.place(x=200, y=330)
    def add(self):
        self.t3.delete(0, 'end')
        num1=int(self.t1.get())
        n = num1
        num2=str(self.t2.get("1.0",END))
        # print(num2)
        list2 = ['T', list(map(str, num2.strip().split(' ')))]
        data.append(list2)
        text_file = open("sample.txt", "w")
        n = text_file.write(num2)
        text_file.close()
        Apriori()

        result=str(num1) + num2
        # self.t3.insert(END, str(result))



lines = open("sample.txt").read().splitlines()
p = 1
for i in lines:
    # print(i)
    list2 = ['T' + str(p), list(map(str, i.strip().split(' ')))]
    p = p + 1
    data.append(list2)

print(data)


def Apriori():
    init = []

    for i in data:
        for q in i[1]:
            if(q not in init):
                init.append(q)
    init = sorted(init)
    print(init)

# sup = int(input("Enter Support Count Percentage: "))
    sp = float(40/100)
    s = int(sp*len(init))
# print(s)


    from collections import Counter

    c = Counter()
    for i in init:
        for d in data:
            if(i in d[1]):
                c[i]+=1

    print("\nC1:")

    for i in c:
        print(str([i])+": "+str(c[i]))
    print()
    l = Counter()

    for i in c:
        if(c[i] >= s):
            l[frozenset([i])]+=c[i]
    print("L1:")

    for i in l:
        print(str(list(i))+": "+str(l[i]))

    print()
    pl = l
    pos = 1

    for count in range (2,1000):
        nc = set()
        temp = list(l)
        for i in range(0,len(temp)):
            for j in range(i+1,len(temp)):
                t = temp[i].union(temp[j])
                if(len(t) == count):
                    nc.add(temp[i].union(temp[j]))
        nc = list(nc)
        c = Counter()
        for i in nc:
            c[i] = 0
            for q in data:
                temp = set(q[1])
                if(i.issubset(temp)):
                    c[i]+=1
        print("C"+str(count)+":")
        for i in c:
            print(str(list(i))+": "+str(c[i]))
        print()
        l = Counter()
        for i in c:
            if(c[i] >= s):
                l[i]+=c[i]
        print("L"+str(count)+":")
        for i in l:
            print(str(list(i))+": "+str(l[i]))
        print()
        if(len(l) == 0):
            break
        pl = l
        pos = count
    print("The Association rules for the subsets")
    print("L"+str(pos)+":")

    for i in pl:
        print(str(list(i))+": "+str(pl[i]))
    print()

    from itertools import combinations

    for l in pl:
        c = [frozenset(q) for q in combinations(l,len(l)-1)]
        mmax = 0
        for a in c:
            b = l-a
            ab = l
            sab = 0
            sa = 0
            sb = 0
            for q in data:
                temp = set(q[1])
                if(a.issubset(temp)):
                    sa+=1
                if(b.issubset(temp)):
                    sb+=1
                if(ab.issubset(temp)):
                    sab+=1
            temp = sab/sa*100
            if(temp > mmax):
                mmax = temp
            temp = sab/sb*100
            if(temp > mmax):
                mmax = temp
            print(str(list(a))+" -> "+str(list(b))+" = "+str(sab/sa*100)+"%")
            print(str(list(b))+" -> "+str(list(a))+" = "+str(sab/sb*100)+"%")
        curr = 1
        print("choosing:", end=' ')
        for a in c:
            b = l-a
            ab = l
            sab = 0
            sa = 0
            sb = 0
            for q in data:
                temp = set(q[1])
                if(a.issubset(temp)):
                    sa+=1
                if(b.issubset(temp)):
                    sb+=1
                if(ab.issubset(temp)):
                    sab+=1
            temp = sab/sa*100
            if(temp == mmax):
                print(curr, end = ' ')
            curr += 1
            temp = sab/sb*100
            if(temp == mmax):
                print(curr, end = ' ')
            curr += 1
        print()
        print()

Apriori()


exit_button = Button(window,
    text = "Exit",
    bg ="#ffb3fe",
    height = 2,
    width = 15, command=window.destroy)

exit_button.pack(pady=20)
exit_button.place(x=340, y=400)


mywin=MyWindow(window)
window.title('Apriori App')
window.geometry("800x500")
window.mainloop()

