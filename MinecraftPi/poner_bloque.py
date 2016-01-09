from mcpi.minecraft import Minecraft #carga las funciones del API

mc = Minecraft.create() #crea la conexion con Minecraft


x, y , z = mc.player.getPos() # devuelve tres valores: x, y, z


mc.setBlock(x+1, y, z, 1) # pone un bloque de piedra junto jugador
