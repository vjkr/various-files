#Python version 2.7.1

###############################################
###############################################
########This code is for reminding user########
########to lookaway from screen for 20sec######
########across 20 feet...The message ##########
########selfdestruts after 20sec and ##########
########repeats every 20minute. ###############
########GOOD LUCK!! TAKE CARE !!###############
###############################################
###############################################


        #!!!!!!!!!FIRST SELFDETRUCT ISNT WORKING!!!!!!#
        #manually close for first display

#import time library to run delay command
import time

#infinite loop. change x=y and x<y and ending with x-=1 for finite loop
x=1
while (x==1):
#using Label library to display a message window
    
    from Tkinter import Label, Tk
    root = Tk()
#your message goes here
    prompt = 'Hey BusyBee!! Lookaway !! This message selfdestructs in 20 seconds and repaets every 20 minutes. Good Luck!!'
    label1 = Label(root, text=prompt, width=len(prompt))
    label1.pack()
    root.mainloop()
#pyhton code to sleep python using time library
    time.sleep(1200) # delays for 1200 seconds- 20min
#define a destroy to autodestruct message 20000 millisec- 20sec
    def close_after_s():
        root.destroy()
    root.after(20000, close_after_s)
