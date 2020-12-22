from logics import *
from tkinter import Frame,Label,CENTER,messagebox
from constants import *
ai=__import__('2048_ai')

class game2048(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.run=True
        self.grid()
        self.master.title("2048")

        self.master.bind("<Down>",self.key_down)
        self.master.bind("<Up>", self.key_down)
        self.master.bind("<Right>", self.key_down)
        self.master.bind("<Left>", self.key_down)
        self.master.bind("<Key>", self.key_down)
        self.commands={key_up:move_up,key_down:move_down,key_left:move_left,key_right:move_right}
        self.grid_cells=[]
        self.init_grid()
        self.init_matrix()
        self.update_grid_cells()
        messagebox.showinfo("Instruction", "Use arrow keys to play and PRESS P if you want the ai to play.")
        self.mainloop()


    def init_grid(self):
        background=Frame(self,bg=background_color_game,width=size,height=size)
        background.grid()
        for i in range(grid_len):
            grid_row=[]
            for j in range(grid_len):
                cell=Frame(background,bg=background_color_cell_empty,width=size/grid_len,height=size/grid_len)
                cell.grid(row=i,column=j,padx=grid_padding,pady=grid_padding)
                t=Label(master=cell,text="",bg=background_color_cell_empty,justify=CENTER,font=FONT,width=5,height=2)
                t.grid()
                grid_row.append(t)
            self.grid_cells.append(grid_row)

    def init_matrix(self):
        self.matrix=start_game()
        add_new_2(self.matrix)
        add_new_2(self.matrix)
    def update_grid_cells(self):
        for i in range(grid_len):
            for j in range(grid_len):
                num=self.matrix[i][j]
                if num==0:
                    self.grid_cells[i][j].configure(text="",bg=background_color_cell_empty)
                else:
                    self.grid_cells[i][j].configure(text=str(num),bg=BACKGROUND_COLOR_DICT[num],fg=CELL_COLOR_DICT[num])
        self.update_idletasks()
    def key_down(self,event):
        if repr(event.char)==ai_key:
            valid=True
            self.run=True
            while valid and self.run:
                self.matrix,valid=ai.mcst_move(self.matrix,searches_per_move,max_depth)
                if valid:
                    self.matrix=add_new_tile(self.matrix)
                    self.update_grid_cells()
                    cs = check_state(self.matrix)
                    if cs == "w":
                        messagebox.showinfo("Game Over!", "AI Won!")
                        self.run = False

                    elif cs == "l":
                        messagebox.showinfo("Game Over!", "AI Lost!")
                        
                        self.run = False
        else:
            key=event.keysym
            if self.run and key in self.commands:
                self.matrix,changed,score=self.commands[key](self.matrix)


                if changed:
                    add_new_tile(self.matrix)
                    self.update_grid_cells()

                    cs=check_state(self.matrix)
                    if cs=="w":
                        self.grid_cells[1][1].configure(text="You",bg=background_color_cell_empty)
                        self.grid_cells[1][2].configure(text="Win!", bg=background_color_cell_empty)
                        self.run=False

                    elif cs=="l":
                        self.grid_cells[1][1].configure(text="You", bg=background_color_cell_empty)
                        self.grid_cells[1][2].configure(text="Lose!", bg=background_color_cell_empty)
                        self.run = False

gamegrid=game2048()

