#import tikinter module
from tkinter import*
host_path='C:\Windows\System32\drivers\etc\hosts'
ip_address='127.0.0.1'
def block():
	website_list=enter_Website.get(1.0,END)
	Website=list(website_list.split(','))
	with open(host_path,'r+')as host_file:
		file_content=host_file.read()
		for web in Website:
			if web in file_content:
				display=Label(root,text='Already Blockd',font='arial')
				display.place(x=200,y=200)
			else:
				host_file.write(ip_address+''+web)
				Label(root,text="Blocked",font='arial').place(x=200,y=200)
def unblock():
	website_list=enter_Website.get(1.0,END)
	#print(website_un)
	Website=list(website_list.split(','))
	temp_f='' 
	with open(host_path,'r+')as host_file:
		file_content=host_file.read()
		#print(file_content)
		for web in Website:
			if web in file_content:
				Label(root,text=web+'Unblock\n',font='arial').place(x=350,y=200)
				with open(host_path,'r+')as website_un:
					for line in website_un:
						print('Line1:-'+line)
						if web in line:
							temp_un=ip_address+' '+web
							line=line.replace(temp_un,'')
						print('line2:-'+line)
						temp_f=temp_f+line
				with open(host_path,'w')as new_file:
					new_file.write(temp_f);
					print(temp_f)
			else:
				display=Label(root,text="Already Unblocked",font='arial')
				display.place(x=350,y=200)

def close():
	root.destroy()
#predefine class
root=Tk() 
root.title("My Blocker Website")
root.geometry('650x450')
root.maxsize(650,450)
root.minsize(650,450)
Label(root,text="WEBSITE BLOCKER",font="arial 20 bold",fg="red").pack()
Label(root,text="Developed By @Sandeeplitindia:2022",font="arial 10 bold",fg="blue").pack(side=BOTTOM)
Label(root,text="Enter Website URL:",font="arial 15 bold").place(x=80,y=90)
enter_Website=Text(root,height=2,width=30)
enter_Website.place(x=300,y=85)
b1=Button(root,text="Block",font="arial 10 bold",bg="red",command=block)
b1.place(x=300,y=125)
b2=Button(root,text="Unblock",font="arial 10 bold",bg="green",command=unblock)
b2.place(x=400,y=125)
b3=Button(root,text="Exit",font="arial 10 bold",bg="cyan",command=close)
b3.place(x=500,y=125)
root.mainloop()