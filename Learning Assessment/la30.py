import tkinter as tk

name = "Justin PALO Somine"
section = "BSIT 2-ABC"
root = tk.Tk()
root.title("BASIC TKINTER WIDGETS")
root.geometry("500x300")
root.configure(bg="Khaki")

frame = tk.Frame(root)
frame.pack(pady=20)

label = tk.Label(frame, text= (f"OOP LA30 {name}, {section}"))
label.grid(row=0, column=0, padx=100, pady=100)

counter = 0
def display_txt():
    global counter
    print(f"{counter} One Punh Man")
    counter += 1

button = tk.Button(root,text="Run", command=display_txt)
button.pack(pady=10)

root.mainloop()