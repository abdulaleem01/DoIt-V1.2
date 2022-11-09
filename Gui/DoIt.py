# keylogger using pynput module

import tkthread
from pynput.keyboard import Key, Listener
from tkinter import *
import pyautogui
from newresi import doc_maker
from PIL import ImageTk, Image, ImageDraw as D
import threading
from newup import hhh


count1 = 1
keys = []
keysl = []
a = True
tcdata = ""


def on_press(key):

    keys.append(key)
    write_file(keys)
    """
    try:ewzc
        print('alphanumeric key {0} pressed'.format(key.char))

    except AttributeError:
        print('special key {0} pressed'.format(key))
    """


def write_file(keys):
    global aw

    with open('keyss.txt', 'w') as f:
        for key in keys:

            # removing ''ttjxc
            global k
            k = str(key).replace("'", "")
            keysl.append(k)

            f.write(k)
            # explicitly adding a space afterhhhhhhqqwjjjjjjskfjksqwqwqwfffffqw
            # every keystroke for readabilitykkkkkkkqqwhjkhkhkjkkhqwqwkkkkkkkkqwqwqwjhjhtr
            f.write(' ')
    if (keysl[-1] == 'x' and keysl[-2] == 'z'):
        task1()
    elif (keysl[-1] == 'c' and keysl[-2] == 'x'):
        tkthread.call_nosync(openNewWindow)

        # openNewWindow()
    elif (keysl[-1] == 'n' and keysl[-2] == 'b'):

        aw = tkthread.call_nosync(newwin)

        # threading.Thread(target=newwin).start
    elif (keysl[-1] == 'c' and keysl[-2] == 'z'):
        task1()
        tkthread.call_nosync(openNewWindow)


#


#

234
def task1():
    # print("Its and screen shot")d
    global count1
    count1 = str(count1)
    name_file = f"capture{count1}"

    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r"{0}.png".format(name_file))
    nn = f"{name_file}.png"
    hhh(0,nn,'image')
    doc_maker(3, f'{name_file}.png')
    # commitkeysl.clear()
    count1 = int(count1)
    count1 += 1


def on_release(key):

    #print('{0} released'.format(key))

    # if key == Key.esc:
    # print(keysl)
    # Stop listener
    global a
    return a


def newwin():
    global count1
    count1 = str(count1)
    name_file = f"capture{count1}"

    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r"{0}.png".format(name_file))
    #doc_maker(3, f'{name_file}.png')
    # commitkeysl.clear()

    top1 = Toplevel(app)
    file_name = "capture4.png"
# Define the geometry of the window
    newfile = f"{name_file}.png"
    im = Image.open(newfile)
    width1, height1 = im.size

    frame = Frame(top1)
    frame.pack()
    frame.place(anchor='s', relx=0.5, rely=0.8)

    nwidth = round(width1/1.3)
    nheight = round(height1/1.3)

    img1 = im.resize((nwidth, nheight))
    img = ImageTk.PhotoImage(img1)
    label = Label(frame, image=img)
    label.pack()

    ####
    def open(a, b, c, d):

        imm = Image.open(newfile)
        img1 = imm.resize((nwidth, nheight))
        top = Toplevel(app)
        #draw = D.Draw(img1)
        # draw.rectangle([(a,b),(c,d)],outline="green")zxzxzxzxzxzxzx
        im1 = img1.crop((a, b, c, d))

        frame = Frame(top)
        frame.pack()
        frame.place(anchor='center', relx=0.5, rely=0.5)
        img11 = ImageTk.PhotoImage(im1)
        label = Label(frame, image=img11)
        label.pack()

        def helloCallBack():
            global aw
            crpfile = f"{name_file}crp.png"
            im1.save(crpfile)
            hhh(0,crpfile,'image')
            doc_maker(3, crpfile)

            top.destroy()
            top1.destroy()

        B = Button(top, text="SAVE", command=helloCallBack)
        B.pack(side="right", padx=50, pady=100)

        top.geometry(f"{width1}x{height1}")
        top.configure(background='#2C3333')
        top.title("DoIt V1.1 Cropped Image Viewer")

        top.mainloop()
    ####

    def motion(event):
        global x, y
        x, y = event.x, event.y
        # print(x,y)
        # return x , y
    label.bind('<Motion>', motion)

    def leftclick(event):
        # print(label.bind('<Motion>',motion))
        # print("left")
        # print(x,y)
        w1, h1 = x, y

        def middleclick(event):
            # print(label.bind('<Motion>',motion))
            # print("middle")
            #print(x, y)
            w2, h2 = x, y
            open(w1, h1, w2, h2)
        label.bind("<Button-3>", middleclick)

    label.bind("<Button-1>", leftclick)

    # <
    top1.title("DoIt V1.1 Image View for Crop")
    top1.geometry(f"{width1}x{height1}")
    top1.configure(background='#2C3333')

    top1.mainloop()
    count1 = int(count1)
    count1 += 1
    return


with Listener(on_press=on_press, on_release=on_release) as listener:
    app = Tk()

    label = Label(app, text='TestIt V1.1', pady=5,
                  font=('Monaco 15'), bg='#2C3333', fg='#A5C9CA')
    label.grid(row=0, column=0)
    label1 = Label(app, text='TC NUM -', pady=10,
                   font=('Monaco 15'), bg='#2C3333', fg='#A5C9CA')
    label1.grid(row=1, column=0)
    name = Entry(app, width=16, font=('Arial 13'), bg='#E7F6F2',)
    name.grid(row=1, column=1)
    label2 = Label(app, text='TC NAME -', pady=10,
                   font=('Monaco 15'), bg='#2C3333', fg='#A5C9CA')
    label2.grid(row=2, column=0)
    name1 = Entry(app, width=16, font=('Arial 13'), bg='#E7F6F2')
    name1.grid(row=2, column=1)
    

    ######
    # @tkthread.main(app)
    def openNewWindow():
     # Toplevel object which will
        # be treated as a new window
        newWindow = Toplevel(app)
        # Label(newWindow, text="Write the steps here ").pack(side=TOP)sssxcsdxc
        Label(newWindow, text="Write the step here ",
              bg='#2C3333', fg='#A5C9CA', font=('Arial 16')).pack(side=TOP)
        #name3 = Entry(newWindow, width=100, font=('Arial 16'))
        # name3.place(x=0, y=15)hhhhxcxc

        name3 = Entry(newWindow, width=100, font=('Arial 16'))
        name3.place(x=0, y=29)

        def for_but2():
            hhh(0,name3.get(),"")
            doc_maker(2, name3.get())
            newWindow.destroy()

        but2 = Button(newWindow, text="Okay", command=for_but2)
        but2.pack(side=BOTTOM)
        newWindow.title("TestIt V1.1")
        newWindow.configure(background='#2C3333')

        newWindow.geometry("900x100")
        newWindow.resizable(0, 0)
        newWindow.mainloop()

    ########

        # n

    def for_but1():
        doc_maker(1, name.get(), name1.get())
        but1.grid_forget()

    def for_but3():
        global a
        a = False

        hhh(2,name1.get())
        hhh(1,name.get())
        hhh(3)
        but3.grid_forget()

        # app.quit()

    but1 = Button(app, text="Start", command=for_but1,
                  bg='#A5C9CA', fg='#395B64')
    but1.grid(row=3, column=1)
    but3 = Button(app, text="End", command=for_but3,
                  bg='#A5C9CA', fg='#395B64')
    but3.grid(row=3, column=0)

    def for_but4():
        nw1 = Toplevel(app)
        Label(nw1, text="A and A Technologies™",
              bg='#2C3333', fg='#A5C9CA', font=('Arial 16')).pack(side=TOP, pady=20)

        Label(nw1, text="Website -https://abdulaleem.pythonanywhere.com/",
              bg='#2C3333', fg='#A5C9CA', font=('Arial 16')).pack(side=TOP, pady=20)
        # https://abdulaleem.pythonanywhere.com/
        Label(nw1, text="Contact - 7358660113",
              bg='#2C3333', fg='#A5C9CA', font=('Arial 16')).pack(side=TOP, pady=20)
        Label(nw1, text="Software © 2022 A and A Technologies™; user contributions licensed under CC BY-SA. rev 2022.10.4.22331",
              bg='#2C3333', fg='#A5C9CA', font=('Arial 5')).pack(side=BOTTOM)

        nw1.title("DoIt V1.1 About")
        nw1.configure(background='#2C3333')

        nw1.geometry("500x300")
        nw1.resizable(0, 0)

    def for_but5():
        nw2 = Toplevel(app)
        Label(nw2, text="1.Click Start button after entering TC name and File Name to start writing your testcase \n(the Start button will dissapear if its a success).",
              bg='#2C3333', fg='#A5C9CA', font=('Arial 13')).pack(side=TOP, pady=15)

        Label(nw2, text="2.Click End button without fail after writing completes \n(the End button will dissapear if its a success).",
              bg='#2C3333', fg='#A5C9CA', font=('Arial 13')).pack(side=TOP, pady=15)

        Label(nw2, text="3.Always mention the filename with docx extension \n example: filename.docx.",
              bg='#2C3333', fg='#A5C9CA', font=('Arial 13')).pack(side=TOP, pady=15)
        Label(nw2, text="4.Please delete the images stored in the folder in which the application is installed",
              bg='#2C3333', fg='#A5C9CA', font=('Arial 13')).pack(side=TOP, pady=15)
        Label(nw2, text="!!!!! New feature added for cropping images in V1.1 !!!!!",
              bg='#2C3333', fg='red', font=('Arial 20')).pack(side=TOP, pady=15)
        # https://abdulaleem.pythonanywhere.com/
        Label(nw2, text="CHEATS:\n1.ScreenShot - zx\n2.Text Input- xc\n3.Text Input and Screen Shot - zc\n4.ScreenShot and crop - bn",
              bg='#2C3333', fg='#A5C9CA', font=('Arial 16')).pack(side=TOP, pady=15)

        nw2.title("DoIt V1.1 Documentation")
        nw2.configure(background='#2C3333')

        nw2.geometry("800x500")
        nw2.resizable(0, 0)

    but4 = Button(app, text="About", command=for_but4,
                  bg='#A5C9CA', fg='#395B64')
    but4.grid(row=4, column=0, pady=25)

    but5 = Button(app, text="Documentation", command=for_but5,
                  bg='#A5C9CA', fg='#395B64')
    but5.grid(row=4, column=1, pady=25)
    app.configure(background='#2C3333')
    photo = PhotoImage(file="do-it.png")
    app.iconphoto(True, photo)

    app.title('DoIT V1.1')
    if count1 == 2:
        app.geometry('1000x100')
    else:
        app.geometry('300x225')
    app.resizable(0, 0)

    app.mainloop()

    listener.join()
