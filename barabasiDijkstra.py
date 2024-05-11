from grafos3daa import *

grafo_barabasi = grafoBarabasiAlbert(30,2)
grafo_barabasi.guardar_grafo2("grafo_barabasi30.gv")
grafo_barabasi.guardar_grafo_dijkstra(6, "grafo_dijkstra30.gv")



grafo_barabasi = grafoBarabasiAlbert(250,2)
grafo_barabasi.guardar_grafo2("grafo_barabasi250.gv")
grafo_barabasi.guardar_grafo_dijkstra(28, "grafo_dijkstra250.gv")