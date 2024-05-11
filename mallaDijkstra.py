from grafos3daa import *

grafo_malla = grafoMalla(5,6)
grafo_malla.guardar_grafo2("grafo_malla30.gv")
grafo_malla.guardar_grafo_dijkstra("2-2", "grafo_dijkstra30.gv")



grafo_malla = grafoMalla(25,10)
grafo_malla.guardar_grafo2("grafo_malla250.gv")
grafo_malla .guardar_grafo_dijkstra("5-5", "grafo_dijkstra250.gv")