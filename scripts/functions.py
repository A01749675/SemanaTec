import csv    
menus={
    "Café de la calle 86":["Cafe del dia","Cappuccino","Matcha latte", "Caramel macchiato", "Chocolate", "Mango dragonfruit refresher", "Mocha", "Espresso"],
    "Casa Nostra":["Spaguetti Carbonara","Lasagna de la Nonna","Pizza Hawaiana", "Esalada de la casa","Gnoki 4 formaggi", "Vino blanco", "Ravioles al pesto"],
    "Crepas del Cuadro":["Cajeta", "Nutella", "Manzana con canela", "Boloñesa", "Hawaiana"," Suiza","Queso con Zarzamora"],
    "Hamburguesas de Fuentes": ["BBQ","Hawaina","Tradicional", "Doble", "Con tocino",]
}
empresas=["Café de la calle 86", "Casa Nostra", "Crepas del Cuadro", "Hamburguesas de Fuentes"]
nump=0
cliente=["Santiago Chevez Trejo", "17/07/03", "Av.Lomas Verdes #415 Naucalpan"]
def menu_empresa(empresa):
    global menus
    return menus[empresa]

def lista_empresas():
    global empresas
    return empresas

def hacer_pedido(empresa,productos,fecha,estatus,direccion):
    global nump
    nump+=1
    with open('write.csv', 'a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([empresa,nump,productos,fecha,estatus,direccion])
def info_cliente():
    global cliente
    return cliente
        

