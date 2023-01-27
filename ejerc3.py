from tkinter import *
from tkinter import ttk
from os.path import exists
from tkinter import messagebox
from sqlite3 import *

try:
    con=connect(r"db\db.sqlite3")
except Error as e:
    print(e)




# def leer():
#     if(not exists("menu.txt")):
#         tmp=open("menu.txt", "x")
#         tmp.close()
#     arr=[]
#     with open("menu.txt", "r") as arch:
#         for linea in arch:
#             arr.append(linea)
#     return arr

def fetch(col:int):
    result=con.execute("SELECT * FROM MENU")
    res=[]
    for reg in result:
        res.append(reg[col])
    return res

raiz=Tk()
raiz.title("Restaurante v0.1")
raiz.geometry("750x350")
anadir=True
total=0
id=0
lbl_menu=Label(raiz, text="Menu")
lbl_menu.place(x=30, y=40)

tree=ttk.Treeview(raiz, columns=("#1", "#2", "#3"))
tree.heading("#0", text="ID")
tree.column("#0", width=50, stretch=False, minwidth=0)
tree.heading("#1", text="Nombre")
tree.column("#1", width=160, stretch=False)
tree.heading("#2", text="Precio")
tree.column("#2", width=100, stretch=False)
tree.heading("#3", text="Tipo")
tree.column("#3", width=100, stretch=False)
tree.place(x=20, y=60)

lsfoods=fetch(1)
lbl_add=Label(raiz, text="Añadir orden")
lbl_add.place(x=450, y=40)
cbb_prod=ttk.Combobox(
    raiz,
    state="readonly",
    values=lsfoods
)
cbb_prod.place(x=450, y=60)
cbb_prod.current(0)

lbl_edit=Label(raiz, text="Añadir/editar items del menú")
lbl_edit.place(x=480, y=90)

lbl_nomb=Label(raiz, text="Nombre del platillo")
lbl_nomb.place(x=450, y=120)

lbl_prec=Label(raiz, text="Precio del platillo")
lbl_prec.place(x=450, y=170)

lbl_tip=Label(raiz, text="Tipo del platillo")
lbl_tip.place(x=450, y=220)

ent_nomb=Entry(raiz)
ent_nomb.place(x=440, y=140, width=150)

ent_prec=Entry(raiz)
ent_prec.place(x=440, y=190)

cbb_tip=ttk.Combobox(
    raiz,
    state="readonly",
    values=["postre", "carne", "pescado", "aperitivo"]
)
cbb_tip.place(x=440, y=240)
cbb_tip.current(0)
def inser_tree():
    arr=con.execute("SELECT * FROM MENU")
    
    for obj in arr:
        #print(asd)
        tree.insert('', END, text=obj[0], values=(obj[1], obj[2], obj[3]))
            #tree.configure()

inser_tree()
def clear_tree():
   for item in tree.get_children():
      tree.delete(item)

def add_DB(nombre:str, precio: int, tipo:str):
    # if(not ent_nomb.get() or not ent_prec.get()):
    #     messagebox.showerror("Error al añadir", "Hay un ")
    query="INSERT INTO MENU(nombre, precio, tipo) VALUES('"+nombre+"',"+str(precio)+",'"+tipo+"')"
    con.execute(query)
    con.commit()

def upd_DB(nombre:str, precio: int, tipo:str, id:int):
    query="UPDATE MENU SET nombre='"+nombre+"', precio="+str(precio)+", tipo='"+tipo+"' WHERE id="+str(id)
    print(query)
    con.execute(query)
    con.commit()

def del_DB(id:int):
    query="DELETE FROM MENU WHERE id="+str(id)
    con.execute(query)
    con.commit()

def add_click():
    id=cbb_prod.current()+1
    precio=0
    global total
    quer="SELECT * FROM MENU WHERE ID="+str(id)
    preres=con.execute(quer)
    for i in preres:
        precio=i[2]
    total=total+precio
    

def fin():
    global total
    messagebox.showinfo("Tus ganancias este mes", "Tus ganancias fueron: "+str(total))
    total=0
    cbb_tip.current(0)

def edit_click():

    if(not ent_nomb.get() or not ent_prec.get()):
        messagebox.showerror("Error al añadir o editar", "Hay uno o varios campos vacios")
        return
    global anadir
    global id
    if(anadir):
        add_DB(ent_nomb.get(), int(ent_prec.get()), cbb_tip.get())
    else:
        upd_DB(ent_nomb.get(), int(ent_prec.get()), cbb_tip.get(), id)
        anadir=True
    tree.selection_remove(*tree.selection())
    ent_nomb.delete(0, 'end')
    ent_prec.delete(0, 'end')
    clear_tree()
    inser_tree()
    cbb_tip.current(0)



def del_click():
    global id
    global anadir
    del_DB(id)
    clear_tree()
    inser_tree()
    ent_nomb.delete(0, 'end')
    ent_prec.delete(0, 'end')
    anadir=True
    btn_del.place_forget()
    cbb_tip.current(0)

btn_del=Button(raiz, text="Eliminar registro", command=del_click)
btn_del.place(x=620, y=230)
btn_del.place_forget()

def tree_clk(a):
    global anadir
    global id
    
    try:
        iid_slcted=tree.selection()[0]
    except IndexError as e:
        return
    anadir=False
    ent_nomb.delete(0, 'end')
    ent_prec.delete(0, 'end')
    ent_nomb.insert(0, tree.item(iid_slcted)["values"][0])
    ent_prec.insert(0, tree.item(iid_slcted)["values"][1])
    id=tree.item(iid_slcted)["text"]
    if tree.item(iid_slcted)["values"][2]=='postre':
        cbb_tip.current(0)
    elif tree.item(iid_slcted)["values"][2]=='carne':
        cbb_tip.current(1)
    elif tree.item(iid_slcted)["values"][2]=='pescado':
        cbb_tip.current(2)
    elif tree.item(iid_slcted)["values"][2]=='aperitivo':
        cbb_tip.current(3)
    else:
        cbb_tip.current(0)
    btn_del.place(x=620, y=230)
    #print(id)

tree.bind("<<TreeviewSelect>>", tree_clk)

btn_anadir=Button(raiz, text="Añadir orden", command=add_click)
btn_anadir.place(x=610, y=60)

btn_edit=Button(raiz, text="Añadir o editar", command=edit_click)
btn_edit.place(x=620, y=200)

btn_fin=Button(raiz, text="Terminar mes", command=fin)
btn_fin.place(x=600, y=300)



raiz.resizable(False, False)
raiz.mainloop()