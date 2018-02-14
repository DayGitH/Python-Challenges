"""
[Weekly #25] Escape the trolls

https://www.reddit.com/r/dailyprogrammer/comments/4vrb8n/weekly_25_escape_the_trolls/

#Description
We are going to create a mini game. 
I'm going post updates with ideas, if you guys have them.
The goal of the game is to escape a maze and not get eaten by the trolls.
#Phases of the game
##Phase 1
Create your character and make it moveable.
You can use this amazing maze (see what I did there?) or create one yourself.
If you are going to use ASCII for the game, I suggest you use `<>v^` for your character since direction becomes
important.
    #########################################################################
    #   #               #               #           #                   #   #
    #   #   #########   #   #####   #########   #####   #####   #####   #   #
    #               #       #   #           #           #   #   #       #   #
    #########   #   #########   #########   #####   #   #   #   #########   #
    #       #   #               #           #   #   #   #   #           #   #
    #   #   #############   #   #   #########   #####   #   #########   #   #
    #   #               #   #   #       #           #           #       #   #
    #   #############   #####   #####   #   #####   #########   #   #####   #
    #           #       #   #       #   #       #           #   #           #
    #   #####   #####   #   #####   #   #########   #   #   #   #############
    #       #       #   #   #       #       #       #   #   #       #       #
    #############   #   #   #   #########   #   #####   #   #####   #####   #
    #           #   #           #       #   #       #   #       #           #
    #   #####   #   #########   #####   #   #####   #####   #############   #
    #   #       #           #           #       #   #   #               #   #
    #   #   #########   #   #####   #########   #   #   #############   #   #
    #   #           #   #   #   #   #           #               #   #       #
    #   #########   #   #   #   #####   #########   #########   #   #########
    #   #       #   #   #           #           #   #       #               #
    #   #   #####   #####   #####   #########   #####   #   #########   #   #
    #   #                   #           #               #               #   #
    # X #####################################################################
Small corridor version, thanks to /u/rakkar16
    #####################################
    # #       #       #     #         # #
    # # ##### # ### ##### ### ### ### # #
    #       #   # #     #     # # #   # #
    ##### # ##### ##### ### # # # ##### #
    #   # #       #     # # # # #     # #
    # # ####### # # ##### ### # ##### # #
    # #       # # #   #     #     #   # #
    # ####### ### ### # ### ##### # ### #
    #     #   # #   # #   #     # #     #
    # ### ### # ### # ##### # # # #######
    #   #   # # #   #   #   # # #   #   #
    ####### # # # ##### # ### # ### ### #
    #     # #     #   # #   # #   #     #
    # ### # ##### ### # ### ### ####### #
    # #   #     #     #   # # #       # #
    # # ##### # ### ##### # # ####### # #
    # #     # # # # #     #       # #   #
    # ##### # # # ### ##### ##### # #####
    # #   # # #     #     # #   #       #
    # # ### ### ### ##### ### # ##### # #
    # #         #     #       #       # #
    #X###################################
Place the character in a random spot and navigate it to the exit. `X` marks the exit.
##Phase 2
We have a more powerfull character now. He can push blocks that are in front of him.
He can only push blocks into an empty space, not into another block.
e.g.
    Can push
    #   #     
    # > #   ##
    #   #        
    Can't push
    
    #   #     
    # > #####
    #   #   
##Phase 3
Let's add some trolls. Place trolls at random spots and let them navigate to you character.
You can avoid the trolls by pushing blocks. 
The trolls should move a block when you move a block, so it is turnbased.
##Phase 4
Generate your own maze.
#Notes/Hints
Each movement is 1 turn. So turning your character spends 1 turn
I propose to use ASCII for the game. 
But if you want to use a framework with images, go ahead. If you do it in 3D, that is also fine.
You can use pathfinding for the trolls, but let's be honest, they are trolls. They should not be the brightest of them
all.
Some usefull links:
- https://en.wikipedia.org/wiki/Maze_generation_algorithm
- http://weblog.jamisbuck.org/2011/2/7/maze-generation-algorithm-recap
- https://en.wikipedia.org/wiki/Pathfinding
- http://theory.stanford.edu/~amitp/GameProgramming/AStarComparison.html
#Bonus
Bonuses don't need to be done in any specific order
##Bonus 1 by /u/JaumeGreen
Make the trolls crushable. When you move a block on a troll, it is dead/crushed/pancaked.
##Bonus 2
Make it real time. You'll have to see what pacing of the trolls are doable.
##Bonus 3 by /u/Dikaiarchos
Create tunnels to traverse the maze in a more complicated way.
##Bonus 4 by /u/Dikaiarchos
Create a perfect maze algorithm (no loops to walk trough). This does makes the game a lot harder...
##Bonus 5 by /u/gandalfx
Instead of using `#` as a wall piece, you could use [UTF-8 boxes](https://en.wikipedia.org/wiki/Box-drawing_character)
##Bonus 6 by /u/chunes
Add a limited sight for the player, so the player has to navigate without seeing the complete maze
##Bonus 7 by /u/GentlemanGallimaufry
When moving blocks, you have a chance that you block yourself from the exit.
So when this happens you should give a game over message.
#Finally
Have a good challenge idea?
Consider submitting it to /r/dailyprogrammer_ideas
"""


def main():
    pass


if __name__ == "__main__":
    main()
