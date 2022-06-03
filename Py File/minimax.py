from tkinter import *
from tkinter import font                        
from tkinter import messagebox

def x(num):     
    b_list = (button0, button1, button2, button3, button4, button5, button6, button7, button8)          #   button0  button1  button2 
    b_temp = b_list[num]                                                                                #   button3  button4  button5
    var.set('X')                                                                                        #   button6  button7  button8
    b_temp["text"] = var.get()
    b_temp["state"] = DISABLED

    ToWin()

    key=0
    for i in b_list:
        if i['state']== DISABLED: key+=1 
        else: pass
        
    if key<8: o()
    else: pass

def o():
    b_list = (button0, button1, button2, button3, button4, button5, button6, button7, button8)
    bestscore = -10

    for i in b_list:                # tahtanın o an ki durumundan sonra ki butun ihtimaller icin doner
        if i['text'] == '':
            var.set('O')
            i["text"] = var.get()
            i["state"] = DISABLED

            score = minimax(False)  #print("score: ",score)

            var.set('')
            i["text"] = var.get()
            i["state"] = NORMAL

            if score > bestscore:   # score un alacagı -1 , 1 ve 0 degerine gore bu durumlar ihtimal havuzunda ki en iyi durumsa, if in icerisine girer ve i en iyi o durumu olur
                bestscore = score   # en iyi score guncellenir dongu devam eder 
                a = i               # mimimax fonksiyonunda O nun en iyi oynayabiliecegi yer  

    var.set('O')                            # en iyi O degerini tahtaya yazar
    a["text"] = var.get()
    a["state"] = DISABLED
    
    ToWin()

def minimax(isMinimax):
    if possibility() == "X":
        return -1
    elif possibility() == "O":
        return 1
    elif possibility() == "DRAW":
        return 0
    else: pass

    if isMinimax == True:       # hayali bilgisayar oynuyor
        b_list = (button0, button1, button2, button3, button4, button5, button6, button7, button8)
        bestscore = -10

        for i in b_list:
            if i['text'] == '':
                var.set('O')                # sıra O da oldugu icin bos bir yere O koy
                i["text"] = var.get()
                i["state"] = DISABLED

                score = minimax(False)      # ihtimal havuzunu olusturan minimax fonksiyonu     
                
                var.set('')                 # sıra O da oldugu icin bos alana koydugumuz O yu tekrar siliyoruz     
                i["text"] = var.get()
                i["state"] = NORMAL

                if score > bestscore:
                    bestscore = score

        return bestscore

    if isMinimax == False:      # hayali kullanıcı oynuyor  
        b_list = (button0, button1, button2, button3, button4, button5, button6, button7, button8)
        bestscore = 10

        for i in b_list:
            if i['text'] == '':
                var.set('X')
                i["text"] = var.get()
                i["state"] = DISABLED 

                score = minimax(True)

                var.set('')
                i["text"] = var.get()
                i["state"] = NORMAL

                if score < bestscore:
                    bestscore = score

        return bestscore    

def possibility():
    b_list = (button0, button1, button2, button3, button4, button5, button6, button7, button8)

    if (b_list[0]['text']==b_list[1]['text']==b_list[2]['text']=='X' or
        b_list[3]['text']==b_list[4]['text']==b_list[5]['text']=='X' or 
        b_list[6]['text']==b_list[7]['text']==b_list[8]['text']=='X' or 
        b_list[0]['text']==b_list[3]['text']==b_list[6]['text']=='X' or 
        b_list[1]['text']==b_list[4]['text']==b_list[7]['text']=='X' or 
        b_list[2]['text']==b_list[5]['text']==b_list[8]['text']=='X' or 
        b_list[0]['text']==b_list[4]['text']==b_list[8]['text']=='X' or 
        b_list[2]['text']==b_list[4]['text']==b_list[6]['text']=='X'    ):
            return "X"

    elif(b_list[0]['text']==b_list[1]['text']==b_list[2]['text']=='O' or 
         b_list[3]['text']==b_list[4]['text']==b_list[5]['text']=='O' or
         b_list[6]['text']==b_list[7]['text']==b_list[8]['text']=='O' or 
         b_list[0]['text']==b_list[3]['text']==b_list[6]['text']=='O' or 
         b_list[1]['text']==b_list[4]['text']==b_list[7]['text']=='O' or 
         b_list[2]['text']==b_list[5]['text']==b_list[8]['text']=='O' or
         b_list[0]['text']==b_list[4]['text']==b_list[8]['text']=='O' or 
         b_list[2]['text']==b_list[4]['text']==b_list[6]['text']=='O'   ) :
            return "O"

    elif(b_list[0]['state']==b_list[1]['state']==b_list[2]['state']==
         b_list[3]['state']==b_list[4]['state']==b_list[5]['state']==
         b_list[6]['state']==b_list[7]['state']==b_list[8]['state']==DISABLED):
            return "DRAW"

    else:
        pass

def ToWin():
    b_list = (button0, button1, button2, button3, button4, button5, button6, button7, button8)

    if (b_list[0]['text']==b_list[1]['text']==b_list[2]['text']=='X' or
        b_list[3]['text']==b_list[4]['text']==b_list[5]['text']=='X' or 
        b_list[6]['text']==b_list[7]['text']==b_list[8]['text']=='X' or 
        b_list[0]['text']==b_list[3]['text']==b_list[6]['text']=='X' or 
        b_list[1]['text']==b_list[4]['text']==b_list[7]['text']=='X' or 
        b_list[2]['text']==b_list[5]['text']==b_list[8]['text']=='X' or 
        b_list[0]['text']==b_list[4]['text']==b_list[8]['text']=='X' or 
        b_list[2]['text']==b_list[4]['text']==b_list[6]['text']=='X'    ):
            messagebox.showinfo("TO WIN", "Kullanıcı Kazandı :)")
            master.destroy()

    elif(b_list[0]['text']==b_list[1]['text']==b_list[2]['text']=='O' or 
         b_list[3]['text']==b_list[4]['text']==b_list[5]['text']=='O' or
         b_list[6]['text']==b_list[7]['text']==b_list[8]['text']=='O' or 
         b_list[0]['text']==b_list[3]['text']==b_list[6]['text']=='O' or 
         b_list[1]['text']==b_list[4]['text']==b_list[7]['text']=='O' or 
         b_list[2]['text']==b_list[5]['text']==b_list[8]['text']=='O' or
         b_list[0]['text']==b_list[4]['text']==b_list[8]['text']=='O' or 
         b_list[2]['text']==b_list[4]['text']==b_list[6]['text']=='O'   ) :
            messagebox.showinfo("TO WIN", "Bilgisayar Kazandı :(")
            master.destroy()

    elif(b_list[0]['state']==b_list[1]['state']==b_list[2]['state']==
         b_list[3]['state']==b_list[4]['state']==b_list[5]['state']==
         b_list[6]['state']==b_list[7]['state']==b_list[8]['state']==DISABLED):
            messagebox.showinfo("TO WIN", "Oyun Berabere  :|")
            master.destroy()

    else:
        pass


master = Tk()
master.title("X O X")
master.resizable(False, False)

myfont = font.Font(family='Arial', size=40, weight='bold') 
maincolor = 'peach puff'
secondcolor = 'bisque'  #secondcolor = 'papaya whip'

canvas = Canvas(master, height=400, width=400, bg=maincolor)
canvas.pack()

var = StringVar()
var.set('')

button0 = Button(canvas, text=var.get(), font=myfont, disabledforeground='black', bd=2, relief='raised', bg=secondcolor, activebackground=maincolor, command=lambda : x(0))
button0.place(relx=0.005, rely=0.005, relheight=0.33, relwidth=0.33) 

button1 = Button(canvas, text=var.get(), font=myfont, disabledforeground='black',  bd=2, relief='raised', bg=secondcolor, activebackground=maincolor, command=lambda : x(1))
button1.place(relx=0.335, rely=0.005, relheight=0.33, relwidth=0.33) 

button2 = Button(canvas, text=var.get(), font=myfont, disabledforeground='black', bd=2, relief='raised', bg=secondcolor, activebackground=maincolor, command=lambda : x(2))
button2.place(relx=0.665, rely=0.005, relheight=0.33, relwidth=0.33) 

button3 = Button(canvas, text=var.get(), font=myfont, disabledforeground='black', bd=2, relief='raised', bg=secondcolor, activebackground=maincolor, command=lambda : x(3))
button3.place(relx=0.005, rely=0.335, relheight=0.33, relwidth=0.33) 

button4 = Button(canvas, text=var.get(), font=myfont, disabledforeground='black', bd=2, relief='raised', bg=secondcolor, activebackground=maincolor, command=lambda : x(4))
button4.place(relx=0.335, rely=0.335, relheight=0.33, relwidth=0.33) 

button5 = Button(canvas, text=var.get(), font=myfont, disabledforeground='black', bd=2, relief='raised', bg=secondcolor, activebackground=maincolor, command=lambda : x(5))
button5.place(relx=0.665, rely=0.335, relheight=0.33, relwidth=0.33) 

button6 = Button(canvas, text=var.get(), font=myfont, disabledforeground='black', bd=2, relief='raised', bg=secondcolor, activebackground=maincolor, command=lambda : x(6))
button6.place(relx=0.005, rely=0.665, relheight=0.33, relwidth=0.33) 

button7 = Button(canvas, text=var.get(), font=myfont, disabledforeground='black', bd=2, relief='raised', bg=secondcolor, activebackground=maincolor, command=lambda : x(7))
button7.place(relx=0.335, rely=0.665, relheight=0.33, relwidth=0.33) 

button8 = Button(canvas, text=var.get(), font=myfont, disabledforeground='black', bd=2, relief='raised', bg=secondcolor, activebackground=maincolor, command=lambda : x(8))
button8.place(relx=0.665, rely=0.665, relheight=0.33, relwidth=0.33) 

master.mainloop()