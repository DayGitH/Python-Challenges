"""
[2016-05-25] Challenge #268 [Intermediate] Network and Cards: Part 2, The cards

https://www.reddit.com/r/dailyprogrammer/comments/4kz0e0/20160525_challenge_268_intermediate_network_and/

#Description
This week we are creating a game playable over network. This will be a 3-parter.
The second part is less dry then the first part. We are going to play a simplyfied version of blackjack over the
network.
The server will deal cards over the network to all connected clients, there is no dealer stack like in real blackjack.
When all connected clients send a `START` command, the game will begin, you don't have to look for other connections
then.
The communication goes as followed:
    SERVER -> CLIENT A: TAKE or PASS
    CLIENT A -> SERVER: TAKE
    SERVER -> CLIENT A: HEARTS QUEEN
    
    SERVER -> CLIENT B: TAKE or PASS
    CLIENT B -> SERVER: PASS
    
The client has the option to either respond with a `TAKE` command or `PASS` command, the server then go to the next
client till everyone is done (all passed or everyone has 21 or more in score)
The cards have the following values:
    2 -> 2
    3 -> 3
    4 -> 4
    5 -> 5
    6 -> 6
    7 -> 7
    8 -> 8
    9 -> 9
    Jack -> 10
    Queen -> 10
    King -> 10
    Ace -> 1 or 11 (11 if not over 21 and 1 if over)
#Formal Inputs & Outputs
##Input description
 - Server
 
Server has to accept at least 3 commands: `START`, `TAKE` and `PASS`
 - Client
 
 Clients must be able to recieve the choice for `TAKE` and `PASS` and must be able to recieve cards, format of that is
up to you
##Output description
 - Server
 
 No Output required, but I can imagen that some loggin will be handy.
 
  - Client
  
  A decent output for humans to read the cards and see their current score.
  Also must know when to type in the option to `TAKE` and `PASS`
 
#Notes/Hints
## TCP Socket approach
The server needs to able to handle multiple clients in the end, so a multithreaded approach is advised.
It is advised to think of some command like pattern, so you can send messages to the server and back.
For the server and client, just pick some random ports that you can use.
[Here](https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers) you have a list off all "reserved" ports.
For the connection, TCP connections are the easiest way to do this in most languages. But you are not limited to that
if you want to use something more high-level if your language of choice supports that.
## REST api approach
Some off you pointed out that this could be done with a webserver. If this is more in the line of what you are used to,
no problem then, as long as it stays in the line of a multiplayer game.
#Bonus
 - Send all the events to other clients in the form `CLIENT A takes a Queen of Hearts` or `Client A passes`
 - Allow clients to join when a game is running for the next game
 - Add a spectator mode, nothing more fun then Let's play no?
#Finally
Have a good challenge idea?
Consider submitting it to /r/dailyprogrammer_ideas
"""


def main():
    pass


if __name__ == "__main__":
    main()
