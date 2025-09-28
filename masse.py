def indice_masse(poids,taille):
    imc=poids/(taille)**2
    if imc<18.5:
        print(" sa categorie est maigre")
    elif 18.5<imc<25:
        print("sa categorie est normal ")
    elif imc>25 and imc <30:
        print("sa categorie est surpoids")
    elif imc>30:
        print("sa categorie est obése")
    return imc
poids=float(input("saisir le poids :"))
taille=float(input("saisir la taille :"))
im=indice_masse(poids,taille)
print(f"sa taille est{im :.2f}")
