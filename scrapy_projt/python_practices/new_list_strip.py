s = '\n Surface de la terrasse\n \n 32\n\n \n \n m²\n \n \n mètres carrés\n \n \n \n'

print([line.strip() for line in s.split('\n') if line.strip()])
