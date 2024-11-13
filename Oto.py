import seals
import fish
import eseals
import matplotlib.pyplot as plt

seal_pop_number = 100
fish_pop_number = seal_pop_number * 100

sealpop = eseals.seals_generate(seal_pop_number)
fishpop = fish.generate_fish(fish_pop_number)

infected_seals = []
infected_fish = []
infected_pseals = []
young_seals_infection = []
old_seals_infection = []
cycle_number = []

infected_eseals = []
infected_young_eseals = []
infected_old_eseals = []
infected_proportiontimes10 = []
#this generates the population
elephant_seals_pop = eseals.seals_generate(seal_pop_number)

#this for loop runs the cycle 100 times
for x in range(0,100):
  #this for loop is meant to make every instance undergo the code they need to
  for m in elephant_seals_pop:
    #this gets the seal to eat 10 fish and catch oto if they have to
    eseals.hunt(m, fishpop)
    #this makes the seal poop and spread it to fish
    eseals.poop(m, fishpop)
    #this adds a year to every seal and kills off the older seals
    m.age += 1
    if m.age > 10:
      elephant_seals_pop.remove(m)
  #this kills off fish. 10% every year.
  fish.other_causes(fishpop)
  #this replaces any dead seals due to age or disease
  eseals.replace_seal_pop(elephant_seals_pop, seal_pop_number)
  #this replaces the dead fish
  fish.regenerate_fishpop(fishpop)
  #the following code prints various pieces of data
  infectedyoung = eseals.print_infected_young_seals(elephant_seals_pop)
  infectedold = eseals.print_infected_old_seals(elephant_seals_pop)
  antibodies = eseals.print_seal_antibodies(elephant_seals_pop)
  infected_total_eseals = eseals.print_infected_seal(elephant_seals_pop)
  fish.print_infected_fish(fishpop)
  eseals.increase_oto_length(elephant_seals_pop)
  #this appends data into a list soit can be graphed
  infected_eseals.append(infected_total_eseals)
  infected_young_eseals.append(infectedyoung)
  infected_old_eseals.append(infectedold)
  num_young = 0
  #this prints the proportion of infected young
  for x in elephant_seals_pop:
    if x.age < 4:
      num_young += 1
  print(num_young)
  infected_proportiontimes10.append(infectedyoung/num_young*100)
  print()

#this generates a fish population
fishpop = fish.generate_fish(fish_pop_number)


for x in range(0, 100):
    print(str(x + 1) + 'th year')
    for m in sealpop:
      eseals.hunt(m, fishpop)
      eseals.poop(m, fishpop)
      m.age += 1
      if m.age > 10:
        sealpop.remove(m)
    fish.other_causes(fishpop)


    print('Infected fish number')
    infected_number_fish = fish.print_infected_fish(fishpop)
    fish.regenerate_fishpop(fishpop)

    print('Infected seal number')
    infected_number_seals = eseals.print_infected_seal(sealpop)
    print('seal antibodies')
    eseals.print_seal_antibodies(sealpop)
    infected_fish.append(infected_number_fish)
    infected_seals.append(infected_number_seals)
    print('old seals infected')
    old_seals_infected_number = eseals.print_infected_old_seals(sealpop)
    print('young seals infected')
    young_seals_infected_number = eseals.print_infected_young_seals(sealpop)
    young_seals_infection.append(young_seals_infected_number)
    old_seals_infection.append(old_seals_infected_number)
    cycle_number.append(x)
    eseals.increase_oto_length(sealpop)
    eseals.replace_seal_pop(sealpop, seal_pop_number)

    print()


#combined model
  
for x in range(0,100):
  #this for loop is meant to make every instance undergo the code they need to
  for m in range(len(elephant_seals_pop)):
    #this gets the seal to eat 10 fish and catch oto if they have to
    eseals.hunt(elephant_seals_pop[m], fishpop)
    eseals.hunt(sealpop[m], fishpop)
    #this makes the seal poop and spread it to fish
    eseals.poop(elephant_seals_pop[m], fishpop)
    eseals.poop(sealpop[m], fishpop)
    #this adds a year to every seal and kills off the older seals
    elephant_seals_pop[m].age += 1
    sealpop[m].age += 1
  hi = []
  
  for x in elephant_seals_pop:
    if x.age < 10:
      hi.append(x)
  elephant_seals_pop = hi
  hi = []
  for x in sealpop:
    if x.age < 10:
      hi.append(x)
  sealpop = hi
  #this kills off fish. 10% every year.
  fish.other_causes(fishpop)
  #this replaces any dead seals due to age or disease
  eseals.replace_seal_pop(elephant_seals_pop, seal_pop_number)
  eseals.replace_seal_pop(sealpop, seal_pop_number)
  #this replaces the dead fish
  fish.regenerate_fishpop(fishpop)
  #this prints the proportion of infected young
  for x in elephant_seals_pop:
    if x.age < 4:
      num_young += 1
  infected_proportiontimes10.append(infectedyoung/num_young*100)






plt.plot(cycle_number, old_seals_infection, label = 'old seals')
plt.plot(cycle_number, young_seals_infection, label = 'young seals')
plt.plot(cycle_number, infected_seals, label = 'seals in general')
plt.plot(cycle_number, infected_eseals, label = 'eseals')
plt.plot(cycle_number, infected_young_eseals, label = 'infected young')
plt.plot(cycle_number, infected_old_eseals, label = 'infected old')
#plt.plot(cycle_number, infected_proportiontimes10, label = 'proportion')

#green = total northern harbour
#brown = old elephant seals infected
#orange+blue = old+young northern harbur
#red = 
#pink = proportion of infected

plt.show()

#break the time down into months (later)


