import random

def failist_to_dict(f: str):
    riik_pealinn = {}  
    pealinn_riik = {}  
    riigid = []  
    file = open(f, 'r', encoding="utf-8-sig")
    for line in file:
        k, v = line.strip().split('-')
        riik_pealinn[k] = v  
        pealinn_riik[v] = k  
        riigid.append(k)
    file.close()
    return riik_pealinn, pealinn_riik, riigid


def getByPealinn(riik_pealinn, to_search_pealinn):
    for riik, pealinn in riik_pealinn.items():
        if pealinn == to_search_pealinn:
            return riik


def fix(riik_pealinn):
    riik = input("Sisesta vale riik: ")
    if riik not in riik_pealinn:
        print("Hüvasti")
        return

    new_riik = input("Sisesta õige riik: ")
    new_pealinn = input("Sisesta õige pealinn: ")
    riik_pealinn.pop(riik)
    riik_pealinn[new_riik] = new_pealinn
    file = open("TextFile.txt", "a", encoding="utf-8-sig")
    file.write(f"{new_riik}-{new_pealinn}")
    file.close()

def getRandom(riik_pealinn):
    i = random.randint(0, len(riik_pealinn.keys()) - 1)
    riik = list(riik_pealinn.keys())[i]
    return riik, riik_pealinn[riik]


def game(riik_pealinn):
    score = 0
    for i in range(10):
        riik, pealinn = getRandom(riik_pealinn)
        i = random.randint(0, 1)
        if i == 0:
            gues_pealinn = input(f"Sisenege {riik} pealinna: ")
            if pealinn == gues_pealinn:
                print("sul on punkt")
                score += 1
        else:
            gues_riik = input(f"Sisenege {pealinn} riigi: ")
            if riik == gues_riik:
                print("sul on punkt")
                score += 1

    print(f"Teie koguskoor {score}. Täpsus {score / 10 * 100}%")