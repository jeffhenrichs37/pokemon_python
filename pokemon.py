class Pokemon:
  def __init__(self, name, type, max_health, level=5, attack_pts=20):
    self.name = name
    self.level = level
    self.type = type
    self.health = max_health
    self.max_health = max_health
    self.is_knocked_out = False
    self.xp = 0
    self.attack_pts = attack_pts

  def __repr__(self):
    return "{}".format(self.name)

  def poke_info(self):
    return "----------Poke Info----------\nName: {}\nLevel: {}\nType: {}\nHealth {} / {}\nXP: {}\nKO: {}".format(self.name, self.level, self.type, self.health, self.max_health, self.xp, self.is_knocked_out)

  def attack(self, other, damage):
    if self.is_knocked_out == True:
      return "{} is unable to battle.".format(self.name)
    else:
      if self.type == "Fire":
        if other.type == "Water" or other.type == "Fire":
          other.loss_health(self, int(damage/2))
          return "Not very effective.\n{} took a {} pt hit.".format(other.name, int(damage/2))
        else:
          other.loss_health(self, damage*2)
          return "Super Effective\n{} took a {} pt hit".format(other.name, damage*2)
      elif self.type == "Water":
        if other.type == "Water" or other.type == "Grass":
          other.loss_health(self, int(damage/2))
          return "Not very effective.\n{} took a {} pt hit.".format(other.name, int(damage/2))
        else:
          other.loss_health(self, damage*2)
          return "Super Effective\n{} took a {} pt hit".format(other.name, damage*2)
      else:
        if other.type == "Grass" or other.type == "Fire":
          other.loss_health(self, int(damage/2))
          return "Not very effective.\n{} took a {} pt hit.".format(other.name, int(damage/2))
        else:
          other.loss_health(self, damage*2)
          return "Super Effective\n{} took a {} pt hit".format(other.name, damage*2)

    

  def loss_health(self, other, loss):
    self.health -= loss
    if self.health <= 0:
      self.health = 0
      self.knocked_out(other)
    else:
      print("{} now has {} health".format(self.name, self.health)) 

  def heal(self, gain):
    self.health += gain
    if self.health > self.max_health:
      self.health = self.max_health
    print("{} now has {} health".format(self.name, self.health))

  def revive(self, healed):
    self.health = healed
    self.is_knocked_out = False
    print("{health} restored. {name} is revived.".format(name=self.name, health=self.health))

  def evolve(self):
    if self.level >= 36:
      if self == charmander:
        self.name = "Charzard"
        self.max_health = 250
        self.health = 250
        self.attack_pts = 100
        return "Charmeleon evolved into Charzard."
      elif self == squirtle:
        self.name = "Blastoise"
        self.max_health = 270
        self.health = 270
        self.attack_pts = 100
        return "Wartotle evolved into Blastoise"
      elif self == bulbasaur:
        self.name = "Venusaur"
        self.max_health = 260
        self.health = 260
        self.attack_pts = 100
        return "Ivysaur evolved into Venusaur."
    elif self.level >= 16:
      if self == charmander:
        self.name = "Charmeleon"
        self.max_health = 125
        self.health = 125
        self.attack_pts = 50
        return "Charmander evolved into Charmeleon."
      elif self == squirtle:
        self.name = "Wartotle"
        self.max_health = 135
        self.health = 135
        self.attack_pts = 50
        return "Squirtle evolved into Wartotle."
      elif self == bulbasaur:
        self.name = "Ivysaur"
        self.max_health = 130
        self.health = 130
        self.attack_pts = 50
        return "Bulbasaur evolved into Ivysaur."

  def knocked_out(self, other):
    other.xp += 25
    other.level_up()
    self.is_knocked_out = True
    return "{} is knocked out.".format(self.name)

  def level_up(self):
    if self.xp >= 100:
      self.level += 1
      self.xp = 0
      self.max_health += 5
      self.health = self.max_health
      self.attack_pts += 5
      return "{} is now a level {}".format(self.name, self.level)

  
charmander = Pokemon("Charmander", "Fire", 50,16)
squirtle = Pokemon("Squirtle", "Water", 45)  
bulbasaur = Pokemon("Bulbasuar", "Grass", 60, 17)    

print(squirtle.poke_info())
print(charmander.poke_info())
print(bulbasaur.poke_info())
print(charmander.evolve())
print(charmander.poke_info())
print(bulbasaur.evolve())
print(bulbasaur.poke_info())
bulbasaur.level = 36
print(bulbasaur.poke_info())
print(bulbasaur.evolve())
print(bulbasaur.poke_info())
squirtle.xp = 105
print(squirtle.level_up())

#print(charmander.attack(squirtle, 10))
#print(squirtle.attack(charmander, 25))
#print(charmander.poke_info())
#print(charmander.attack(squirtle, 20))

class Trainer:
  def __init__(self, name, pokemon):
    self.name = name
    self.potions = 10
    self.current_active_pokemon = pokemon[0]
    if len(pokemon) <= 6:
      self.pokemon = pokemon
    else:
      print(len(pokemon)-1)
      index = len(pokemon) - 1
      while len(pokemon) > 6:
        pokemon.pop(len(pokemon)-1)
      self.pokemon = pokemon

  def __repr__(self):
    return "-------Trainer Info----------\nName: {}\nNumber of Potions: {}\nCurrent Pokemon: {}\nPokemon: {}".format(self.name, self.potions, self.current_active_pokemon, self.pokemon)

  def use_potion(self):
    if self.current_active_pokemon.health == self.current_active_pokemon.max_health:
        return "{} is already at max health. You still have {} potions.".format(self.current_active_pokemon.name, self.potions)
    else:
      if self.potions > 0:
        self.potions -= 1
        self.current_active_pokemon.heal(30)
        if self.potions == 0:
          return " {} just ran of potions.".format(self.name)
        else:
          return "{} now has {} potions".format(self.name, self.potions)
      else:
        return "{} doesn't have any potions to use.".format(self.name)

  def attack(self, other):
    self.current_active_pokemon.attack(other.current_active_pokemon, self.current_active_pokemon.attack_pts)
    

  def switch(self, selected_pokemon):
    if selected_pokemon.is_knocked_out == True:
      return "You cannot switch to a KO'ed pokemon."
    else:
      if selected_pokemon in pokemon:
        self.current_active_pokemon = selected_pokemon
        return "{} chose you, {}".format(self.name, selected_pokemon.name) 


pokemon = [charmander, squirtle, bulbasaur]
ash = Trainer("Ash Ketchum", pokemon)

gary = Trainer("Gary Oak", [squirtle, bulbasaur])

print(gary.attack(ash))


  