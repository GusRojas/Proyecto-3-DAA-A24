from grafos3daa import *

grafo_dorogov = grafoDorogovtsevMendes(30)
grafo_dorogov.guardar_grafo2("grafo_dorogov30.gv")
grafo_dorogov.guardar_grafo_dijkstra(6, "grafo_dijkstra30.gv")



grafo_dorogov = grafoDorogovtsevMendes(250)
grafo_dorogov.guardar_grafo2("grafo_dorogov250.gv")
grafo_dorogov.guardar_grafo_dijkstra(28, "grafo_dijkstra250.gv")