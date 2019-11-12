"""#3.a
def vinnerlag(hjemmelag, bortelag, hjemmemaal, bortemaal):
    if hjemmemaal>bortemaal:
        return hjemmelag
    elif hjemmemaal==bortemaal:
        return "uavgjort"
    else:
        return bortelag
def forkort_lagliste(lagliste):
    return list(set(lagliste))

def legg_inn_null_maal(lagliste):
    ordbok = {}
    for lag in lagliste:
        ordbok[lag] = 0
    return ordbok

def ekstraher_lagliste(fn):
    lagnavn = []
    #home, away, homegoal, awaygoal
    file = open(fn, "r")
    for line in file:
        linelist = line.split()
        lagnavn.append(linelist[0])
        lagnavn.append(linelist[1])
    return lagnavn
    file.close()


def regn_poengsum(fn):
    laggoals = []
    lagnavnListe = ekstraher_lagliste(fn)
    typerLag = forkort_lagliste(lagnavnListe)

    ordbok = legg_inn_null_maal(typerLag)
    #home, away, homegoal, awaygoal
    
    file = open(fn, "r")
    for line in file:
        linelist = line.split()


        lagnavn.append(linelist[2])
        lagnavn.append(linelist[3])
        if linelist[0] ==
"""
def minst(t1, t2, t3):
    return min(t1,t2,t3)
print(minst(5,10,2))
    

