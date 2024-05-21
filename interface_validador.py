import tkinter as tk
from tkinter import messagebox
from Validador_CPF import *

class IntercaceValidador:
    def __init__(self, root):
        self.root = root
        self.interface_GUI()

    def interface_GUI(self):
        self.label = tk.Label(self.root, text='CPF - (Apenas números): ', font='Arial 15')
        self.entry = tk.Entry(self.root, font='Arial 15', justify=tk.CENTER)
        self.label.pack(pady=10)
        self.entry.pack(pady=10)

    def verifica_flag_validador(self):
        valida_entry = ValidadorCPF(self.entry.get())
        if valida_entry.valida_cpf() == True:
            messagebox.showinfo('Validação concluída!', 'O CPF informado é válido!')
        else:
            messagebox.showerror('Validação concluída!', 'O CPF informado é inválido!')

def main():
        root = tk.Tk()
        app = IntercaceValidador(root)
        button = tk.Button(root, text='Validar', font='Arial 15', command=app.verifica_flag_validador)
        button.pack(pady=20, expand=True)
        root.mainloop()


if __name__ == "__main__":
    main()
