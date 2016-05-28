#def shutdown(self):
 #   import subprocess
  #  subprocess.call(["shutdown", "-f", "-s", "-t", "60"])
#import tkMessageBox
#tkMessageBox.showinfo(title="Greetings", message="Hello World!")
from Tkinter import Label, Tk
root = Tk()
prompt = 'hello'
label1 = Label(root, text=prompt, width=len(prompt))
label1.pack()
def close_after_20s():
    root.destroy()
x=1
while (x==1):
    root.mainloop()
    root.after(2000, close_after_20s)
