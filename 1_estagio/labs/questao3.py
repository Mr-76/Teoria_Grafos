from jgrapht.properties import has_multipleedges, has_selfloops
def tipos_grafos (g):
  resultado = []
  if has_multipleedges(g):
    return ["Multigrafo"]
  elif has_selfloops(g):
    return ["Pseudografo"]
  else:
    resultado.append("Simples")
    if len(g.vertices) == 0:
      resultado.append("Nulo")
      return resultado
    if len(g.vertices) == 1:
      resultado.append("Trivial")
      return resultado
    else:
      return resultado


