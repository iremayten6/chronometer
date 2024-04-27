from tkinter import *
def islem():
    if(durum):
        global sure
        sure[2] += 1
        if(sure[2] >= 100):
            sure[2] = 0
            sure[1] += 1
        if(sure[1] >= 60):
            sure[0] += 1
            sure[1] += 0
        sureFormati = metin.format(sure[0],sure[1],sure[2])
        sureEtiketi.config(text=sureFormati)

    pencere.after(10,islem)

def basla():
    global durum
    durum = True
def durdur():
    global durum
    durum = False
def sifirla():
    global sure
    sure =[0,0,0]
    sureEtiketi.configure(text="00:00:00")
def cikis():
    pencere.destroy()

durum = False

pencere = Tk()
pencere.title('Kronometre')
pencere.config(bg= "black")
sure =[0,0,0]
metin = '{0:02d}:{1:02d}:{2:02d}'
sureEtiketi = Label(pencere, text="00:00:00", bg="black", fg="white",font="Times 140")
sureEtiketi.pack(side=LEFT)

cerceve = Frame(bg="black")
cerceve.pack(side=LEFT, fill= "both", expand= True, pady=10)

baslaButon = Button(cerceve, text="Başla", width=10, command=basla)
baslaButon.pack(padx=10, pady=10)

durButon = Button(cerceve, text="Dur", width=10, command=durdur)
durButon.pack(padx=10, pady=10)

sifirlaButon = Button(cerceve, text="Sıfırla", width=10, command=sifirla)
sifirlaButon.pack(padx=10, pady=10)

cikisButon = Button(cerceve, text="Çıkış", width=10, command=cikis)
cikisButon.pack(padx=10, pady=10)

islem()

pencere.mainloop()