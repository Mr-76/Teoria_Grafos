v = 1
vizinhos_v = [g0.opposite(e,v) for e in g0.edges_of(v)]

print(vizinhos_v)

#print((g0.vertices-[0]))

tudo = vizinhos_v + [v]


def retorna_resto(g0,lista):
  """
  g0 -- grafo
  lista -- lista de procura
  """

  resto = []
  for procurado in g0.vertices:
    if procurado not in lista:
      resto.append(procurado)
    else:
      continue
  return resto


resto = retorna_resto(g0,tudo)
print(vizinhos_v)
print(tudo)
print(resto)



draw_graph(g0,layout,vertex_font_color="white",vlabel='label',v_attrs=v_g0,
           vset=[vizinhos_v,[v],resto],vsetcolor=['blue','red','orange'],vsetlabel=['v_Azul','v_Vermelho',"v_Laranja"],
           eset=[[0,1,2],[3]],esetcolor=['cyan','black'],esetlabel=['Azul','Preto'])
