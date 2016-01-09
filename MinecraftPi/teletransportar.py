from mcpi.minecraft import Minecraft #carga las funciones del API

mc = Minecraft.create() #crea la conexion con Minecraft


x, y , z = mc.player.getPos() # devuelve tres valores: x, y, z

mc.player.setPos(x, y+140, z) # recoloca al jugador más arriba

mc.postToChat("Mira para abajo")

