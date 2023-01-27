from tkinter import *
from tkinter import messagebox
encuestados=[]
def getstats(lista:list):
    htotales=0
    mtotales=0
    h_menores=0
    m_menores=0
    h_mayores=0
    m_mayores=0
    for encuesta in lista:
        if(encuesta[3]==1):
            htotales=htotales+1
            if(encuesta[2]<18):
                h_menores=h_menores+1
            else:
                h_mayores=h_mayores+1
        else:
            mtotales=mtotales+1
            if(encuesta[2]<18):
                m_menores=m_menores+1
            else:
                m_mayores=m_mayores+1
    
    return [[htotales, h_menores, h_mayores], [mtotales, m_menores, m_mayores]]

raiz=Tk()
num_enc=IntVar()
var=IntVar()
raiz.title("Demografias v1.1")
raiz.geometry("820x350")

lbl_progreso=Label(raiz, text="Persona: 1/50")
lbl_progreso.place(x=40, y=30)

lbl_nombre=Label(raiz, text="Nombre")
lbl_nombre.place(x=30, y=60)

ent_nom=Entry(raiz)
ent_nom.place(x=25, y=80)

lbl_edad=Label(raiz, text="Edad")
lbl_edad.place(x=30, y=110)

ent_edad=Entry(raiz)
ent_edad.place(x=70, y=110, width=50)

lbl_sexo=Label(raiz, text="Sexo")
lbl_sexo.place(x=60, y=140)

rb1=Radiobutton(raiz, text="Masculino", variable=var, value=1)
rb1.place(x=30, y=160)

rb2=Radiobutton(raiz, text="Femenino", variable=var, value=2)
rb2.place(x=30, y=190)



var.set(1)
num_enc.set(1)
live_h_lbfrm=LabelFrame(raiz, text="Estadisticas en vivo masculino", width=200, height=300)
live_h_lbfrm.place(x=190, y=20)

live_m_lbfrm=LabelFrame(raiz, text="Estadisticas en vivo femenino", width=200, height=300)
live_m_lbfrm.place(x=400, y=20)

liv_gral_lbfrm=LabelFrame(raiz, text="Estadisticas generales en vivo", width=200, height=300)
liv_gral_lbfrm.place(x=610, y=20)

lbl_tot_m=Label(live_h_lbfrm, text="Total de hombres: 0")
lbl_tot_m.place(x=10, y=200)

lbl_porm_m=Label(live_h_lbfrm, text="% mayores de edad: 0%")
lbl_porm_m.place(x=10, y=220)

lbl_porme_m=Label(live_h_lbfrm, text="% menores de edad: 0%")
lbl_porme_m.place(x=10, y=240)

lbl_tot_f=Label(live_m_lbfrm, text="Total de mujeres: 0")
lbl_tot_f.place(x=10, y=200)

lbl_porm_f=Label(live_m_lbfrm, text="% mayores de edad: 0%")
lbl_porm_f.place(x=10, y=220)

lbl_porme_f=Label(live_m_lbfrm, text="% menores de edad: 0%")
lbl_porme_f.place(x=10, y=240)

lbl_tot=Label(liv_gral_lbfrm, text="Total de encuestados: 0")
lbl_tot.place(x=10, y=200)

lbl_porm=Label(liv_gral_lbfrm, text="% mayores de edad: 0%")
lbl_porm.place(x=10, y=220)

lbl_porme=Label(liv_gral_lbfrm, text="% menores de edad: 0%")
lbl_porme.place(x=10, y=240)

def insertar(nombre:str, edad: str, sexo: int):
    ind_reg=[]
    id=len(ind_reg)+1
    ind_reg.append(id)
    ind_reg.append(nombre)
    n_edad=int(edad)
    ind_reg.append(n_edad)
    ind_reg.append(sexo)
    encuestados.append(ind_reg)
    #print(encuestados)

def actualizar():
    
    tot_ec=len(encuestados)
    lbl_tot.config(text="Total de encuestados: "+str(tot_ec))
    stats=getstats(encuestados)
    tot_h=stats[0][0] if stats[0][0] > 0 else 1
    tot_m=stats[1][0] if stats[1][0] > 0 else 1
    lbl_tot_m.config(text="Total de hombres: "+str(stats[0][0]))
    lbl_tot_f.config(text="Total de mujeres: "+str(stats[1][0]))
    lbl_porm_m.config(text="% mayores de edad: "+str((stats[0][2]/tot_h)*100)+"%")
    lbl_porm_f.config(text="% mayores de edad: "+str((stats[1][2]/tot_m)*100)+"%")
    lbl_porm.config(text="% mayores de edad: "+str((stats[0][2]+stats[1][2])/(stats[0][0]+stats[1][0])*100)+"%")
    lbl_porme_m.config(text="% menores de edad: "+str((stats[0][1]/tot_h)*100)+"%")
    lbl_porme_f.config(text="% menores de edad: "+str((stats[1][1]/tot_m)*100)+"%")
    lbl_porme.config(text="% menores de edad: "+str(((stats[0][1]+stats[1][1])/tot_ec)*100)+"%")
    


def update():
    if(not ent_edad.get() or not ent_nom.get()):
        messagebox.showerror("Error al procesar los datos", "Uno o varios campos estan vacios, favor de llenar antes de procesar")
        return
    nombre=ent_nom.get()
    edad=ent_edad.get()
    insertar(nombre, edad, var.get())
    actualizar()
    #print(num_enc.get())
    tmp=num_enc.get()+1
    num_enc.set(tmp)
    lbl_progreso.config(text="Persona "+str(num_enc.get())+"/50")
    ent_edad.delete(0, 'end')
    ent_nom.delete(0, 'end')
    var.set(1)
    if(num_enc.get()>=50):
        btn_ing.config(state=DISABLED)
        return


btn_ing=Button(raiz, text="Aceptar", command=update)
btn_ing.place(x=60, y=220)

raiz.resizable(False, False)
raiz.mainloop()