#@title  { vertical-output: true }
#@title  { run: "auto", vertical-output: true }
#@title  { vertical-output: true }
pessoa = "Maria" #@param ["Joao", "Maria", "Eduardo", "Cristina", "Otavio", "Jose"]
# Criando a instância do grafo (multigrafo, não-direcionado, não-ponderado)
# e seus dicionários vazios de vértices e arestas
g2 = jgrapht.create_graph(directed=False,weighted=False,allowing_multiple_edges=True)
v_g2 = {}
e_g2 = {}
read_multiple_CSV(g2,v_g2,e_g2,
                  vfilename='nomes.csv',vid='nome',vlabel='nome',
                  efilename='amigos.csv',esourceid='nome1',etargetid='nome2')
#print(v_g2)
#print(e_g2.keys())


def acha_key_pessoa(v_g,pessoa):
  for key_v in v_g.keys():
    if v_g[key_v]["nome"] == pessoa:
      print("found")
      print(key_v)
      key_pessoa = key_v
      return key_pessoa
      break
    else:
      continue


#print(acha_key_pessoa(v_g2,pessoa))


#key_pessoa = 0

#for key_v in v_g2.keys():
#  if v_g2[key_v]["nome"] == pessoa:
#    print("found")
#    print(key_v)
#    key_pessoa = key_v
#    break
#  else:
#    continue

lista_vizinhos = vizinhos(g2,acha_key_pessoa(v_g2,pessoa))
#print("lista",lista_vizinhos)

for vizinho in lista_vizinhos:
  print(v_g2[vizinho]["nome"])


draw_graph(g2,vlabel='nome',v_attrs=v_g2,width=11,height=11)

# Escreva aqui o seu código

