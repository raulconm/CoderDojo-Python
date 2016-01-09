from mcpi.minecraft import Minecraft #carga las funciones del API

mc = Minecraft.create() #crea la conexion con Minecraft

mc.postToChat("Hola, ya estoy dentro")  #escribe en la barra de chat


