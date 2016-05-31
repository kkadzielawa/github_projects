from connectfour import *
from minimax import *
from player import *
from utility import *
from Tkinter import *
from tkMessageBox import *

# MINIMAX DIALOG

def minimax_dialog(playernum):
	def createminimax(playernum):
		global minimax_instance
		ply_int = int(ply.get())
		twoscore_int = int(twoscore.get())
		threescore_int = int(threescore.get())
		root2.destroy()
		minimax_instance = MinimaxPlayer(playernum=playernum, ply_depth=ply_int, utility=SimpleUtility(twoscore_int, threescore_int))
		

	root2 = Tk()
	
	Label(root2, text="Ply depth").grid(row=0, column=0)
	Label(root2, text="Two score").grid(row=1, column=0)
	Label(root2, text="Three score").grid(row=2, column=0)
	ply = StringVar()
	twoscore = StringVar()
	threescore = StringVar()
	ply.set('4')
	twoscore.set('1')
	threescore.set('5')
	Entry(root2, textvariable=ply).grid(row=0, column=1)
	Entry(root2, textvariable=twoscore).grid(row=1, column=1)
	Entry(root2, textvariable=threescore).grid(row=2, column=1)
	Button(root2, text="OK", command=lambda playernum=playernum: createminimax(playernum)).grid(row=3, column=0, columnspan=2)
	mainloop()
	return minimax_instance


# SELECT PLAYERS

root = Tk()
Label(root, text="Player 1").grid(row=0, column=0)
Label(root, text="Player 2").grid(row=0, column=1)
p1choice = IntVar()
p2choice = IntVar()
Radiobutton(root, text="Human", variable=p1choice, value=0).grid(row=1, column=0)
Radiobutton(root, text="Random", variable=p1choice, value=1).grid(row=2, column=0)
Radiobutton(root, text="Minimax", variable=p1choice, value=2).grid(row=3, column=0)
Radiobutton(root, text="Human", variable=p2choice, value=0).grid(row=1, column=1)
Radiobutton(root, text="Random", variable=p2choice, value=1).grid(row=2, column=1)
Radiobutton(root, text="Minimax", variable=p2choice, value=2).grid(row=3, column=1)



def start():
	global p1, p2
	if (p1choice.get() > 0) and (p2choice.get() > 0):
		showwarning("Error", "At least one of the players needs to be human")
		return
	if p1choice.get() == 0:
		p1 = 'Human'
	elif p1choice.get() == 1:
		p1 = RandomPlayer(playernum=1)
	else:
		root.destroy()
		p1 = minimax_dialog(1) #MinimaxPlayer(playernum=1, ply_depth=4, utility=SimpleUtility(1, 5))
	if p2choice.get() == 0:
		p2 = 'Human'
	elif p2choice.get() == 1:
		p2 = RandomPlayer(playernum=2)
	else:
		root.destroy()
		p2 = minimax_dialog(2) #MinimaxPlayer(playernum=2, ply_depth=4, utility=SimpleUtility(1, 5))
	root.destroy()

Button(root, text="Start game", command=start).grid(row=4, column=0, columnspan=2)

mainloop()


# GAME
board = ConnectFour()

root = Tk()
canvas = Canvas(root, width=700, height=600)

def draw_board():
		for i in range(6):
			for j in range(7):
				if board.get_position(i, j) == 1:
					canvas.create_oval(100*j, 100*(5-i), 100*(j+1), 100*(5-i+1), fill="orange") 
				if board.get_position(i, j) == 2:
					canvas.create_oval(100*j, 100*(5-i), 100*(j+1), 100*(5-i+1), fill="blue")

w = None

if p1 == 'Human':
	human = 1
else:
	human = 2

def buttonclick(j):
	global w, human
	if w != None:
		return
	if board.get_position(5, j) != None:
		return
	board.play_turn(human, j)
	draw_board()
	w = board.is_game_over()
	if w != None:
		canvas.create_line(100*board.winning_column+50, 100*(5-board.winning_row)+50, 100*board.winning_column+50+board.winning_step_col*300, 100*(5-board.winning_row)+50-board.winning_step_row*300) #(row, column, step_row, step_col)
		showinfo('Game over','Player %i won!' % w)
		return
	if p2 != 'Human':
		p2.play_turn(board)
		draw_board()
		canvas.create_oval(100*board.last_column, 100*(5-board.last_row), 100*(board.last_column+1), 100*(5-board.last_row+1), fill="royal blue") 
	if p1 != 'Human':
		p1.play_turn(board)
		draw_board()
		canvas.create_oval(100*board.last_column, 100*(5-board.last_row), 100*(board.last_column+1), 100*(5-board.last_row+1), fill="gold")  
	w = board.is_game_over()
	if w != None:
		canvas.create_line(100*board.winning_column+50, 100*(5-board.winning_row)+50, 100*board.winning_column+50+board.winning_step_col*300, 100*(5-board.winning_row)+50-board.winning_step_row*300) #(row, column, step_row, step_col)
		showinfo('Game over','Player %i won!' % w)
		return
	if p1 == 'Human' and p2 == 'Human':
		human = 3 - human
	
	
for j in range(7):
	Button(root, text=str(j), command=lambda j=j:buttonclick(j)).grid(row=0, column=j)

canvas.grid(row=1, column=0, columnspan=7)

for i in range(8):
	canvas.create_line(100*i, 0, 100*i, 600)

for i in range(7):
	canvas.create_line(0, 100*i, 700, 100*i)

if p1 != 'Human':
	p1.play_turn(board)
	draw_board()
	
mainloop()
	
