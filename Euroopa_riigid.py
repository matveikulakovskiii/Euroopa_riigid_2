from module import *

riik_pealinn = failist_to_dict("TextFile.txt")[0]
while True:
    action = int(input("0 – programmist väljumine.\n 1 – Vaadake riike ja nende pealinnu.\n 2 - Uurige välja riik või pealinn.\n 3 – vale sõna muutmine.\n 4 – mäng.\n"))
    if action == 0:
        exit(0)
    elif action == 1:
        print(riik_pealinn)
    elif action == 2:
        getBy = input("Uurige riigi või pealinna järgi (riik/pealinn): ")
        if getBy == "riik":
            riik = input("Sisesta riik: ")
            print(riik_pealinn.get(riik))
        else:
            pealinn = input("Sisesta pealinn: ")
            print(getByPealinn(riik_pealinn, pealinn))
    elif action == 3:
        fix(riik_pealinn)
    elif action == 4:
        game(riik_pealinn)