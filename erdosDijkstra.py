from grafos3daa import *

grafo_erdos = grafoErdosRenyi(30,90)
grafo_erdos.guardar_grafo2("grafo_erdos30.gv")
grafo_erdos.guardar_grafo_dijkstra(6, "grafo_dijkstra30.gv")

#distancia_mas_corta = grafo_erdos.Dijkstra(6)
#print(distancia_mas_corta)

#for nodo, distancia in distancia_mas_corta.items():
 #   print(f"Nodo {nodo} tiene una distancia de {distancia} desde el nodo fuente.")

grafo_erdos = grafoErdosRenyi(250,350)
grafo_erdos.guardar_grafo2("grafo_erdos250.gv")
grafo_erdos.guardar_grafo_dijkstra(28, "grafo_dijkstra250.gv")
