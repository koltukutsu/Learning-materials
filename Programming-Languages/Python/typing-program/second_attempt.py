import curses
from curses.textpad import rectangle
from glob import glob


class TypingProgram:
    def __init__(self):
        self.word_file_name: str
        self.music_file_name: str
        self.menu_choice: int
        self.max_y: int # row
        self.max_x: int # col
        self.middle_col: int
        self.middle_row: int
        self.rectangle_constant: int
        
        self.screen_row_pos: int
        
        self.screen = curses.initscr() # screen to be used
        self.max_y, self.max_x = self.screen.getmaxyx()
        self.middle_row = int(self.max_y / 2)
        self.middle_col = int(self.max_x / 2)
        
        
        self.choice = None
        TypingProgram.menu(self)
        

    def menu(self):
        curses.echo()
        
        messages = ["1-Start", "2-Choose the file", "3-Configure","q-Quit"]
        self.rectangle_constant = 1
        self.max_len = 0
        while self.choice != "q":
            for i, el in enumerate(messages):
                # TypingProgram.put_to_screen(self, el, self.middle_row + (i * 2), self.middle_col, put_rect=True)
                TypingProgram.put_to_screen(self, el, self.middle_row + (i * self.rectangle_constant), self.middle_col, put_rect=False)
                if self.max_len < len(el):
                    self.max_len = int(len(el) / 2) + 3
            else:
                # self.screen_row_pos = (i * self.rectangle_constant) + 2
                self.screen_row_pos = (i * self.rectangle_constant) + 1
            TypingProgram.put_to_screen(self, "Choose: ", self.middle_row + self.screen_row_pos, self.middle_col, put_rect = False)
            self.screen_row_pos += 1
            print(self.max_len * 2)
            TypingProgram.draw_multiple_rectangle(self, self.middle_row - 1, self.middle_col - self.max_len, self.middle_row + self.screen_row_pos, self.middle_col + self.max_len )
            
            self.choice = str(self.screen.getkey())

            if self.choice == "1":
                TypingProgram.startGame(self)

            elif self.choice == "2":
                self.word_file_name = None
                TypingProgram.fileOperatinos(self)
            elif self.choice == "c":
                self.configure = None
                TypingProgram.configureStart(self)
            else:
                pass    
            
            
    def draw_multiple_rectangle(self, row_start, col_start, row_end, col_end):
        rectangle(self.screen, row_start, col_start, row_end, col_end)
        self.screen.refresh()
    
    
    def put_to_screen(self, msg, row, col, put_rect=True, napm=False, clear=False):
        if clear:
            self.screen.clear()
            
        half_msg_len = int(len(msg) / 2)
        self.screen.addstr(row, col - half_msg_len, msg)
        
        if put_rect:
            rectangle(self.screen, row - 1, col - half_msg_len - 1, row + 1, col + half_msg_len + 1)
        self.screen.refresh()
        if napm:
            curses.napms(napm)
        if clear:
            self.screen.clear() 
            
            
    def showFiles_and_Select(self):
        self.screen.clear()
        TypingProgram.put_to_screen(self, "The files: ", self.middle_row, self.middle_col, True, False, False)
        for i, file in enumerate(glob("./*.txt")):
            file = file.split("\\")[-1]
            TypingProgram.put_to_screen(self, file, self.middle_row + 2 + i, self.middle_col, False, False, False)
        
        TypingProgram.put_to_screen(self, "Choose a file: ", self.middle_row + i + 4, self.middle_col, False)
        # self.screen.addstr(self.middle_row + i + 4, self.middle_col, "> ")
        self.word_file_name = self.screen.getstr()
        self.screen.clear()    

    
    def startGame(self):
        self.screen.clear()
        ##
        #Code
        ##
        self.screen.clear()
    

    
    def fileOperatinos(self):
        self.screen.clear()
        curses.echo()
        curses.curs_set(0)
        
        messages = ["-1- Show the files and Choose One", "-q- To turn back" ,"Choose: "]
        
        while self.word_file_name != "q":        
            for i, el in enumerate(messages):
                if i != len(messages) - 1:
                    TypingProgram.put_to_screen(self, el, self.middle_row + (i * 2), self.middle_col)
                else:
                    TypingProgram.put_to_screen(self, el, self.middle_row + (i * 2), self.middle_col, False)
            
            self.word_file_name = self.screen.getkey()
            
            if self.word_file_name == "1":
                TypingProgram.showFiles_and_Select(self)
                
            elif self.word_file_name == "q":
                TypingProgram.put_to_screen(self, "Turning back!", self.middle_row, self.middle_col, False, 1000, True)
            
            elif ".txt" in self.word_file_name:
                TypingProgram.put_to_screen(self, "Valid file!", self.middle_row, self.middle_col, False, 1500, True)
                self.word_file_name = "b"
            else:
                TypingProgram.put_to_screen(self, "Invalid Command or File Name!", self.middle_row, self.middle_col, False, 1500, True)        
        self.screen.clear()
        # if self.word_file_name 
        
        def configureStart(self):
            pass
        
TypingProgram()