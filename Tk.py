import tkinter as tk

interface = tk.Tk()

def close():
    button['text'] = 'See you later...'
    button['text'] = 'Please wait...'
    button['state'] = 'disabled'
    interface.after(2000, interface.destroy)

button = tk.Label(text='Glad to see you')
button.pack()

button = tk.Button(text='exit', command = close)
button.pack()

interface.protocol('WM_DELETE_WINDOW', close)

interface.mainloop()
