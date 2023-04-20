# Open both text files in read mode + convert to lowercase
with open("list1.txt", "r") as f1, open("list2.txt", "r") as f2:
    list1 = [serveurs.lower() for serveurs in f1.read().splitlines()] 
    list2 = [serveurs.lower() for serveurs in f2.read().splitlines()] 

# Find common results
commun = set(list1) & set(list2)

# Find unique results in list1/list2
uniques_list1 = set(list1) - commun
uniques_list2 = set(list2) - commun

# Result file
with open("resultat.txt", "w") as f3:
    # resultat unique list1
    f3.write("Liste des items presents dans list1 mais pas dans list2:\n")
    for items in uniques_list1:
        f3.write(f"{items}\n")
    f3.write("\n")
    # resultat unique list2
    f3.write("Liste des items presents dans list2 mais pas dans list1:\n")
    for items in uniques_list2:
        f3.write(f"{items}\n")

