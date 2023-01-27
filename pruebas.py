from sqlite3 import *
try:
    con=connect(r"db\db.sqlite3")
except Error as e:
    print(e)

# con.execute('''CREATE TABLE MENU(
#         id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#         nombre VARCHAR (60),
#         precio int,
#         tipo VARCHAR (50)
#         )
# ''')
try:

    # con.execute('''INSERT INTO MENU(nombre, precio, tipo) VALUES
    #         ("marisco (?)",9999,"postre"),
    #         ("El vacio",3,"carne"),
    #         ("EL CUBO",213,"postre"),
    #         ("Ensalada en forma de",32,"pescado"),
    #         ("manzana... yes",75,"aperitivo"),
    #         ("p i r a m i d e",23,"carne"),
    #         ("roca en forma de pastel",65,"aperitivo"),
    #         ("carne vampiro",43,"carne"),
    #         ("carne del lunes",23,"postre"),
    #         ("si",432,"aperitivo")
    # ''')
    # con.commit()
    #con.execute("DROP TABLE MENU")
    rows=con.execute("SELECT * FROM MENU")
    for i in rows:
        print(i)

except Error as e:
    print(e)

