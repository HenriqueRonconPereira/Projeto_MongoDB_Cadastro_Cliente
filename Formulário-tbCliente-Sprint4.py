import tkinter as tk
from tkinter import messagebox, ttk
import pymongo
from bson.objectid import ObjectId
 
# Conexão com o MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["test"]
clientes_collection = db["Clientes"]
 
# Função para inserir cliente no MongoDB
def inserir_cliente():
    nome = entry_nome.get()
    email = entry_email.get()
    telefone = entry_telefone.get()
    rua = entry_rua.get()
    numero = entry_numero.get()
    cidade = entry_cidade.get()
    estado = entry_estado.get()
    cep = entry_cep.get()
   
    if nome and email and telefone and rua and numero and cidade and estado and cep:
        cliente = {
            "nome": nome,
            "email": email,
            "telefone": telefone,
            "endereco": {
                "rua": rua,
                "numero": numero,
                "cidade": cidade,
                "estado": estado,
                "cep": cep
            }
        }
        clientes_collection.insert_one(cliente)
        messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
        limpar_campos()
        listar_clientes()
    else:
        messagebox.showwarning("Atenção", "Por favor, preencha todos os campos obrigatórios.")
 
# Função para deletar cliente selecionado
def deletar_cliente():
    try:
        selected_item = treeview.focus()  # Obtém o item selecionado
        cliente_id = treeview.item(selected_item)['values'][0]  # Pega o ID do cliente
        clientes_collection.delete_one({"_id": ObjectId(cliente_id)})
        messagebox.showinfo("Sucesso", "Cliente deletado com sucesso!")
        listar_clientes()
    except Exception as e:
        messagebox.showwarning("Erro", f"Erro ao deletar cliente: {str(e)}")
 
# Função para atualizar cliente selecionado
def atualizar_cliente():
    try:
        selected_item = treeview.focus()
        cliente_id = treeview.item(selected_item)['values'][0]
 
        nome = entry_nome.get()
        email = entry_email.get()
        telefone = entry_telefone.get()
        rua = entry_rua.get()
        numero = entry_numero.get()
        cidade = entry_cidade.get()
        estado = entry_estado.get()
        cep = entry_cep.get()
 
        if nome and email and telefone and rua and numero and cidade and estado and cep:
            clientes_collection.update_one(
                {"_id": ObjectId(cliente_id)},
                {"$set": {
                    "nome": nome,
                    "email": email,
                    "telefone": telefone,
                    "endereco": {
                        "rua": rua,
                        "numero": numero,
                        "cidade": cidade,
                        "estado": estado,
                        "cep": cep
                    }
                }}
            )
            messagebox.showinfo("Sucesso", "Cliente atualizado com sucesso!")
            limpar_campos()
            listar_clientes()
        else:
            messagebox.showwarning("Atenção", "Por favor, preencha todos os campos.")
    except Exception as e:
        messagebox.showwarning("Erro", f"Erro ao atualizar cliente: {str(e)}")
 
# Função para listar os clientes no Treeview
def listar_clientes():
    # Limpar a tabela antes de listar
    for item in treeview.get_children():
        treeview.delete(item)
 
    # Listar todos os clientes
    clientes = clientes_collection.find()
    for cliente in clientes:
        endereco = cliente["endereco"]
        treeview.insert("", tk.END, values=(
            str(cliente["_id"]),
            cliente["nome"],
            cliente["email"],
            cliente["telefone"],
            endereco["rua"],
            endereco["numero"],
            endereco["cidade"],
            endereco["estado"],
            endereco["cep"]
        ))
 
# Função para preencher os campos ao selecionar um cliente
def selecionar_cliente(event):
    selected_item = treeview.focus()
    if selected_item:
        values = treeview.item(selected_item)['values']
        if len(values) == 9:  # Verifique se temos 9 valores
            cliente_id, nome, email, telefone, rua, numero, cidade, estado, cep = values
           
            # Preencher os campos com as informações do cliente
            entry_nome.delete(0, tk.END)
            entry_nome.insert(0, nome)
            entry_email.delete(0, tk.END)
            entry_email.insert(0, email)
            entry_telefone.delete(0, tk.END)
            entry_telefone.insert(0, telefone)
            entry_rua.delete(0, tk.END)
            entry_rua.insert(0, rua)
            entry_numero.delete(0, tk.END)
            entry_numero.insert(0, numero)
            entry_cidade.delete(0, tk.END)
            entry_cidade.insert(0, cidade)
            entry_estado.delete(0, tk.END)
            entry_estado.insert(0, estado)
            entry_cep.delete(0, tk.END)
            entry_cep.insert(0, cep)
 
# Função para limpar os campos
def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)
    entry_rua.delete(0, tk.END)
    entry_numero.delete(0, tk.END)
    entry_cidade.delete(0, tk.END)
    entry_estado.delete(0, tk.END)
    entry_cep.delete(0, tk.END)
 
# Criação da interface com tkinter
root = tk.Tk()
root.title("Formulário de Cadastro de Cliente")
 
# Configurando o layout
frame_form = tk.Frame(root, padx=10, pady=10)
frame_form.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
 
# Labels e entradas para o formulário
label_nome = tk.Label(frame_form, text="Nome *")
label_nome.grid(row=0, column=0, sticky=tk.W)
entry_nome = tk.Entry(frame_form)
entry_nome.grid(row=0, column=1, padx=10, pady=5)
 
label_email = tk.Label(frame_form, text="Email *")
label_email.grid(row=1, column=0, sticky=tk.W)
entry_email = tk.Entry(frame_form)
entry_email.grid(row=1, column=1, padx=10, pady=5)
 
label_telefone = tk.Label(frame_form, text="Telefone *")
label_telefone.grid(row=2, column=0, sticky=tk.W)
entry_telefone = tk.Entry(frame_form)
entry_telefone.grid(row=2, column=1, padx=10, pady=5)
 
label_rua = tk.Label(frame_form, text="Rua *")
label_rua.grid(row=3, column=0, sticky=tk.W)
entry_rua = tk.Entry(frame_form)
entry_rua.grid(row=3, column=1, padx=10, pady=5)
 
label_numero = tk.Label(frame_form, text="Número *")
label_numero.grid(row=4, column=0, sticky=tk.W)
entry_numero = tk.Entry(frame_form)
entry_numero.grid(row=4, column=1, padx=10, pady=5)
 
label_cidade = tk.Label(frame_form, text="Cidade *")
label_cidade.grid(row=5, column=0, sticky=tk.W)
entry_cidade = tk.Entry(frame_form)
entry_cidade.grid(row=5, column=1, padx=10, pady=5)
 
label_estado = tk.Label(frame_form, text="Estado *")
label_estado.grid(row=6, column=0, sticky=tk.W)
entry_estado = tk.Entry(frame_form)
entry_estado.grid(row=6, column=1, padx=10, pady=5)
 
label_cep = tk.Label(frame_form, text="CEP *")
label_cep.grid(row=7, column=0, sticky=tk.W)
entry_cep = tk.Entry(frame_form)
entry_cep.grid(row=7, column=1, padx=10, pady=5)
 
# Botões de ação
btn_inserir = tk.Button(frame_form, text="Inserir", command=inserir_cliente, bg="lightblue", width=15)
btn_inserir.grid(row=8, column=0, padx=5, pady=5)
 
btn_atualizar = tk.Button(frame_form, text="Atualizar", command=atualizar_cliente, bg="lightgreen", width=15)
btn_atualizar.grid(row=8, column=1, padx=5, pady=5)
 
btn_deletar = tk.Button(frame_form, text="Deletar", command=deletar_cliente, bg="lightcoral", width=15)
btn_deletar.grid(row=9, column=0, padx=5, pady=5) 

btn_limpar = tk.Button(frame_form, text="Limpar", command=limpar_campos, bg="lightgray", width=15)
btn_limpar.grid(row=9, column=1, padx=5, pady=5)  
 
# Listagem de clientes à direita
frame_lista = tk.Frame(root, padx=10, pady=10)
frame_lista.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
 
columns = ("ID", "Nome", "Email", "Telefone")
treeview = ttk.Treeview(frame_lista, columns=columns, show="headings")
 
# Definindo o título das colunas
for col in columns:
    treeview.heading(col, text=col)
 
# Adicionando a barra de rolagem
scrollbar = ttk.Scrollbar(frame_lista, orient=tk.VERTICAL, command=treeview.yview)
treeview.configure(yscroll=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
 
treeview.pack(fill=tk.BOTH, expand=True)
 
# Evento para selecionar um cliente ao clicar na tabela
treeview.bind("<<TreeviewSelect>>", selecionar_cliente)
 
# Inicializando a lista de clientes
listar_clientes()
 
# Função para fechar a aplicação
def fechar():
    root.quit()
 
btn_fechar = tk.Button(root, text="Fechar", command=fechar)
btn_fechar.pack(pady=10)
 
# Iniciando o loop da interface
root.mainloop()
 