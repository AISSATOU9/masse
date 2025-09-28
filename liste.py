n=int(input("saisir le nbre de valeur : "))
a=[]
p=1
for i in range (n):
    v=int(input("saisir une valeur :"))
    a.append(v)
    p=p*v
print("le produit est",p)
