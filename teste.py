from tkinter import *
from tkinter import messagebox

estoque = {
    "Casquinha": 10,
    "Sorvete de Chocolate": 5,
    "Sorvete de Morango": 8
}

precos = {
    "Casquinha": 2.00,
    "Sorvete de Chocolate": 5.00,
    "Sorvete de Morango": 5.00
}

pedido = []

def adicionar_item(item):
    if estoque[item] <= 0:
        messagebox.showerror("Estoque Insuficiente", f"O item '{item}' está em falta.")
        return
    pedido.append(item)
    atualizar_total()

def finalizar_venda():
    if not pedido:
        messagebox.showwarning("Pedido vazio", "Nenhum item foi adicionado ao pedido.")
        return
    for item in pedido:
        if estoque[item] <= 0:
            messagebox.showerror("Estoque Insuficiente", f"O item '{item}' está em falta.")
            return
    for item in pedido:
        estoque[item] -= 1
    total = sum(precos[item] for item in pedido)
    cupom = "\n--- CUPOM FISCAL (SIMULADO) ---\n"
    for item in pedido:
        cupom += f"{item} - R${precos[item]:.2f}\n"
    cupom += f"TOTAL: R${total:.2f}\nStatus: PAGAMENTO APROVADO\n-------------------------------"
    messagebox.showinfo("Venda Finalizada", cupom)
    pedido.clear()
    atualizar_total()
    atualizar_estoque()

def atualizar_total():
    total = sum(precos[item] for item in pedido)
    total_label.config(text=f"Total: R${total:.2f}")

def atualizar_estoque():
    for widget in estoque_frame.winfo_children():
        widget.destroy()
    for item in estoque:
        Label(estoque_frame, text=f"{item}: {estoque[item]} no estoque").pack(anchor="w")

root = Tk()
root.title("Sistema de Sorveteria")
root.geometry("400x450")

Label(root, text="Selecione os produtos", font=("Arial", 14)).pack(pady=10)

for item in precos:
    Button(root, text=f"{item} - R${precos[item]:.2f}", width=30,
           command=lambda i=item: adicionar_item(i)).pack(pady=2)

total_label = Label(root, text="Total: R$0.00", font=("Arial", 12))
total_label.pack(pady=10)

Button(root, text="Finalizar Venda", bg="green", fg="white", font=("Arial", 12),
       command=finalizar_venda).pack(pady=5)

Label(root, text="Estoque Atual:", font=("Arial", 12, "bold")).pack(pady=10)
estoque_frame = Frame(root)
estoque_frame.pack()
atualizar_estoque()

root.mainloop()
