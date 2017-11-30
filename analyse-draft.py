# il faudrait mettre univ en paramètre de toutes mes fonctions ?

univ = reconstitue(nom, t);

def CPUnumber(univ, t) : ## assez inutile ?
    "renvoie le nombre de CPUs présents dans la liste CPU[] de l'univers à la date t"
    return len(univ.CPU) ;


def colonisationRate(univ, t) :
    "renvoie le taux de cases remplies dans la liste Memoire[] de l'univers à la date t"
    instructionsNb = 0;
    for i in univ.Memory :
        if i != None :
            instructionsNb += 1;
    return (instructionsNb/len(univ.Memory)) ;


def individus_boucles(t) : # pas fini du tout !
    "??? en utilisant la méthose donnée par le tuteur : un CPU-test parcourt le code, on identifie un individu-boucle comme la plus grande boucle possible."
    # je ne sais plus s'il faut pouvoir retourner au début depuis la fin, où juste arriver à la fin depuis le début
    univ = reconstitue(t);
    N = len(univ.Memoire);   # devrait être une variable globale ?
    loopStart = [None] * N;
    test = CPU() ;
    for i in range(N) :
        if loopStart[i] == None :
            loopStart[i] = i;
            debut_courant = i;
            test.index = i;
            while ?? :
                test.execute();
                if ?? :
                    debut_boucle[test.index] = debut_courant;
            test.clear() ; #si cette méthode n'existe pas, on peut juste remplacer par test=CPU();
    return debut_boucle;


def rateCreationCPUs(univ, t, interval) :
    "retourne le nombre moyen de CPUs créés par CPU existant et par an pendant l'intervalle de temps de longueur intervalle et commençant à la date t"
    univ = univ(t); # à écrire
    nbCreated = 0;
    date = t;
    currentCPUnumber = len(univ.CPU);
    while date < t+interval :
        univ.forward(1) ;
        nb_created += len(univ.CPU)/currentCPUnumber - 1 ; # ou faire une fonction qui calcule le nb de CPUs crées à la date t ?
        currentCPUnumber = len(univ.CPU);
    return (nb_created/interval) ;


def densityCPU(univ, t) :
    "affiche et renvoie la densite de CPU par site d'instruction occupé" #on pourrait faire par site d'instruction tout court ?
    d = len(univ.CPU) / (colonisationRate(univ)*len(univ.Memory)) ;
    print("La densité de CPU est {}, soit 1 CPU pour {} instructions".format(d, 1/d));
    return d;


def nbIndividuals(t) :
    "renvoie le nombre d'individus-boucles"

def nbSpecies(t) :
    "renvoie le nombre de codes différents parmi tous les individus-boucles identifiés"

def speciesDistance(??) :
    "renvoie la distance d'édition entre les codes des deux espèces données en paramètre"
