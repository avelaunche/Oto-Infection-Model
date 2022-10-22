import random
fish_spawn_infection_chance = 0.1
#this is the class for the fish with infection status, and location
class fish:
  def __init__(self,oto_infection, location):
    self.oto_infection = oto_infection
    self.location = location

#this function generates the fish pop
def generate_fish(number):
  newpop = []
  #this codes out 100 fish for every single location
  for x in range(0,100):
    grid_pop = []
    for c in range(0,int(number/100)):
      oto_infection_fish = 0
      if random.random() < fish_spawn_infection_chance:
        oto_infection_fish = 1
      grid_pop.append(fish(oto_infection_fish,x))
    newpop.append(grid_pop)
  return newpop

#This function prints the number of fish in the population
def print_fishpop(fishpop):
  len_of_pop = 0
  for x in fishpop:
    len_of_pop += len(x)
  print(len_of_pop)

#this function kills off around 10% of the fish population every cycle to simulate natural deaths in a fish population
def other_causes(fishpop):
  for x in fishpop:
    for c in x:
      if random.random() < 0.1:
        x.remove(c)

#This replenishes the fish population to demonstrate the breeding that fish do. They have no oto infection because they are meant to represent new uninfected baby fish.
def regenerate_fishpop(fishpop):
  for x in fishpop:
    while len(x) < 100:
      x.append(fish(0,x))

#This prints the number of infected fish in the population
def print_infected_fish(fishpop):
  number_of_infected = 0
  for x in fishpop:
    for c in x:
      if c.oto_infection == 1:
        number_of_infected += 1
  print(number_of_infected)
  return number_of_infected
