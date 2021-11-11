chovendo = True

print ("Hoje estou com as roupas " + ("secas" , "molhadas") [chovendo])
print ("hoje estou com as roupas " + ("molhadas" if chovendo else "secas."))