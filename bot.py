import datetime
import telepot
import os
import time

global reg
reg=[]

def handle(msg):
    #registros=[]
    chat_id = msg['chat']['id']
    command = msg['text']
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#
    def start():
        try:
            bot.sendMessage(chat_id,("Bot de Parqueo"))
            bot.sendMessage(chat_id,("Puede realizar lo siguiente: \n"))
            bot.sendMessage(chat_id,("1) /ingresar (placa carro)\nIngresa carro al parqueo"))
            bot.sendMessage(chat_id,("2) /consultar (placa carrp)\nConsultar si el carro ha entrado al parqueo"))
            bot.sendMessage(chat_id,("3) /borrar (placa)\nCarro sale del parqueo"))
        except(TypeError, NameError, ValueError):
            bot.sendMessage(chat_id,"No envie una cadena donde vaa un entero")
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#
    def Ingresar_Articulo(command):
        try:
            datos=command.split()
            placa=int(datos[1])
            if len(reg)<10:
                reg.append(placa)
                bot.sendMessage(chat_id, "Aun hay parqueo disponible")
                bot.sendMessage(chat_id, ("Entro el Carro"))
                bot.sendMessage(chat_id, reg)
            else:
                bot.sendMessage(chat_id ,"ya no hay parqueo")
        except(TypeError, NameError, ValueError):
            bot.sendMessage(chat_id,"No envie una cadena donde vaa un entero")

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#
    def Consultar_Articulo(command):
        try:
            comp=command.split()
            c=int(comp[1])
            if c in reg:
                bot.sendMessage(chat_id,"El carro si esta en el parqueo")
            else:
                bot.sendMessage(chat_id, "El carro no esta en el parqueo\nLe puso llave :D")
        except(TypeError, NameError, ValueError):
            bot.sendMessage(chat_id,"No envie una cadena donde vaa un entero")
            
    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#
    def Borrar(command):#funcion para borrar un articulo
        try:
            comp=command.split()
            c=int(comp[1])
            if c in reg:
                reg.remove(c)
                bot.sendMessage(chat_id,"El carro ha salido del parqueo")
            else:
                bot.sendMessage(chat_id, "El carro no esta en el parqueo\nLe puso llave :D")
        except(TypeError, NameError, ValueError):
            bot.sendMessage(chat_id,"No envie una cadena donde vaa un entero")
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#
    lista1=['/ingresar','/consultar','/borrar']
    div=command.split()
    comparacion = []
    for item in lista1:
        if item in div:
            comparacion.append(item)
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#
    try:
        if command==("/start"):#comparo y decido que funcion se ejecutara, para el caso de /start, como no contiene valores de entrada de usuario va directo
            start()#la funcion tiene los valores de entrada del id de la persona y el objeto bot, para no utilizaro 2 veces
        elif comparacion[0]==("/ingresar"):#a esta funcion le envio command porque las cosas llegan por ejemplo
            Ingresar_Articulo(command)#/Ingresar 123(codigo) 25(cantidad) 100(precio) zapatos(nombre)
        elif comparacion[0]==("/consultar"):#para diferenciar eso hago lo del .split()
            Consultar_Articulo(command)#haci con todas las funciones similares
        elif comparacion[0]==("/borrar"):
            Borrar(command)
    except(IndexError):
        bot.sendMessage(chat_id, ("Ingreso una funcion no valida"))
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#


TOKEN=("633567832:AAGza38FnZqswxPiU6Fk0YFlGXFpORq-AdQ")
bot = telepot.Bot(TOKEN)
bot.message_loop(handle)
print ('Estoy escuchando...')


while 1:
     time.sleep(10)
