from mcpi.minecraft import Minecraft #carga las funciones del API

mc = Minecraft.create() #crea la conexion con Minecraft


posicion = mc.player.getPos() # devuelve tres valores: x, y, z

mc.postToChat(posicion.x)


x, y , z = mc.player.getPos()

mc.postToChat(x)
