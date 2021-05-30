import re
text="""LID - E164 [pii]
LID - 10.3390/antiox9020164 [doi]
AB  - Although prickly pear fruits have become an important part of the Canary diet,
      their native varieties are yet to be characterized in terms of betalains and
      phenolic compounds.
FAU - Gomez-Maqueo, Andrea
AU  - Gomez-Maqueo A
AUID- ORCID: 0000-0002-0579-1855

PG  - 1-13
LID - 10.1007/s00442-020-04624-w [doi]
AB  - Recent observational evidence suggests that nighttime temperatures are increasing
      faster than daytime temperatures, while in some regions precipitation events are 
      becoming less frequent and more intense.
CI  - (c) 2020 Production and hosting by Elsevier B.V. on behalf of Cairo University.
FAU - Farag, Mohamed A
AU  - Farag MA

PG  - 3044
LID - 10.3389/fmicb.2019.03044 [doi]
AB  - Microbial symbionts account for survival, development, fitness and evolution of
      eukaryotic hosts. These microorganisms together with their host form a biological
      unit known as holobiont.

AU  - Flores-Nunez VM
AD  - Departamento de Ingenieria Genetica, Centro de Investigacion y de Estudios
      Avanzados del Instituto Politecnico Nacional, Irapuato, Mexico.
"""

result = re.findall(r"AB\W*-\W*([^-]+(?=\n))", text)

print(result)
print([" ".join(map(str.strip, i.split('\n'))) for i in result])
print([" ".join(map(str.strip,i.split('\n'))) for i in result])
