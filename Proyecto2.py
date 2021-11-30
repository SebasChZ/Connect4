import tkinter
from tkinter import *
import random
import time
from tkinter import messagebox
from PIL import ImageTk, Image
import webbrowser

def getColumn(M, columnNbr):
    column = []

    for fila in M[0:6]:
        column.append(fila[columnNbr])
    return column


listaindexes = [0,1,2,3,4,5,6] 


MatrizBase=[
        [0,0,0,0,0,0,0], 
        [0,0,0,0,0,0,0], 
        [0,0,0,0,0,0,0], 
        [0,0,0,0,0,0,0], 
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0]]

boton=[ 
        [0,0,0,0,0,0,0], 
        [0,0,0,0,0,0,0], 
        [0,0,0,0,0,0,0], 
        [0,0,0,0,0,0,0], 
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0]]

#Movement
redsB=[0,0,0,0,0,0,0]
movements=[0,0,0,0]

indexes=[0,1,2,3,4,5,6]
actualColumns=[0,1,2,3,4,5]

indexesAux=[0,1,2,3,4,5,6]

#GENERAL FUNCION MADE BY: teacher
def read (filePath):
    try:
        fo = open (filePath, 'r')
        res = fo.read()
        fo.close()
        return res
    except:
        return {}

winners = eval(read('Connect4\leaderboard.txt')) #GAMES FILE
MLoad = eval(read('Connect4\game.txt'))

#MAIN MENU#
class Main:
    def __init__(self, master):
        self.master = master
        master.title("Connect 4")
        master.geometry("550x550")
        master.iconbitmap('Connect4\icon.ico')

        self.img = ImageTk.PhotoImage(Image.open('Connect4\gamingBG.jpg'))#BACKGROUND
        self.background = Label(master, image=self.img)
        self.background.place(x=0, y=0, relwidth=1, relheight=1)

        self.tittle = Label(master,text="CONNECT 4", font=("8-BIT WONDER.TFF",40),bg="navy",fg="red")
        self.tittle.place(x=120,y=60)

        self.playButtom = Button(master, text="PLAY",bg = "royal blue",
                                    font=("8-BIT WONDER.TFF",20),command=self.opengameSelector)#PLAY BUTTOM
        self.playButtom.place(x=225,y=170)

        self.leaderButtom = Button(master, text="LEADERBOARD", bg="dodger blue",
                                    font=("8-BIT WONDER.TFF",20),command=self.openBoard)#HELP BUTTOM
        self.leaderButtom.place(x=155,y=240)

        self.helpButtom = Button(master, text="HELP", bg="dodger blue",
                                    font=("8-BIT WONDER.TFF",20),command=self.openDoc)#HELP BUTTOM
        self.helpButtom.place(x=225,y=310)

        self.quitButtom = Button(master, text="QUIT", bg="dodger blue",
                                    font=("8-BIT WONDER.TFF",20),command=self.master.destroy)#HELP BUTTOM
        self.quitButtom.place(x=225,y=380)

    def openDoc(self): #OPEN DOCUMENTATION
        webbrowser.open("https://drive.google.com/file/d/1YzrHGsU7adG770_yyjj5e_odhzVCcKM8/view",new=1)

    def opengameSelector(classCall): #OPEN GAME SELECTION WINDOW
        gamemenu = Toplevel(menu)
        classCall = GameSelector(master=gamemenu)
        gamemenu.mainloop()

    def openBoard(self): #OPEN LEADERBOARD
        gamemenu = Toplevel(menu)
        classCall = Leaderboard(master=gamemenu)
        gamemenu.mainloop()

class Leaderboard(): #LEADERBOARD
    global winners
    def __init__(self, master):
        self.master = master
        master.title("Connect 4")
        master.geometry("550x550")
        master.iconbitmap('Connect4\icon.ico')

        self.img = ImageTk.PhotoImage(Image.open('Connect4\leaders.jpg'))#BACKGROUND
        self.background = Label(master, image=self.img)
        self.background.place(x=0, y=0, relwidth=1, relheight=1)

        self.names = Label(master,text="NICKNAMES",bg="bisque2",fg="goldenrod",
                                    font=("8-BIT WONDER.TFF",20))
        self.names.place(x=80,y=130)
        self.names = Label(master,text="SCORES",bg="bisque2",fg="goldenrod",
                                    font=("8-BIT WONDER.TFF",20))
        self.names.place(x=320,y=130)

        self.ycord = 170
        self.sorted_dict = {k: v for k, v in sorted(winners.items(), key=lambda item: item[1],reverse=True)}
        for key, value in self.sorted_dict.items():
            self.nick = Label(self.master,text=key,bg="bisque2",fg="red",
                                    font=("8-BIT WONDER.TFF",15)).place(x=120,y=self.ycord)
            self.score = Label(self.master,text=value,bg="bisque2",fg="red",
                                    font=("8-BIT WONDER.TFF",15)).place(x=370,y=self.ycord)
            self.ycord += 50
            

class GameSelector(): #GAME SELECTION WINDOW
    def __init__(self, master):
        self.master = master
        master.title("Connect 4")
        master.geometry("550x550")
        master.iconbitmap('Connect4\icon.ico')

        self.img = ImageTk.PhotoImage(Image.open('Connect4\modeselector.jpg'))#BACKGROUND
        self.background = Label(master, image=self.img)
        self.background.place(x=0, y=0, relwidth=1, relheight=1)

        self.tittle = Label(master,text="Game mode", font=("8-BIT WONDER.TFF",40),bg="royal blue",fg="yellow")
        self.tittle.place(x=120,y=60)

        self.pvp = Button(master, text="PVP",bg = "royal blue",fg="yellow",
                                    font=("8-BIT WONDER.TFF",20),command=self.pvpStarter)#PLAY BUTTOM
        self.pvp.place(x=230,y=170)

        self.ai = Button(master, text="AI",bg = "royal blue",fg="yellow",
                                    font=("8-BIT WONDER.TFF",20),command=self.openPvE)#PLAY BUTTOM
        self.ai.place(x=245,y=240)

        self.load = Button(master, text="LOAD",bg = "royal blue",fg="yellow",
                                    font=("8-BIT WONDER.TFF",20),command=self.openLoad)#PLAY BUTTOM
        self.load.pack(side=BOTTOM)
    
    def pvpStarter(self):
        self.scrollbar = Scrollbar(orient="horizontal")
        self.p1 =  Entry(self.master,bg="deep sky blue",fg="yellow",font=("8-BIT WONDER.TFF",10),xscrollcommand=self.scrollbar.set)
        self.p1.insert(0,"Player 1:")
        self.p1.place(x=200,y=310)

        self.p2 =  Entry(self.master,bg="deep sky blue",fg="yellow",font=("8-BIT WONDER.TFF",10),xscrollcommand=self.scrollbar.set)
        self.p2.insert(0,"Player 2:")
        self.p2.place(x=200,y=340)

        self.start = Button(self.master, text="START",bg = "royal blue",fg="yellow",
                                    font=("8-BIT WONDER.TFF",15),command=self.openPvPGame)#PLAY BUTTOM
        self.start.place(x=230,y=370)
    
    def openPvPGame(self):
        global Matriz
        Matriz = MatrizBase
        actualGame = FullGame(player1=self.p1.get(),player2=self.p2.get(),mode="X",turn=True,matrix=MatrizBase)
        actualGame.mainloop()
    
    def openPvE(self):
        global Matriz
        Matriz = MatrizBase
        actualGame = FullGame(player1="X",player2="X",mode="AI",turn=True,matrix=MatrizBase)
        actualGame.mainloop()
    
    def openLoad(self):
        global Matriz
        Matriz = MLoad[0]
        actualGame = FullGame(player1=MLoad[2],player2=MLoad[3],mode=MLoad[4],turn=MLoad[1],matrix=Matriz)
        actualGame.mainloop()



class FullGame(tkinter.Tk):

    def __init__(self,player1,player2,mode,turn,matrix):
        global Matriz
        self.matrix = matrix
        self.modo=mode  
        self.actualT = turn      
        tkinter.Tk.__init__(self)
        self.iconbitmap('Connect4\icon.ico')
        self.p1 = player1
        self.p2 = player2
        if self.modo != "AI":
            self.title("Connect4 - "+self.p1+" VS "+self.p2)
        else:
            self.title("Connect4 - AI")
        # variables que definen filas y actualColumns

        self.cols = len(Matriz[0])
        self.rows = len(Matriz)

        if self.modo != "AI":
            self.mainFrame = tkinter.Frame(self)
            self.minsize(1000,800)
            self.maxsize(100,800)
            self.mainFrame.grid()
            self.configure(bg='gray80')
        else:
            self.mainFrame = tkinter.Frame(self)
            self.minsize(667,700)
            self.maxsize(100,800)
            self.mainFrame.grid()
            self.configure(bg='gray80')


        self.buttonMovement()
        self.labelAddtion()
        self.create_buttons()
        self.eachButton()
        self.teacherPintaTablero()

        self.actualTurn(self.actualT)

        if mode != "AI":
            self.p1Show = Label(self,text=self.p1,font=("8-BIT WONDER.TFF",20),bg="ivory2",fg="red").place(x=740,y=300)
            self.VSShow = Label(self,text="VS",font=("8-BIT WONDER.TFF",25),bg="ivory2",fg="dark green").place(x=740,y=360)
            self.p2Show = Label(self,text=self.p2,font=("8-BIT WONDER.TFF",20),bg="ivory2",fg="blue").place(x=740,y=420)
            self.saveActualGame = Button(self,text="SAVE GAME",font=("8-BIT WONDER.TFF",17),bg="gray",fg="black",command=lambda:self.saveActualGame_F(self.actualT,self.p1,self.p2,"PVP")).place(x=450,y=750)
        else:
            self.saveActualGame = Button(self,text="SAVE GAME",font=("8-BIT WONDER.TFF",17),bg="gray",fg="black",command=lambda:self.saveActualGame_F(self.actualT,self.p1,self.p2,"AI")).place(x=270,y=650)
        
    
    def saveActualGame_F(self,turn,player1,player2,mode):
        toSave = [Matriz,turn,player1,player2,mode]
        fo = open("Connect4\game.txt", "w")  #crea el file si no existe
        fo.write (str(toSave))
        fo.close()
        messagebox.showinfo(title="Game Saved",message="Succesful Save"+"\n"+"See you soon!")
        self.destroy()

    def actualTurn(self,turn):
        if self.modo != "AI":
            if self.actualT == True:
                self.turntoPLay = Label(self,text="NOW PLAYING",font=("8-BIT WONDER.TFF",20),bg="red",fg="white").place(x=740,y=80)
            elif self.actualT == False:
                self.turntoPLay = Label(self,text="NOW PLAYING",font=("8-BIT WONDER.TFF",20),bg="blue",fg="white").place(x=740,y=80)


########################################################################################################################
#Check for the buttons functions#

    def buttonMovement(self):
        global movements
        if self.modo != "AI":
            if self.actualT == True:
                self.bgx = 'red'
            elif self.actualT == False:
                self.bgx = 'blue'
        else:
            self.bgx = 'DarkOrchid4'
        btn=tkinter.Button(self.mainFrame,text="←",bg=self.bgx,
                                    width=3,height =3,fg="black",
                                    command = self.lookLeft)
        btn.grid(row=8, column=0,rowspan=9)
        movements[0]=btn
        #boton derecha
        btn=tkinter.Button(self.mainFrame,text="→",bg=self.bgx,
                                    width=3,height =3,fg="black",
                                    command = self.lookRight)
        btn.grid(row=8, column=10,rowspan=9)
        movements[2]=btn
        
    def lookRight(self):
        global indexes
        global Matriz
        global indexesAux
        global movements
        
        indexesAux=self.lUpdate(indexesAux)

        indexes=self.lUpdate(indexes)
        if 6 < indexes[-1]:
            Matriz=self.addition(Matriz)

        self.constantUpdate1()
        
        if self.validador2(0) == True:
            movements[0].config(state=NORMAL,text="←")
        self.labelAddtion()
        self.teacherPintaTablero()

    def lookLeft(self):
        global Matriz
        global indexesAux
        global indexes
        indexesAux=self.toTheLeft(indexesAux)
        
        if indexes[0] == 0:
            Matriz=self.ladd(Matriz)
        if 0 < indexes[0]:
            indexes=self.toTheLeft(indexes)
        
        self.constantUpdate2()
        
        if self.validador3(6) == True:
            movements[2].config(state=NORMAL,text="→")
        self.labelAddtion()
        self.teacherPintaTablero()
        
    def lUpdate(self,list):
        num=0
        while num < len(list):
            list[num]=list[num]+1
            num+=1
        return list

    def toTheLeft(self,list):
        num=0
        while num < len(list):
            list[num]=list[num]-1
            num+=1
        return list
    
    def addition(self,M):
        for i in M:
            i+=[0]
        return M

    def ladd(self,matrix):
        newL=[0]
        i=0
        while i < len(matrix):
            matrix[i]=newL+matrix[i]
            i+=1
        return matrix

    def constantUpdate(self):
        print ()
        self.constantUpdate1()
        self.constantUpdate2()

########################################################################################################################

########################################################################################################################
#Create the updates per turn#

    def constantUpdate1(self):
        global movements
        global indexes
        if self.validador3(6) == True or self.validador() == True:
            movements[2].config(text="→",state=NORMAL)
        else:
            movements[2].config(text="‼",state=DISABLED)
            movements[0].config(text="←",state=NORMAL)


    def constantUpdate2(self):
        global movements
        global indexes

        if self.validador2(0) == True or self.validador() == True:
            movements[0].config(text="←",state=NORMAL)
        else:
            movements[0].config(text="‼",state=DISABLED)

            movements[2].config(text="→",state=NORMAL)

########################################################################################################################

########################################################################################################################
#Validations#

    def validador(self):
        global Matriz
        for i in range(len(Matriz)):
            for j in range(len(Matriz[0])):
                if Matriz[i][j] != 0:
                    return False
        return True
    
    def validador2(self,index):
        global indexes
        global Matriz
        for i in range(len(Matriz)):
            for j in range(indexes[index],indexes[index]+7):
                if Matriz[i][j] == 1 or Matriz[i][j] == 2:
                    return True
        return False

    def validador3(self,index):
        global indexes
        global Matriz
        for i in range(len(Matriz)):
            for j in range(indexes[index]-6,indexes[index]+1):
                if Matriz[i][j] == 1 or Matriz[i][j] == 2:
                    return True
        return False                    

########################################################################################################################
#Creates Labels for names, etc...# 

    def labelAddtion(self):
        global indexesAux
        global actualColumns
        n=2
        num=3
        for i in indexesAux:
            if self.modo == "AI":
                labelactualColumns=tkinter.Label(self.mainFrame,text=str(i),
                                        width=10,height =2,fg="DarkOrchid4")
                labelactualColumns.grid(row=1,column=n)
                n+=1
            else:
                if self.actualT == True:
                    labelactualColumns=tkinter.Label(self.mainFrame,text=str(i),
                                            width=10,height =2,fg="red")
                    labelactualColumns.grid(row=1,column=n)
                    n+=1
                elif self.actualT == False:
                    labelactualColumns=tkinter.Label(self.mainFrame,text=str(i),
                                            width=10,height =2,fg="blue")
                    labelactualColumns.grid(row=1,column=n)
                    n+=1
        for elem in actualColumns:
            if self.modo == "AI":
                n=2
                labelindexes=tkinter.Label(self.mainFrame,text=str(elem),
                                        width=5,height =5,fg="DarkOrchid4")
                labelindexes.grid(row=num,column=1)
                num+=1
            else:
                if self.actualT == True:
                    n=2
                    labelindexes=tkinter.Label(self.mainFrame,text=str(elem),
                                            width=5,height =5,fg="red")
                    labelindexes.grid(row=num,column=1)
                    num+=1
                elif self.actualT == False:
                    n=2
                    labelindexes=tkinter.Label(self.mainFrame,text=str(elem),
                                            width=5,height =5,fg="blue")
                    labelindexes.grid(row=num,column=1)
                    num+=1
########################################################################################################################

########################################################################################################################
#WINNER#

    def champ(self):
        global winners
        if self.modo != "AI":
            if self.actualT == True:
                    if self.line1(1) == True or self.line2(1) == True or self.line3(1)==True or self.line4(1) == True:
                        messagebox.showinfo(title="We have a winner", message="Congratulations! " + "\n" +  self.p1 + " is the Winner")
                        if self.p1 in winners:
                            winners[self.p1] +=1
                            try:
                                fo = open("Connect4\leaderboard.txt", "w")  
                                fo.write (str(winners))
                                fo.close()
                                newSave = [MatrizBase,True,"X","Y","mode"]
                                fo = open("Connect4\game.txt", "w")  
                                fo.write (str(newSave))
                                fo.close()
                            except:
                                print("ERROR WHEN SAVING")
                        else:
                            actualPlayers = {self.p1:1}
                            winners.update(actualPlayers)
                            try:
                                fo = open("Connect4\leaderboard.txt", "w")  
                                fo.write (str(winners))
                                fo.close()
                                newSave = [MatrizBase,True,"X","Y","mode"]
                                fo = open("Connect4\game.txt", "w")  
                                fo.write (str(newSave))
                                fo.close()
                            except:
                                print("ERROR WHEN SAVING")
                        self.destroy()
            elif self.actualT == False:  
                if self.modo != "AI":  
                    if self.line1(2) == True or self.line2(2) == True or self.line3(2)==True or self.line4(2) == True:
                        messagebox.showinfo(title="We have a winner", message="Congratulations! " + "\n" +  self.p2 + " is the Winner")
                        if self.p2 in winners:
                            winners[self.p2] += 1 
                            try:
                                fo = open("Connect4\leaderboard.txt", "w")  
                                fo.write (str(winners))
                                fo.close()
                                newSave = [MatrizBase,True,"X","Y","mode"]
                                fo = open("Connect4\game.txt", "w")  
                                fo.write (str(newSave))
                                fo.close()
                            except:
                                print("ERROR WHEN SAVING")
                        else:
                            actualPlayers = {self.p2:1}
                            winners.update(actualPlayers)
                            try:
                                fo = open("Connect4\leaderboard.txt", "w") 
                                fo.write (str(winners))
                                fo.close()
                                newSave = [MatrizBase,True,"X","Y","mode"]
                                fo = open("Connect4\game.txt", "w")  
                                fo.write (str(newSave))
                                fo.close()
                            except:
                                print("ERROR WHEN SAVING")
                        self.destroy()

########################################################################################################################
#MATRIX LINES AND COLUMS#

    #Vertical
    def line1(self,actual): 
        global Matriz 
        matriz=Matriz
        for j in range(len(Matriz[0])):
            for i in range(len(Matriz)-3):
                if matriz[i][j] == actual:
                    if matriz[i+1][j] == actual and matriz[i+2][j] == actual and matriz[i+3][j] == actual:
                        return True
        return False
    
    #Horizontal
    def line2(self,numero):
        global Matriz 
        matriz=Matriz
        for i in range(len(Matriz)):
            for j in range(len(Matriz[0])-3):
                if matriz[i][j] == numero:
                    if matriz[i][j+1] == numero and matriz[i][j+2] == numero and matriz[i][j+3] == numero:
                        return True
 
        return False

    #Diagonal
    def line3(self,numero):
        global Matriz 
        matriz=Matriz
        for i in range(len(Matriz)-3):
            for j in range(len(Matriz[0])-3):
                if matriz[i][j] == numero:
                    if matriz[i+1][j+1] == numero and matriz[i+2][j+2] == numero and matriz[i+3][j+3] == numero:
                        return True
        return False

    #Diagonal
    def line4(self,numero):
        global Matriz 
        matriz=Matriz#para no cambiar nombres xd
        #recorre la matriz buscando lineas de 4 un

        for i in range(len(Matriz)-3):
            for j in range(4,len(Matriz[0])):
                if matriz[i][j] == numero:
                    #Lineas verticales
                    if matriz[i+1][j-1] == numero and matriz[i+2][j-2] == numero and matriz[i+3][j-3] == numero:
                        return True
########################################################################################################################

########################################################################################################################
#MATRIX MADE BY:teacher #
    def create_buttons(self):
        global Matriz 
        for i in range(3,9): 
            for j in range(2,9): 
                btn = tkinter.Button(self.mainFrame,text="a",bg="white",
                                     width=10,height =5,fg="white")
                btn.grid(row=i, column=j)
                boton[i-3][j-2] = btn

    def eachButton(self):
        global redsB
        global actualT
        if self.modo != "AI":
            self.bgxb = 'green'
        else:
            self.bgxb = 'DarkOrchid4'
        for i in range(2,9):
            btn = tkinter.Button(self.mainFrame,text="Insert",bg=self.bgxb,
                                     width=10,height =5,fg="white")
            btn.grid(row=2,column=i)
            redsB[i-2]=btn
        redsB[0].config(command = self.c0_byTeacher)
        redsB[1].config(command = self.c1_byTeacher)
        redsB[2].config(command = self.c2_byTeacher)
        redsB[3].config(command = self.c3_byTeacher)
        redsB[4].config(command = self.c4_byTeacher)
        redsB[5].config(command = self.c5_byTeacher)
        redsB[6].config(command = self.c6_byTeacher)
          
    def teacherPintaTablero(self):
        global boton
        global indexes
        global actualColumns
        if self.modo == "AI":
            self.bgxf = 'orange'
            self.bgxp = 'DarkOrchid4'
        else:
            self.bgxp = 'red'
            self.bgxf = 'blue' 
        for j in range(len(actualColumns)):
            for i in range(len(indexes)):
                if Matriz[j][indexes[i]] == 1:
                    boton[j][i].config(bg=self.bgxp)
                elif Matriz[j][indexes[i]] == 2:
                    boton[j][i].config(bg=self.bgxf)
                else:
                    boton[j][i].config(bg="white")
                    
    def forPlaying(self,col):
        res=0
        for elem in col:
            if elem == 0:
                res+=1
            else:
                return res-1
        return res 

    def getColumn(self,M, col):
        column = []

        for fila in M:
            column.append(fila[col])
        return column

    def c0_byTeacher(self):
        global Matriz
        global indexes
        index=indexes[0]
        if self.actualT:
            if Matriz[5][index] == 0:
                Matriz[5][index]=1
            else:
                placeToPlay=self.forPlaying(self.getColumn(Matriz,index))
                if Matriz[placeToPlay][index]==0:
                    Matriz[placeToPlay][index]=1
        else:
            if Matriz[5][index] == 0:
                Matriz[5][index]=2
            else:
                placeToPlay=self.forPlaying(self.getColumn(Matriz,index))
                if Matriz[placeToPlay][index]==0:
                    Matriz[placeToPlay][index]=2

        self.champ()
        self.actualT = not self.actualT

        self.constantUpdate()                
        self.teacherPintaTablero()
        self.labelAddtion()
        self.buttonMovement()

        if self.modo=="AI":
            time.sleep (0.1)
            self.AIG()
        else:
            self.actualTurn(self.actualT)

    def c1_byTeacher(self):
        global Matriz
        global indexes
        index=indexes[1]
        if self.actualT:
            if Matriz[5][index] == 0:
                Matriz[5][index]=1
            else:
                placeToPlay=self.forPlaying(self.getColumn(Matriz,index))
                if Matriz[placeToPlay][index]==0:
                    Matriz[placeToPlay][index]=1
        else:
            if Matriz[5][index] == 0:
                Matriz[5][index]=2
            else:
                placeToPlay=self.forPlaying(self.getColumn(Matriz,index))
                if Matriz[placeToPlay][index]==0:
                    Matriz[placeToPlay][index]=2
                else:
                    return "no hay campo bro"
        self.champ()
        self.actualT = not self.actualT

        self.constantUpdate()                
        self.teacherPintaTablero()
        self.labelAddtion()
        self.buttonMovement()

        if self.modo=="AI":
            time.sleep (0.1)
            self.AIG()
        else:
            self.actualTurn(self.actualT)

    def c2_byTeacher(self):
        global Matriz
        global indexes
        index=indexes[2]
        if self.actualT:
            if Matriz[5][index] == 0:
                Matriz[5][index]=1
            else:
                placeToPlay=self.forPlaying(self.getColumn(Matriz,index))
                if Matriz[placeToPlay][index]==0:
                    Matriz[placeToPlay][index]=1
        else:
            if Matriz[5][index] == 0:
                Matriz[5][index]=2
            else:
                placeToPlay=self.forPlaying(self.getColumn(Matriz,index))
                if Matriz[placeToPlay][index]==0:
                    Matriz[placeToPlay][index]=2

        self.champ()
        self.actualT = not self.actualT

        self.constantUpdate()        
        self.teacherPintaTablero()
        self.labelAddtion()
        self.buttonMovement()
        
        if self.modo=="AI":
            time.sleep (0.1)
            self.AIG()
        else:
            self.actualTurn(self.actualT)
     
    def c3_byTeacher(self):
        global Matriz
        global indexes
        index=indexes[3]
        if self.actualT:
            if Matriz[5][index] == 0:
                Matriz[5][index]=1
            else:
                placeToPlay=self.forPlaying(self.getColumn(Matriz,index))
                if Matriz[placeToPlay][index]==0:
                    Matriz[placeToPlay][index]=1
                else:
                    return "no hay campo bro"
        else:
            if Matriz[5][index] == 0:
                Matriz[5][index]=2
            else:
                placeToPlay=self.forPlaying(self.getColumn(Matriz,index))
                if Matriz[placeToPlay][index]==0:
                    Matriz[placeToPlay][index]=2
                else:
                    return "no hay campo bro"
        self.champ()
        self.actualT = not self.actualT

        self.constantUpdate()        
        self.teacherPintaTablero()
        self.labelAddtion()
        self.buttonMovement()
        
        if self.modo=="AI":
            time.sleep (0.1)
            self.AIG()
        else:
            self.actualTurn(self.actualT)
      
    def c4_byTeacher(self):
        global Matriz
        global indexes
        index=indexes[4]
        if self.actualT:
            if Matriz[5][index] == 0:
                Matriz[5][index]=1
            else:
                placeToPlay=self.forPlaying(self.getColumn(Matriz,index))
                if Matriz[placeToPlay][index]==0:
                    Matriz[placeToPlay][index]=1
        else:
            if Matriz[5][index] == 0:
                Matriz[5][index]=2
            else:
                placeToPlay=self.forPlaying(self.getColumn(Matriz,index))
                if Matriz[placeToPlay][index]==0:
                    Matriz[placeToPlay][index]=2
        self.champ()
        self.actualT = not self.actualT

        self.constantUpdate()
        self.teacherPintaTablero()
        self.labelAddtion()
        self.buttonMovement()
        
        if self.modo=="AI":
            time.sleep (0.1)
            self.AIG()
        else:
            self.actualTurn(self.actualT)
            
    def c5_byTeacher(self):
        global Matriz
        global indexes
        index=indexes[5]
        if self.actualT:
            if Matriz[5][index] == 0:
                Matriz[5][index]=1
            else:
                placeToPlay=self.forPlaying(self.getColumn(Matriz,index))
                if Matriz[placeToPlay][index]==0:
                    Matriz[placeToPlay][index]=1
        else:
            if Matriz[5][index] == 0:
                Matriz[5][index]=2
            else:
                placeToPlay=self.forPlaying(self.getColumn(Matriz,index))
                if Matriz[placeToPlay][index]==0:
                    Matriz[placeToPlay][index]=2
        self.champ()
        self.actualT = not self.actualT
        self.constantUpdate()
        self.teacherPintaTablero()
        self.labelAddtion()
        self.buttonMovement()
        
        if self.modo=="AI":
            time.sleep (0.1)
            self.AIG()
        else:
            self.actualTurn(self.actualT)
 
    def c6_byTeacher(self):
        global Matriz
        global indexes
        index=indexes[6]
        if self.actualT:
            if Matriz[5][index] == 0:
                Matriz[5][index]=1
            else:
                placeToPlay=self.forPlaying(self.getColumn(Matriz,index))
                if Matriz[placeToPlay][index]==0:
                    Matriz[placeToPlay][index]=1
        else:
            if Matriz[5][index] == 0:
                Matriz[5][index]=2
            else:
                placeToPlay=self.forPlaying(self.getColumn(Matriz,index))
                if Matriz[placeToPlay][index]==0:
                    Matriz[placeToPlay][index]=2
        self.champ()
        self.actualT = not self.actualT 
        
        self.constantUpdate()      
        self.teacherPintaTablero()
        self.labelAddtion()
        self.buttonMovement()
        self.eachButton()

        if self.modo=="AI":
            time.sleep (0.1)
            self.AIG()
        else:
            self.actualTurn(self.actualT)
########################################################################################################################

########################################################################################################################
    def AIG(self):
        global indexes
        global actualT
        if self.actualT == False:
            if self.AI_aux(1) != -1:
                j=self.AI_aux(1)
                self.toPress(j)
            elif self.AI_auxs(1) != -1:
                j=self.AI_auxs(1)
                try:
                    self.toPress(j) 
                except:
                    self.toPress(j-4) 
            else:
                self.toAI()
            self.teacherPintaTablero()
            self.teacherPintaTablero()
            if self.line1(1) == True or self.line2(1) == True or self.line3(1)==True or self.line4(1) == True:
                messagebox.showinfo(title="We have a winner", message="Damn you human!")
                newSave = [MatrizBase,True,"X","Y","mode"]
                fo = open("Connect4\game.txt", "w")  #crea el file si no existe
                fo.write (str(newSave))
                fo.close()
                self.destroy()
            elif self.line1(2) == True or self.line2(2) == True or self.line3(2)==True or self.line4(2) == True:
                messagebox.showinfo(title="We have a winner",message="The invention has surpassed its creator!")
                newSave = [MatrizBase,True,"X","Y","mode"]
                fo = open("Connect4\game.txt", "w")  #crea el file si no existe
                fo.write (str(newSave))
                fo.close()
                self.destroy()
            self.champ
            self.actualT=not self.actualT
        
    def toPress(self,game):
        global Matriz
        index=game
        if Matriz[5][index] == 0:
                Matriz[5][index]=2
        else:
            placeToPlay=self.forPlaying(self.getColumn(Matriz,index))
            if Matriz[placeToPlay][index]==0:
                Matriz[placeToPlay][index]=2
            else:
                self.toAI()
        self.teacherPintaTablero()
         
    def toAI(self):
        global actualT
        ramdom=random.randint(0,6)
        classCall=self.toPress(ramdom)

    def AI_aux(self,num):
        global Matriz
        global indexes 
        matriz=Matriz
        for j in range(len(Matriz[0])):
            for i in range(len(Matriz)-2):
                if matriz[i][j] == num:
                    #Lineas verticales
                    if matriz[i+1][j] == num and matriz[i+2][j] == num:
                        return j
        return -1
    
    def AI_auxs(self,numero):
        global Matriz 
        matriz=Matriz
        for i in range(len(Matriz)):
            for j in range(len(Matriz[0])-2):
                if matriz[i][j] == numero:
                    if matriz[i][j+1] == numero and matriz[i][j+2] == numero:
                        try:
                            if matriz[i][j+3] == 0:
                                return j+3
                            elif matriz[i][j-1]==0:
                                if j==-1:
                                    return j+3
                                return j-1
                        except:
                            if matriz[i][j-1]==0:
                                if j==-1:
                                    return j+3
                                return j-1
        return -1

menu = Tk()
classCall = Main(master=menu)
menu.mainloop()