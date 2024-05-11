from grafos3daa import *

grafo_geo = grafoGeografico(30,0.10)
grafo_geo.guardar_grafo2("grafo_geo30.gv")
grafo_geo.guardar_grafo_dijkstra(6, "grafo_dijkstra30.gv")



grafo_geo = grafoGeografico(250,0.10)
grafo_geo.guardar_grafo2("grafo_geo250.gv")
grafo_geo.guardar_grafo_dijkstra(28, "grafo_dijkstra250.gv")