#########################################
#
#         100pt - Working with Canvas
#
#########################################


# Add a button called "Right"
# Make it so that when you press the buttons, the oval moves to the left or right

from Tkinter import *
root = Tk()
# Create our drawpad and oval
drawpad = Canvas(root, width=480,height=320, background='white')
oval = drawpad.create_oval(160,160,320,320, fill="red")

class MyApp:
	def __init__(self, parent):
	        # Make sure the drawpad is accessible from inside the function
	        global drawpad
		self.myParent = parent  
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()
		
		self.button1 = Button(self.myContainer1)
		self.button1.configure(text="Left", background= "green")
		self.button1.grid(row=0,column=0)
		
	        # Add a second button!
		self.myContainer2 = Frame(parent)
		self.myContainer2.pack()		
		self.button2 = Button(self.myContainer2)
		self.button2.configure(text="Right", background= "red")
		self.button2.grid(row=0,column=0)
						
		# "Bind" an action to the first button												
		self.button1.bind("<Button-1>", self.button1Click)
		# Create the code to bind an action to the second button
		# Do not change "<Button-1>"
		self.button2.bind("<Button-1>", self.button1Click)
		  
		# This creates the drawpad - no need to change this 
		drawpad.pack()
		

		
	def button1Click(self, event):   
		# Make the oval move to the left!
                # "global" makes sure that we can access our oval and our drawpad
		global oval
		global drawpad
	
	# Add the event handler for the second button to make it move right!
	def button2Click(self, event):   
		# Make the oval move to the right!
                # "global" makes sure that we can access our oval and our drawpad
		global oval
		global drawpad
		
		#i started crying at this point. Tears.
	        global direction
                x1, y1, x2, y2 = drawpad.coords(circle)
                if x2 > drawpad.winfo_widtj():
                    direction = 1
            #Move our oval object by the value of direction
                drawpad.move(circle, 0, direction)
            # Wait for 1 millisecond, then recursively call our animate function
                drawpad.after(1, animate)
        def animate():
            global direction
            x1, y1, x2, y2 = drawpad.coords(circle)
            if x2 > drawpad.winfo_widtj(): 
                direction = -1
            #Move our oval object by the value of direction
            drawpad.move(circle, 0, direction)
            # Wait for 1 millisecond, then recursively call our animate function
            drawpad.after(1, animate)
		
myapp = MyApp(root)
root.mainloop()