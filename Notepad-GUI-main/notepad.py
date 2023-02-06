from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import datetime
import time
import os
def newFile():
	global file
	root.title("Untitled-Notepad")
	file=None
	TextArea.delete(1.0,END)
def openFile():
	global file
	file = askopenfilename(defaultextension=".txt", filetypes = [("All Files", "*.*"), 
				("Text Documents", "*.txt")])

	if file == "":
		file=None
	else:
		root.title(os.path.basename(file) + "-Notepad")
		TextArea.delete(1.0,END)
		f = open(file,"r")
		TextArea.insert(1.0,f.read())
		f.close()
def saveasFile():
	global file
	if file==None:
		file = asksaveasfilename(initialfile='Untitled.txt',defaultextension='.txt',filetypes = [("All Files", "*.*"), 
				("Text Documents", "*.txt")])
		if file=="":
			file = None
		else:
			#save it as a new file
			f = open(file,'w')
			f.write(TextArea.get(1.0,END))
			f.close()
			root.title(os.path.basename(file)+'-Notepad')
			print("File is saved")
	else:
		f = open(file,'w')
		f.write(TextArea.get(1.0,END))
		f.close()
		root.title(os.path.basename(file)+'-Notepad')
		print("File is saved")

def saveFile():
	f = open(file,'w')
	f.write(TextArea.get(1.0,END))
	f.close()
	root.title(os.path.basename(file)+'-Notepad')
	print("File is saved")

def find_fun(*args):
	def find():
		TextArea.tag_remove('matches','1.0',tk.END)
		word = find_input.get()
		matches = 0
		if word:
			start_pos = '1.0'
			while True:
				start_pos = TextArea.search(word,start_pos,stopindex=tk.END)
				if not start_pos:
					break
				end_pos = f"{start_pos}+{len(word)}c"
				TextArea.tag_add("matches",start_pos,end_pos)
				matches+=1
				start_pos=end_pos
				TextArea.tag_config('matches',foreground='red',background='blue')
	find_popup = tk.Toplevel()
	find_popup.geometry('450x200')
	find_popup.title('find word')
	find_popup.resizable(0,0)
	#fram for find
	find_fram = ttk.LabelFrame(find_popup,text='Find')
	find_fram.pack(pady=20)
	#label
	text_find = ttk.Label(find_fram,text='find')
	find_input = ttk.Entry(find_fram,width=30)
	find_button = ttk.Button(find_fram,text='find',command=find)
	text_find.grid(row=0,column=0,padx=4,pady=4)
	find_input.grid(row=0,column=1,padx=4,pady=4)
	find_button.grid(row=1,column=0,padx=8,pady=4)
	
def find_and_replace():
	def find():
		TextArea.tag_remove('matches','1.0',tk.END)
		word = find_input.get()
		matches = 0
		if word:
			start_pos = '1.0'
			while True:
				start_pos = TextArea.search(word,start_pos,stopindex=tk.END)
				if not start_pos:
					break
				end_pos = f"{start_pos}+{len(word)}c"
				TextArea.tag_add("matches",start_pos,end_pos)
				matches+=1
				start_pos=end_pos
				TextArea.tag_config('matches',foreground='red',background='blue')
	def replace():
		word = find_input.get()
		replace_text = replace_input.get()
		content = TextArea.get(1.0,tk.END)
		new_content = content.replace(word,replace_text)
		TextArea.delete(1.0,tk.END)
		TextArea.insert(1.0,new_content)

	find_popup = tk.Toplevel()
	find_popup.geometry('450x200')
	find_popup.title('find word')
	find_popup.resizable(0,0)
	#fram for find
	find_fram = ttk.LabelFrame(find_popup,text='Find and Replace')
	find_fram.pack(pady=20)
	#label
	text_find = ttk.Label(find_fram,text='find')
	text_replace = ttk.Label(find_fram,text='Replace')
	#entry box
	find_input = ttk.Entry(find_fram,width=30)
	replace_input = ttk.Entry(find_fram,width=30)
	#button
	find_button = ttk.Button(find_fram,text='find',command=find)
	replace_button = ttk.Button(find_fram,text='Replace',command=replace)
	#text label grid
	text_find.grid(row=0,column=0,padx=4,pady=4)
	text_replace.grid(row=1,column=0,padx=4,pady=4)
	#entry grid
	find_input.grid(row=0,column=1,padx=4,pady=4)
	replace_input.grid(row=1,column=1,padx=4,pady=4)
	#button grid
	find_button.grid(row=2,column=0,padx=8,pady=4)
	replace_button.grid(row=2,column=1,padx=8,pady=4)

def quitApp():
	root.destroy()
def cut():
	TextArea.event_generate(("<<Cut>>"))
def copy():
	TextArea.event_generate(("<<Copy>>"))
def paste():
	TextArea.event_generate(("<<Paste>>"))
def about():
	showinfo("Notepad","Notepad for CS384 project")

def word_count():
	global file
	f = open(file,'r')
	string = f.read()
	x=string.split()
	res = "The word count is = "+str(len(x))
	showinfo("Word count of the file",res)
	f.close()

def char_count():
	global file
	f = open(file,'r')
	string = f.read()
	res = ""
	res = "The character count is = "+str(len(string))
	showinfo("Character count of the file",res)
	f.close()
	
def created_time():
	global file
	ctime = time.ctime(os.path.getctime(file))
	showinfo("Created time of the file is ",ctime)
def modified_time():
	global file
	mtime = time.ctime(os.path.getmtime(file))
	showinfo("modified time of the file is ",mtime)

if __name__=='__main__':
	#basic tkinter setup
	root=Tk()
	root.title("Untitled-Notepad")
	#root.wm_iconbitmap("instagram.ico")
	root.geometry("644x788")
	TextArea = Text(root,font="lucida 13")
	TextArea.pack(expand=True,fill=BOTH)
	file = None
	#now creating menubar
	MenuBar = Menu(root)
	#File menu starts
	FileMenu = Menu(MenuBar,tearoff=0)
	#To open file
	FileMenu.add_command(label="New",command=newFile)
	#To open already existing file
	FileMenu.add_command(label="Open",command=openFile)
	#To save the current file
	FileMenu.add_command(label="Save",command=saveFile)
	FileMenu.add_command(label="Save As",command=saveasFile)
	FileMenu.add_separator()
	FileMenu.add_command(label="Exit",command=quitApp)

	MenuBar.add_cascade(label="File",menu=FileMenu)
	#File menu ends
	EditMenu = Menu(MenuBar,tearoff=0)
	EditMenu.add_command(label="Cut",command=cut)
	EditMenu.add_command(label="Copy",command=copy)
	EditMenu.add_command(label="Paste",command=paste)
	EditMenu.add_command(label="Find",command=find_fun)
	EditMenu.add_command(label="Find and Replace",command=find_and_replace)
	MenuBar.add_cascade(label="Edit",menu=EditMenu)

	#stats menu starts

	StatsMenu = Menu(MenuBar,tearoff=0)
	StatsMenu.add_command(label="Word Count",command=word_count)
	StatsMenu.add_command(label="Char Count",command=char_count)
	StatsMenu.add_command(label="Created Time",command=created_time)
	StatsMenu.add_command(label="Modified Time",command=modified_time)
	MenuBar.add_cascade(label="Stats",menu=StatsMenu)

	#stats menu ends
	#help menu starts
	HelpMenu = Menu(MenuBar,tearoff=0)
	HelpMenu.add_command(label="About Notepad",command=about)
	MenuBar.add_cascade(label="About",menu=HelpMenu)

	#help menu ends
	root.config(menu=MenuBar)
	#adding a scroll bar
	scrollbar = Scrollbar(TextArea)
	scrollbar.pack(side=RIGHT,fill=Y)
	scrollbar.config(command=TextArea.yview)
	TextArea.config(yscrollcommand=scrollbar.set)


	root.mainloop()

