from tkinter import *
from tkinter import ttk
from os.path import exists
from tkinter import messagebox

def leer():
    if(not exists("hrs.txt")):
        tmp=open("hrs.txt", "x")
        tmp.close()
    arr=[]
    with open("hrs.txt", "r") as arch:
        for linea in arch:
            arr.append(linea)
    return arr
    

raiz=Tk()
raiz.title("Creador de nomina v1.0")
raiz.geometry("800x350")

lbl_id=Label(raiz, text="ID")
lbl_id.place(x=25, y=60)
ent_id=Entry(raiz)
ent_id.place(x=20, y=80, width=150)
lbl_hrs_d=Label(raiz, text="Hrs diurnas")
lbl_hrs_d.place(x=25, y=110)
ent_hrs_d=Entry(raiz)
ent_hrs_d.place(x=20, y=130, width=150)
lbl_hrs_n=Label(raiz, text="Hrs Nocturnas")
lbl_hrs_n.place(x=25, y=160)
ent_hrs_n=Entry(raiz)
ent_hrs_n.place(x=20, y=180, width=150)

tree=ttk.Treeview(raiz, columns=("#1", "#2", "#3", "#4"))
tree.heading("#0", text="ID")
tree.column("#0", width=70, stretch=False, minwidth=0)
tree.heading("#1", text="Hrs diurnas")
tree.column("#1", width=100, stretch=False)
tree.heading("#2", text="Hrs nocturnas")
tree.column("#2", width=100, stretch=False)
tree.heading("#3", text="Pago bruto")
tree.column("#3", width=150, stretch=False)
tree.heading("#4", text="Accion")
tree.column("#4", width=100, stretch=False)


tree.place(x=210, y=60)
def clear_tree():
   for item in tree.get_children():
      tree.delete(item)

def inser(arr:list):
    if(len(arr) != 0):
        for obj in arr:
            asd=obj.split(",")
            #print(asd)
            tree.insert('', END, text=asd[0], values=(asd[1], asd[2], asd[3], asd[4]))
            #tree.configure()

def mostrar():
    reg=leer()
    inser(reg)
def insertar():
    if(not ent_id.get() or not ent_hrs_d.get() or not ent_hrs_n.get()):
        messagebox.showerror("Campos vacios", "Existen campos vacios, por favor llenarlos antes de insertar")
        return
    pago_d=int(ent_hrs_d.get())*10
    pago_n=int(ent_hrs_n.get())*20
    pago_total=pago_d+pago_n
    accion=""
    if((int(ent_hrs_d.get())+int(ent_hrs_n.get()))<20):
        accion="BAJA INMEDIATA"
    else:
        accion="no accion"
    nstr=ent_id.get()+","+ent_hrs_d.get()+","+ent_hrs_n.get()+","+str(pago_total)+"("+str(pago_d)+"+"+str(pago_n)+"),"+accion
    print(nstr)
    with open("hrs.txt", "a") as file:
        file.write(nstr+"\n")
    clear_tree()
    reg=leer()
    inser(reg)

btn_acept=Button(raiz, text="Añadir", command=insertar)
btn_acept.place(x=70, y=220)
mostrar()
raiz.resizable(False, False)
raiz.mainloop()