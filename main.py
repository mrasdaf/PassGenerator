from tkinter import *
from tkinter import messagebox
import random
from tkinter import scrolledtext

randomsymbols = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
onePassLen = 1

window = Tk()
window.title("Генератор паролей by mrasdaf")
window.geometry("475x675")
window.config(bg="black")
window.resizable(width=False, height=False)



countOfPasswordsLabel = Label(window, text="Кол-во паролей:", bg="black", fg="white", font="Arial 14")
countOfPasswordsLabel.place(x=50, y=50)

countOfPasswordsEntry = Entry(window, font="Arial 14")
countOfPasswordsEntry.place(x=200, y=50)

onePassLenEntry = Entry(window, font="Arial 14")
onePassLenEntry.place(x=200, y=100)

onePassLenLabel = Label(window, text="Кол-во символов в 1 пароле:", bg="black", fg="white", font="Arial 9")
onePassLenLabel.place(x=30, y=103)

def generateButtonClick():
    global randomsymbol
    global onePassLen
    cp = 0
    resultText.delete(1.0, "end")
    try:
        cp = int(countOfPasswordsEntry.get())
    except:
        resultText.insert(1.0, "Не удалось распознать число паролей!")
        return False
    try:
        onePassLen = int(onePassLenEntry.get())
    except:
        resultText.insert(1.0, "Не удалось распознать число символов в 1 пароле!")
        return False
    i = 1
    # print("213")
    outputStr = ""
    res = ""
    outputStrFULL = ""
    while i <= cp:
        res = res + "\n\n"
        for u in range(onePassLen):
            res = res + random.choice(randomsymbols)
        outputStrFULL = outputStr + res + "\n"
        i += 1
        outputStr = ""
    resultText.insert(1.0, outputStrFULL)
    
def aboutButtonClick():
    messagebox.showinfo("О программе", """
    Эта программа позволяет вам генерировать пароли.
    Программа выбирает случайные символы из последовательности знаков и после чего выводит результат.
    
    by mrasdaf
    Написано на Python
    """)

generateButton = Button(window, text="Сгенерировать", width=55, command=generateButtonClick)
generateButton.place(x=38, y=150)

resultText = scrolledtext.ScrolledText(width=50, height=27)
resultText.place(x=25, y=200)

aboutButton = Button(window, text="О программе", width=15, command=aboutButtonClick)
aboutButton.place(x=350, y=643)


window.mainloop()
