from grafos3daa import *

grafo_gilbert = grafoGilbert(30,0.10)
grafo_gilbert.guardar_grafo2("grafo_gilbert30.gv")
grafo_gilbert.guardar_grafo_dijkstra(6, "grafo_dijkstra30.gv")



grafo_gilbert = grafoGilbert(250,0.005)
grafo_gilbert.guardar_grafo2("grafo_gilbert250.gv")
grafo_gilbert.guardar_grafo_dijkstra(28, "grafo_dijkstra250.gv")