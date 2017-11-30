# il faudrait mettre univ en paramètre de toutes mes fonctions ?


def nb_CPUs(t) : ## assez inutile ?
    "renvoie le nombre de CPUs présents dans la liste CPU[] de l'univers à la date t"
    univ = reconstitue(t);
    return len(univ.CPU) ;


def taux_colonisation(t) :
    "renvoie le taux de cases remplies dans la liste Memoire[] de l'univers à la date t"
    univ = reconstitue(t);
    nb_instructions = 0;
    for i in univ.Memoire :
        if i != None :       # ou is not ??
            nb_instructions += 1;
    return (nb_instructions/len(univ.Memoire)) ;


def individus_boucles(t) : # pas fini du tout !
    "??? en utilisant la méthose donnée par le tuteur : un CPU-test parcourt le code, on identifie un individu-boucle comme la plus grande boucle possible."
    # je ne sais plus s'il faut pouvoir retourner au début depuis la fin, où juste arriver à la fin depuis le début
    univ = reconstitue(t);
    N = len(univ.Memoire);   # devrait être une variable globale ?
    debut_boucle = [None] * N;
    test = CPU() ;
    for i in range(N) :
        if debut_boucle[i] == None :
            debut_boucle[i] = i;
            debut_courant = i;
            test.index = i;
            while ?? :
                test.execute();
                if ?? :
                    debut_boucle[test.index] = debut_courant;
            test.clear() ; #si cette méthode n'existe pas, on peut juste remplacer par test=CPU();
    return debut_boucle;


def taux_creation_CPUs(univ, t, intervalle) :
    "retourne le nombre moyen de CPUs créés par CPU existant et par an pendant l'intervalle de temps de longueur intervalle et commençant à la date t"
    univ = univ(t); # à écrire
    nb_crees = 0;
    date = t;
    nb_CPUs_courant = len(univ.CPU);
    while date < t+intervalle :
        univ.avance(1) ;
        nb_crees += len(univ.CPU)/nb_CPUs_courant - 1 ; # ou faire une fonction qui calcule le nb de CPUs crées à la date t ?
        nb_CPUs_courant = len(univ.CPU);
    return (nb_crees/intervalle) ;


def densite_CPU(t) :
    "affiche et renvoie la densite de CPU par site d'instruction occupé" #on pourrait faire par site d'instruction tout court ?
    univ = reconstitue(t) ;
    d = len(univ.CPU) / (taux_colonisation*len(univ.Memoire)) ;
    print("La densité de CPU est {}, soit 1 CPU pour {} instructions".format(d, 1/d));
    return d;


def nb_individus(t) :
    "renvoie le nombre d'individus-boucles"

def nb_especes(t) :
    "renvoie le nombre de codes différents parmi tous les individus-boucles identifiés"

def distance_especes(??) :
    "renvoie la distance d'édition entre les codes des deux espèces données en paramètre"
