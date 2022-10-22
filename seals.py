#factors to manipulate
#Odds of a seal getting oto from eating an infected fish
oddsoverallofsealsgettingoto = 0.25
#odds of an older seal getting oto if they eat an infected fish
oddsofoldsealgettingoto = 0
#odds of a younger seal getting oto from eating an infected fish
oddsofyoungsealgettingoto = 0.01
#number of cycle the oto stays in the fish
length_of_oto_in_seal = 1
#the amount of immunity a seal gets after it eats a fish. goes from 0-1.
initial_immunity = 1
#The amount that the immunity decreases each cycle
immunity_decrease_amounts = 0
#the amount of immunity that gets added on after each subsequent infection
cumulative_immunity_addon_amount = 0.33

import random

oto_infection_chance = 0.25

class seals:
  def __init__(self, age, oto_infection, location):
    self.age = age
    self.oto_infection = oto_infection
    self.location = location
    self.oto_length = 0
    self.antibodies = 0

#function to model hunting. each seal hunts 10 times, and if they eat a seal, then they have a chance to be infected by oto.
def hunt(seal, fishpop):
  for x in range(0,10):
    seal.location = random.randint(0,len(fishpop)-1)
    preypop = fishpop[seal.location]
    prey = preypop[random.randint(0,len(preypop)-1)]
    calc_oto_infection_basic(prey, seal)
   # calc_oto_infection_age(prey, seal)
    fishpop[seal.location].remove(prey)

#this calculates if a seal gets covid from eating an infected fish
def calc_oto_infection_basic(prey, seal):
  if prey.oto_infection == 1 and random.random() < oddsoverallofsealsgettingoto and seal.antibodies < random.random():
    seal.oto_infection = 1
    seal.oto_length = 1

#this calculates if a seal gets covid from eating an infected fish, but factors in age.
def calc_oto_infection_age(prey,seal):              
  if seal.age <= 3 and random.random() < oddsofyoungsealgettingoto and seal.antibodies == 0:
    seal.oto_infection = 1
    seal.oto_length = 1
  elif seal.age >= 4 and random.random() < oddsofoldsealgettingoto and seal.antibodies == 0:
    seal.oto_infection = 1
    seal.oto_length = 1

#this function kills off seals that die of oto, reduces antibodies, adds immunity, and eliminates oto from infected seals that have foughtit off. 
def increase_oto_length(sealpop):
  for x in sealpop:
    if random.random() < 0.02:
      sealpop.remove(x)
    if x.oto_length > 0:
      x.oto_length += 1
      if x.oto_length > length_of_oto_in_seal and x.antibodies < 1:
        x.oto_length = 0
        x.oto_infection = 0
        #this codes for the initial immunity after infection
        #x.antibodies = initial_immunity
        x.antibodies += cumulative_immunity_addon_amount
    #this decreases antibodies
    decrease_antibody(x)

def decrease_antibody(seal):
  if seal.antibodies > 0:
    seal.antibodies -= immunity_decrease_amounts
  return seal
