
from tkinter import *
from tkinter.ttk import Progressbar
import random
from pygame import mixer
import pyttsx3


engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


mixer.init()
mixer.music.load("kbc.mp3")
mixer.music.play(-1)
def select(event):
    callButton.place_forget()
    ProgressbarA.place_forget()
    ProgressbarB.place_forget()
    ProgressbarC.place_forget()
    ProgressbarD.place_forget()

    ProgressbarLabelA.place_forget()
    ProgressbarLabelB.place_forget()
    ProgressbarLabelC.place_forget()
    ProgressbarLabelD.place_forget()




    b=event.widget
    value=b["text"]

    for i in range(15):
        if value == correct_answer1[i]:

            if value == correct_answer1[14]:

                def close():
                    root2.destroy()
                    root.destroy()

                mixer.music.stop()
                mixer.music.load("Kbcwon.mp3")
                mixer.music.play()
                root2 = Toplevel()
                root2.overrideredirect(True)
                root2.config(bg="black")
                root2.geometry("560x700+140+30")
                root2.title("You have won zero pounds")
                imageLabel = Label(root2, image=centerImage, bd=0)
                imageLabel.pack(pady=30)
                winLabel = Label(root2, text="You Won", font=("arial", 40, "bold"), bg="black", fg="white")
                winLabel.pack()



                closeButton = Button(root2, text="Close", font=("arial", 20, "bold"), bg="black", fg="white",
                                     activebackground="black", activeforeground="white", border=0, cursor="hand2",
                                     command=close)
                closeButton.pack()
                winLabel1 = Label(root2, text="Congratulations!!!",
                                  font=("arial", 30, "bold"),
                                  bg="black", fg="white")
                winLabel1.pack()
                winLabel2 = Label(root2, text="You have won 1 million pounds",
                                  font=("arial", 20, "bold"),
                                  bg="black", fg="white")
                winLabel2.pack()
                happyImage = PhotoImage(file="happy.png")
                sadLabel = Label(root2, image=happyImage, bg="black")
                sadLabel.place(x=30, y=280)
                sadLabel = Label(root2, image=happyImage, bg="black")
                sadLabel.place(x=400, y=280)

                root2.mainloop()
                break

            questionArea.delete(1.0, END)
            questionArea.insert(END, question1[i + 1])

            optionButton1.config(text=first_option1[i + 1])
            optionButton2.config(text=second_option1[i + 1])
            optionButton3.config(text=third_option1[i + 1])
            optionButton4.config(text=fourth_option1[i + 1])
            amountLabel.config(image=amountImages[i])

        if value not in correct_answer1:
            def close():
                root1.destroy()
                root.destroy()


            root1 = Toplevel()
            root1.overrideredirect(True)
            root1.config(bg="black")
            root1.geometry("560x700+140+30")
            root1.title("You have won zero pounds")
            imageLabel = Label(root1, image=centerImage, bd=0)
            imageLabel.pack(pady=30)

            loseLabel = Label(root1, text="You Lose", font=("arial", 40, "bold"), bg="black", fg="white")
            loseLabel.pack()
            closeButton = Button(root1, text="Close", font=("arial", 20, "bold"), bg="black", fg="white",
                                 activebackground="black", activeforeground="white", border=0, cursor="hand2",
                                 command=close)
            closeButton.pack()
            loseLabel1 = Label(root1, text="You had a great game!",
                              font=("arial", 20, "bold"),
                              bg="black", fg="white")
            loseLabel1.pack()
            loseLabel2 = Label(root1, text="Better luck next time",font=("arial", 20, "bold"),bg="black", fg="white")
            loseLabel2.pack()
            sadImage = PhotoImage(file="sad.png")
            sadLabel = Label(root1, image=sadImage, bg="black")
            sadLabel.place(x=30, y=280)
            sadLabel = Label(root1, image=sadImage, bg="black")
            sadLabel.place(x=400, y=280)
            root1.mainloop()
            break


def lifeline50():
    lifeline50Button.config(image=image50X,state=DISABLED)
    for i in range(15):
        if questionArea.get(1.0, "end-1c") == question1[i]:
            options = [first_option1[i] , second_option1[i] , third_option1[i] , fourth_option1[i]]
            remaining_options=[option for option in options if option not in correct_answer1]
            removed_options=random.sample(remaining_options,2)
            for i in range(2):
                if optionButton1["text"]== removed_options[i]:
                    optionButton1.config(text="")
                if optionButton2["text"]==removed_options[i]:
                    optionButton2.config(text="")
                if optionButton3["text"]==removed_options[i]:
                    optionButton3.config(text="")
                if optionButton4["text"]==removed_options[i]:
                    optionButton4.config(text="")








def audiencePoleLifeline():
    audiencePoleButton.config(image=audiencePoleX,state=DISABLED)
    ProgressbarA.place(x=580,y=250)
    ProgressbarB.place(x=620,y=250)
    ProgressbarC.place(x=660,y=250)
    ProgressbarD.place(x=700,y=250)

    ProgressbarLabelA.place(x=580,y=250)
    ProgressbarLabelB.place(x=620,y=250)
    ProgressbarLabelC.place(x=660,y=250)
    ProgressbarLabelD.place(x=700,y=250)
    for i in range(15):
        if questionArea.get(1.0,"end-1c")==question1[i]:
            random_values=[]
            for j in range(4):
                r=random.randrange(10,60)
                random_values.append(r)
            ProgressbarA.config(value=random_values[0])
            ProgressbarB.config(value=random_values[1])
            ProgressbarC.config(value=random_values[2])
            ProgressbarD.config(value=random_values[3])

def phoneLifeline():
    mixer.music.load("calling.mp3")
    mixer.music.play()
    callButton.place(x=70,y=260)
    phoneLifelineButton.config(image=phoneImageX,state=DISABLED)

def phoneclick():
    callButton.config(state=DISABLED)
    for i in range(15):
        if questionArea.get(1.0,"end-1c")==question1[i]:
            engine.say(f"According to me the answer is {correct_answer1[i]}")
            engine.runAndWait()
            mixer.music.load("kbc.mp3")
            mixer.music.play(-1)




correct_answer=["PITEX","Mumbai","G.Van Rossum","Relph Baer","Commercial",
                "Allen Turing","Macro","Hertz","Machine","Java","C",
                "COBOL","Pseudocode","Eight bits","T.Berners Lee","Radia Perlman","Linux",
                "IBM","Nibble","Execution time","Ubuntu","Seymour Cray","OS/2","Intel 4004",
                "WIN.INI","PROM","1024 kilobytes","Dennis Ritchie","1988","Word Star",
                "Sahasra T","James Gosling","Nexus","Creeper virus","Prolog","1975","Firefox Mozilla",
                "Silicon","HTML","Flops","Cookie","Transistor","1500","FORTRAN",
                "Visicalc","D Flipflop","Bus","Control Bus","Spyware","Assembler",
                "1024","Byte","Root","FRAM","EPROM","Keyboard","hertz","VDU","Digitizer",
                "I/O Ports","All","Software","WRAM","SRAM","SGRAM","Floppy Disc",
                "255","Ribbon","LCD","Keyboard","UPCs","Java","Flip Flop","Information",
                "Polling","Software","External","Shift","Shape","Display","Mouse"]



question=["Which among the following is not an Operating System?",
           "Which among the following cities produce highest e-waste in India?",
           "Who among the following has designed Python programming language?",
           "Who among the following is popular as the father of video games?",
           "The .com used frequently in website url can be expresses as...?",
           "Who is the father of Computer Science?",
           "An instruction that produce several lines of machine language code is?",
           "Speed of processor is measured in ...?",
           "A CPU can directly understand .... language?",
           "The language used for development of various games is ...?",
           "UNIX is written in which language?",
           "A computer program used for business application is ...?",
           "..... is a cross between human language and a programming language?",
           "A group of ..... is commonly called as one byte?",
           "Who has invented World Wide Web?",
           "Who among the following is popular as Mother of Internet?",
           "Which one of the following is the first fully supported 64-bit operating system?",
           "Computer Hard Disk was first introduced by ....?",
           "What is half byte called....?",
           "The time taken by computer to process a specific task?",
           "Which of the following does not represent application software?",
           "Who is credited with the creation of the first Super Computer?",
           "Which of the following OS belongs to IBM?",
           "Which was the name of the first Microphone introduced be Intel?",
           "Which of the following file stores windows settings?",
           "Which of the following non-volatile memory can be written only once?",
           "A metabyte, also knowm as MB, contains?",
           "Who created C Programming language?",
           "When was NASCOM(National Association of Software and Services Companies) established?",
           "Which one is the first word processor application?",
           "Which one is the current fastest Super Computer in India?",
           "Who developed Java programming language?",
           "Which one is the first web browser invented in 1990?",
           "First computer virus is known as....?",
           "Which one programming language is exclusively used for AI?",
           "In which year Microsoft company was founded?",
           "Which of the following is not a search engine?",
           "IC chips for computer are usually made of ....?",
           "Generally, which language is used to construct World Wide Web pages?",
           "Which type Processing speed measurement used in SuperComputer",
           "A packet of information that travels between a browser and the web server is known as?",
           "Second Generation computers were based on?",
           "In EDSAC, an addition operation was completed in .... micro seconds?",
           "The first computer language developed was ...?",
           "The first computer spreadsheet program was ...?",
           "Which Flip Flop is used to store data in registers?",
           "The communication line between CPU memory and Peripherals is a ...?",
           "The Command to access the memory or the I/O device is carried by?",
           "Adware is some times called ___",
           "Which of the following language is the closest to the machine code?",
           "Kilobyte equals to how many bytes?",
           "Which of the following is the smallest measure of storage?",
           "Which of the following is mandatory for every disk?",
           "______ is RAM that combines the fast read and write access of Dynamic RAM",
           "CPU performs read/write operations at any point in time in _____",
           "Where would you find the letters “QWERTY”?",
           "The refresh rate of monitor is measured in ___",
           "The work done by a computer is displayed in which part of computer?",
           "___is an input device that converts analog information into digital form.",
           "The data transfer from CPU to peripheral devices of computer is achieved by",
           "Which of the following is/are example(s) of an Operating System?",
           "____ is a generic term for organized collection of computer data.",
           "_______ is a high-performance video RAM that is dual ported.",
           "Which memory does not use capacitor in its memory cell?",
           "Which is the clock synchronized RAM used for video memory?",
           "A removable magnetic disk that holds information is _________",
           "A byte can represent any number between 0 and ___",
           "Direct Thermal printer does not use ___",
           "Which of the following is non-emissive display?",
           "Which device is used to enter the text and numerical data in a computer",
           "Bar-code readers use light to read __",
           "Which of the following is not a hardware?",
           "The circuit used to store one bit of data is known as__",
           "The primary aim of computer process is to convert the data into ___",
           "The process where in the processor constantly checks the status flags is",
           "Interrupts that are initiated by an instruction are__",
           "Interrupts which are initiated by an I/O drive are",
           "Which register is capable of shifting binary information to right or left",
           "The OCR recognises the _______ of the characters with the help of light source",
           "The ______ may also be called the screen or monitor",
           "Which of these is a pointing and drop device?"]






first_option=["UNIX","Delhi",
              "Larry Wall","Relph Baer","Corporation","Edward Robert",
              "Assemble","Hertz","Java","C",
              "C","FORTRAN","Compiler","Six bits",
              "T.Berners Lee","Radia Perlman","Windows Vista","Dell",
              "Kilo byte","Real time","Open office",
              "Seymour Cray","UNIX","Intel 4004","SYSTEM.INI",
              "PROM","512 bytes","Ken Thompson","1988",
              "MS WORD","Aadithya","James Gosling","Chrome",
              "Rabbit","C","1972","Google",
              "Silver","URL","Giga hertz","Malware","IC","4000","COBOL",
              "Lotus 1-2-3","D Flipflop","Registers","Address Bus","Shareware",
              "Compiler","1000","KB","Root","VRAM","PROM","Joy Stick","Byte","CPU",
              "Plotter","Modem","UNIX","Firmware","VRAM","SRAM","DRAM","Floppy Disk",
              "312","Heat","LED","Plotter","UPCs","Processor","Encoder","Table",
              "Polling","Internal","Internal","Parallel","Size","Scanner","Scanner"]



second_option=["LINUX","Bengaluru",
               "G.Van Rossum","W.J. Clerk","Commercial","Charles Babbage",
               "Address","Pathom","C","Java",
               "C++","BASIC","Interpreter","Eight bits",
               "George Boole","Ada Lovelace","Mac","Apple",
               "bit","Response time","Ms toolkit",
               "Charles Babbage","DOS","Intel 8008","TEMP.INI",
               "EPROM","1024 bytes","Dennis Ritchie","1997",
               "Apple i Word","SAGA-220","D.Engelbart","Mosaic",
               "Creeper virus","Java","1975","Yahoo",
               "Aluminium","IRC","MIPS","Adware","Vacuum tube","3000","PASCAL",
               "MS Excel","JK Flipflop","Motherboard","Data Bus","Abandonware",
               "Interpreter","1064","MB","Sub","WRAM","EPROM","Light Pen","Seconds",
               "VDU","Track Ball","Interface","Linux","Software","WRAM","DRAM","SRAM",
               "Hard Drive","255","Coated Paper","LCD","Scanner","UPSs",
               "Printer","OR","Graph","Inspection","External","External","Serial",
               "Shape","Display","Printer"]

third_option=["OS X","Chennai",
              "Joe Armstrong","L. da Vinci","Cooperative","Allen Turing",
              "Mnemonic","Byte","C++","SQL",
              "Python","COBOL","Java","Twelve bits",
              "Jean Bartik","Grace Hopper","Linux","Microsoft",
              "Nibble","Waiting time","Photoshop",
              "D.M. Ritchie","OS/2","Intel 8080","WIN.INI",
              "EEPROM","1000 kilobytes","Robin Milner","1993",
              "Sun Star Office","Sahasra T","M.Clarke","Mozilla",
              "Elk Cloner","J2EE","1980","Firefox Mozilla",
              "Copper","NIH","Flops","Spyware","Transistor","2000","BASIC",
              "Visicalc","RS Flipflop","Bus","Control Bus","Donationware",
              "Assembler","1024","TB","Bare","MRAM","RAM","Numeric Pad","hertz","ALU",
              "Light Pen","Buffer","Windows XP","Hardware","MRAM","ROM","SGRAM",
              "Monitor","1024","Ribbon","Both","Printer","POSs","Mouse",
              "Flip Flop","File","Reviewing","Hardware","Both","Shift","Colour",
              "Hard Disk","Keyboard"]


fourth_option=["PITEX","Mumbai",
               "Y. Matsumoto","Leon Bolle","Cordial","Bill Gates",
               "Macro","Bit","Machine","PHP",
               "PHP","LOGO","Pseudocode","Fifteen bits",
               "Per Brinch","Anita Borg","Windows XP","IBM",
               "Word size","Execution time","Ubuntu",
               "C. Ginsberg","Fedora","Intel Pentium","SYSINFO.INI",
               "None","1024 kilobytes","Frieder Nake","1882",
               "Word Star","HP Apollo 6000","James D.Foley","Nexus",
               "SCA virus","Prolog","1984","Altavista",
               "Silicon","HTML","Nacron","Cookie","None","1500","FORTRAN",
               "None","None","None","None","Spyware","None","None","Byte","None",
               "FRAM","ROM","Keyboard","None","None","Digitizer","I/O Ports",
               "All","None","None","None","None","None","1025","None",
               "None","Keyboard","Optical Marks","Java","None","Information",
               "None","Software","All","Storage","None","None","Mouse"]

start = 0
end = 81
samples = 15
r = random.sample(range(start, end), samples)
question1 = []
correct_answer1 = []
first_option1 = []
second_option1 = []
third_option1 = []
fourth_option1 = []
for j in r:
    question1.append(question[j])
    correct_answer1.append(correct_answer[j])
    first_option1.append(first_option[j])
    second_option1.append(second_option[j])
    third_option1.append(third_option[j])
    fourth_option1.append(fourth_option[j])


root=Tk()

root.geometry("1520x750+0+0")
root.title("Who wants to be a millionaire?...")

root.config(bg="black")

leftframe=Frame(root,bg="black",padx=120)
leftframe.grid(row=0,column=0)

topframe=Frame(leftframe,bg="black",pady=15)
topframe.grid(row=0,column=0)

centerframe=Frame(leftframe,bg="black",pady=15)
centerframe.grid(row=1,column=0)

bottomframe=Frame(leftframe)
bottomframe.grid(row=2,column=0)

rightframe=Frame(root,pady=60,padx=50,bg="black")
rightframe.grid(row=0,column=1)

image50=PhotoImage(file="50-50.png")
image50X=PhotoImage(file="50-50-X.png")

lifeline50Button=Button(topframe,image=image50,bg="black",bd=0,activebackground="black",width=180,height=80,cursor="hand2",command=lifeline50)
lifeline50Button.grid(row=0,column=0)

audiencePole=PhotoImage(file="audiencePole.png")
audiencePoleX=PhotoImage(file="audiencePoleX.png")

audiencePoleButton=Button(topframe,image=audiencePole,bg="black",bd=0,activebackground="black",width=180,height=80,cursor="hand2",command=audiencePoleLifeline)

audiencePoleButton.grid(row=0,column=1)

phoneImage=PhotoImage(file="phoneAFriend.png")
phoneImageX=PhotoImage(file="phoneAFriendX.png")

phoneLifelineButton=Button(topframe,image=phoneImage,bg="black",bd=0,activebackground="black",width=180,height=80,cursor="hand2",command=phoneLifeline)
phoneLifelineButton.grid(row=0,column=2)

callImage=PhotoImage(file="phone.png")
callButton=Button(root,image=callImage,bd=0,bg="black",activebackground="black",cursor="hand2",command=phoneclick)
centerImage=PhotoImage(file="center.png")

logoLabel=Label(centerframe,image=centerImage,bg="black")
logoLabel.grid(row=0,column=0)

amountImage=PhotoImage(file="picture0.png")
amountImage1=PhotoImage(file="picture1.png")
amountImage2=PhotoImage(file="picture2.png")
amountImage3=PhotoImage(file="picture3.png")
amountImage4=PhotoImage(file="picture4.png")
amountImage5=PhotoImage(file="picture5.png")
amountImage6=PhotoImage(file="picture6.png")
amountImage7=PhotoImage(file="picture7.png")
amountImage8=PhotoImage(file="picture8.png")
amountImage9=PhotoImage(file="picture9.png")
amountImage10=PhotoImage(file="picture10.png")
amountImage11=PhotoImage(file="picture11.png")
amountImage12=PhotoImage(file="picture12.png")
amountImage13=PhotoImage(file="picture13.png")
amountImage14=PhotoImage(file="picture14.png")
amountImage15=PhotoImage(file="picture15.png")

amountImages=[amountImage1,amountImage2,amountImage3,amountImage4,amountImage5,amountImage6,amountImage7,
              amountImage8,amountImage9,amountImage10,amountImage11,amountImage12,amountImage13,
              amountImage14,amountImage15]

amountLabel=Label(rightframe,image=amountImage,bg="black")
amountLabel.grid(row=0,column=0)

layoutImage=PhotoImage(file="lay.png")

layoutLabel=Label(bottomframe,image=layoutImage,bg="black")
layoutLabel.grid(row=0,column=0)

questionArea=Text(bottomframe,font=("arial",18,"bold"),width=34,height=2,wrap="word",bg="black",fg="white",bd=0)
questionArea.place(x=70,y=10)

questionArea.insert(END,question1[0])

labelA=Label(bottomframe,text="A:",bg="black",fg="white",font=("arial",16,"bold"))
labelA.place(x=60,y=110)

optionButton1=Button(bottomframe,text=first_option1[0],font=("arial",18,"bold"),bg="black",fg="white",
                     bd=0,activebackground="black",activeforeground="white",cursor="hand2")
optionButton1.place(x=100,y=100)

labelB=Label(bottomframe,text="B:",bg="black",fg="white",font=("arial",16,"bold"))
labelB.place(x=330,y=110)

optionButton2=Button(bottomframe,text=second_option1[0],font=("arial",18,"bold"),bg="black",fg="white",
                     bd=0,activebackground="black",activeforeground="white",cursor="hand2")
optionButton2.place(x=370,y=100)

labelC=Label(bottomframe,text="C:",bg="black",fg="white",font=("arial",16,"bold"))
labelC.place(x=60,y=190)

optionButton3=Button(bottomframe,text=third_option1[0],font=("arial",18,"bold"),bg="black",fg="white",
                     bd=0,activebackground="black",activeforeground="white",cursor="hand2")
optionButton3.place(x=100,y=180)

labelD=Label(bottomframe,text="D:",bg="black",fg="white",font=("arial",16,"bold"))
labelD.place(x=330,y=190)

optionButton4=Button(bottomframe,text=fourth_option1[0],font=("arial",18,"bold"),bg="black",fg="white",
                     bd=0,activebackground="black",activeforeground="white",cursor="hand2")
optionButton4.place(x=370,y=180)




ProgressbarA=Progressbar(root,orient=VERTICAL,length=120)
ProgressbarB=Progressbar(root,orient=VERTICAL,length=120)
ProgressbarC=Progressbar(root,orient=VERTICAL,length=120)
ProgressbarD=Progressbar(root,orient=VERTICAL,length=120)

ProgressbarLabelA=Label(root,text="A",font=("arial",20,"bold"),bg="black",fg="white")
ProgressbarLabelB=Label(root,text="B",font=("arial",20,"bold"),bg="black",fg="white")
ProgressbarLabelC=Label(root,text="C",font=("arial",20,"bold"),bg="black",fg="white")
ProgressbarLabelD=Label(root,text="D",font=("arial",20,"bold"),bg="black",fg="white")

optionButton1.bind("<Button-1>",select)
optionButton2.bind("<Button-1>",select)
optionButton3.bind("<Button-1>",select)
optionButton4.bind("<Button-1>",select)
