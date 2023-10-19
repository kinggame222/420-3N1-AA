import tkinter as tk


def initialisation():
    print("initialisation")

    t.title("Mon premier programme")
    t.geometry("800x600")
    t.iconbitmap("jeuxAlma.ico")
    gr = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    l1 = tk.Label(t, text="Hello World", font=("Arial", 20), fg="red")
    l2 = tk.Label(t, text="Hello World2", font=("Arial", 20), fg="red")

    e1 = tk.Entry(t)

    l1.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
    l2.grid(row=0, column=1)
    e1.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)

    bnt1 = tk.Button(t, text="Quitter", command=t.destroy)
    bnt1.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)


if __name__ == '__main__':
    t = tk.Tk()
    initialisation()
    t.mainloop()
