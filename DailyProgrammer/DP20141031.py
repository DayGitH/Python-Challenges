"""
[10/31/2014] Challenge #186 [Special] Code or Treat - Halloween 2014

https://www.reddit.com/r/dailyprogrammer/comments/2kwfqr/10312014_challenge_186_special_code_or_treat/

#Description:
Happy Halloween. For Today's challenge we will go off our typical path and do a special challenge posting. I have come
up with 2 challenges. One will be [Easy] the other [Intermediate]. They do have a Halloween theme and it is intended to
be a bit light hearted in our typical approach to challenges. Have fun :)
#[Easy] Bag Inventory:
##Description:
So to help out all the trick or treaters we need to develop a tool to help inventory their candy haul for the night.
You will be given a text file that contains a listing of every piece of candy in the bag. Your challenge is to develop
a solution to inventory the candy and print out a summary of how much candy you got.
You must answer these basic questions
* How many pieces of candy did you get
* How much of each type
* What percentage of total candy does that type occupy
##Input:
Use this gist listing as your text file to represent your bag of candy.
[Candy Bag Link] (https://gist.github.com/coderd00d/54215798871d0c356cfb)
##Output: 
You must answer the basic questions. How you display it and present it we leave to the programmer to decide. Some
suggestions could be a text output. Perhaps you do a histogram or pie chart. Maybe show a real time tally as you go
through the bag counting the candy and display it as a gif for all to enjoy.
#[Intermediate] - The Coding Dead
##Description:
Zombie lore has been very popular in the recent years. We are entertained by the stories of the dead coming back to
life as a zombie and the struggle of human to survive the zombie horde. In Zombie lore it is common that if you are
bitten by a zombie you become a zombie. This behavior works much like a plague. The zombie grow in numbers and the
living must deal with them by usually do a fatal wound to the zombie's brain/spinal cord. 
We will explore this plague of zombies by creating  zombie simulator. This simulator will randomly populate a map and
have 3 types of entities: Zombies, Victims and hunters.
* Zombies -- The walking dead back to life. They will roam looking to bite victims to turn them into zombies.
* Victims -- Innocent humans who are not trained in Zombie lore and have no skills or knowledge to fight back.
* Hunters -- Trained humans in Zombie lore who seek out to destroy Zombies to save the planet.
##Simulation Map
Our simulation will run on a 20x20 Map. Each spot can occupy Either a Zombie, Victim, Hunter or be an empty space. You
need to develop a way to support this map and to be able to create the map by randomly placing a set amount of starting
Zombies, Victims or Hunters. Only 1 entity per a space.
##Input
You will feed your simulation 4 numbers. x y z t
* x - how many zombies to randomly spawn
* y - how many victims to randomly spawn
* z - how many hunters to randomly spawn.
* t - how many "ticks" of time to run the simulation
##Map Error Checking:
So on a 20x20 map you have 400 spots. If x+y+z > 400 you will return an error. You cannot create a map that holds more
than it can hold.
##Simulation
Our simulation will have a "tick". This is a unknown unit of time. But in this time actions occur as follows to define
our simulation.
* Movement
* Zombie slaying
* Bite
##Movement
Movement occurs for all our life forms. If the life forms try to move and the space is occupied they will just continue
to occupy their current location.
* Zombies -- will try to move 1 space. They will either move up, down, left or right. Zombies are not able to move
diagonal. They just cannot handle such a movement.
* Victims -- typically do not move. However, if they are next to a zombie (up, down, left, right or diagonal) they will
try to move 1 square. Note they might end up in a square next to the zombie again or a new zombie. The panic of
movement and being a "victim" does not mean they make the optimal move.
* Hunters - Will move to 1 new spot in any direction (up, down, left, right, diagonal) to seek and find a zombie to
destroy.
## Zombie Slaying
Once movement occurs if a hunter is next to in any direction (up, down, left, right, diagonal) to a zombie he will slay
a zombie. If the hunter is next to two zombies he will slay two zombies. However if the hunter is next to three or more
zombies he will only be able to slay two of them. Just not enough time to kill more than two. When you slay a zombie
you remove it off our map.
## Bite
Zombies will bite a non-zombie if they are (up, down, left, right) of a non-zombie. They will not be able to bite at a
diagonal to represent the simple mind of the zombie. Victims or Hunters can be bitten. Once bitten the Victim or Hunter
becomes a zombie. You will change them into a Zombie. 
## Data
We want to gather data during the simulation. Each time an entity changes spots in movement we record this distance by
entity.
* Zombie Stumble Units - number of spots zombies moved too
* Victim Flee Units - number of spots victims moved too
* Hunter Seek Units - number of spots hunters moved too.
We will maintain a population number. We will know our original population because we are given those numbers.
As time goes on we want to record the final population of all 3 entities. Also we want to record some basic events.
* Number of "Single" kills by hunter (killing only 1 zombie a turn)
* Number of "Double" kills by a hunter (killing 2 zombies a turn)
* Total zombies killed by Hunters
* Number of Victims bitten
* Number of Hunters bitten
* Total number of non-zombies bitten
## Output
The programmer should output at the end of the simulation a report of what happened.
* Output the x y z t values. So your starting populations and how many ticks the simulator ran
* Output all the Data above in the data
* You will show the final population counts of your entities. 
## Final
With all this data we can compute a decay rate. Either the zombie population is decaying or the non-zombie population
is decaying. If the decay difference is within 5 then the population is a balance. So for example if 100 zombies are
killed but 95 are created it is a balance. (The difference between killed zombies and bites was 5 or less) However if
the decay difference is more than 5 in favor of bites the Zombies Win. If the decay difference is more than 5 in favor
of the Hunters then the Humans win. 
You will decide who wins the simulation. Humans, Zombies or a tie.
## Now have fun
Using different x y z and t values try to see if you can get a balance For a total population (x + y + z) for the
following numbers of (x + y + z)
* 100
* 200
* 300
# Message From the Mods
From the Moderator Staff of /r/dailyprogrammer enjoy your 2014 Halloween :) Thank you for your participation in our
subreddit.
"""


def main():
    pass


if __name__ == "__main__":
    main()
