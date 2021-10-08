hero = "Super Man"
char = "^"
hero = hero.upper()

hero_rep = (hero.replace("","^"))
hero_final = hero_rep[1:10] + " " + hero_rep[13:18]
print(hero_final)