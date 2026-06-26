#INPUT
verbo= input("ingresa el verbo:")
#PROCESS
#lista
pronombres= ['yo', 'tu', 'el', 'nosotros', 'vosotros', 'ellos']
#diccionario
terminaciones= {
    "ar": ["o", "as", "a", "amos", "ais", "an"],
    "er": ["o", "es", "e", "emos", "eis", "en"],
    "ir": ["o", "es", "e", "imos", "is", "en"]
}
#sacar raiz del verbo (primeras dos letras del verbo) y el final (ultimas dos letras del verbo)
#ejemplo: AMAR, RAIZ= AM, FINAL= AR
raiz_delverbo= verbo[:-2]
final_delverbo= verbo[-2:]

#buscar sus respectivas terminaciones del verbo y guardarla en una lista
finaldelverbo_lista= terminaciones[final_delverbo]

for index, pronombre in enumerate(pronombres):
    terminacion= finaldelverbo_lista[index]
#OUTPUT
    print(f"{pronombre} {raiz_delverbo}{terminacion}")