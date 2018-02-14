"""
[2017-06-09] Challenge #318 [Hard] Ladder Logic

https://www.reddit.com/r/dailyprogrammer/comments/6g8ey0/20170609_challenge_318_hard_ladder_logic/

#Description
Most industrial equipment is ran on Programmable Logic Controllers (PLCs).  To this day, the most common programming
language for these systems (in the US) is a graphical language called "Ladder Logic".  
Based on traditional circuit relay systems, it is called Ladder Logic because the code resembles a ladder, with
statements organized into "rungs" with "power" flowing from left to right through the logic.  Any statement that
evaluates to true allows power to pass, and more statements to be evaluated in an "AND" configuration.  If power is
blocked, power flows top-bottom, in an "OR" configuration (if so programmed). This is described below with diagrams.
This language excels at displaying boolean logic in a way that is incredibly intuitive for electricians and industrial
maintenance personnel to read and troubleshoot without advanced programming knowledge or skills.  Statements that
evaluate to true are highlighted, so any logic with a highlighted path from left to right is true.
As the programs are controlling real world equipment, there is a series of hardwired inputs and outputs.  These are
labeled sequentially with a prefix that corresponds to the (I)nput or (O)utput.  For example I0 may be hooked up to a
switch and O4 may be hooked up to a horn.  Additionally, internal system memory can be accessed with different prefixes
for different data types (B for bools, N for integers, T for timers, etc.)
The rungs are always flanked by vertical rails - the left representing the "power" supply and the right representing
the "power" return or ground.  A EOR signifies the end of one rung and SOR the start of the next.  The rails must
travel the entire length of the program.
There are a number of instructions used but we will focus on the most common:
    Representation	Instruction Mnemonic	Description
    
    |-              SOR                     Start Of Rung
    
    -| |-         	XIC                 	True if 1 (eXamine If Closed)
    
    -|/|-          	XIO                  	True if 0 (eXamine If Open)
    
    -+-?-+-        	BST                 	Or Start (Branch STart)
     |   | 	     	NXB                 	Or Entry (NeXt Branch)
     +-?-+       	BND                  	Or End   (Branch eND)
    
    -( )-       	OTE                 	Set to result of logic (OuTput Energize)
    
    -(L)-       	OTL                  	Set to True if logic is true (OuTput Latch)
    
    -(U)-          	OTU                 	Set to False if logic is true (OuTput Unlatch)
    
    -|              EOR                     End Of Rung
Your task is to convert a series of mnemonics and data points (inputs, outputs, memory locations) into the graphical
representation.  Each rung should be numbered.  The number of dashes between items does not matter but it should be
readable and reasonably aligned.  It is common for all input logic to be aligned to the left and for all output logic
to be aligned to the right side of the screen, but this is not requied.  I have provided some pseudo code with each
example that more or less matches what is going on in the ladder logic for reference.  Instead of a text
representation, feel free to do a graphical representation instead.
#Formal Inputs & Outputs
##Example 1 - Motor Starter (Traditional Ladder Style)
I1 = stop button, I2 = Start Button, O1 = Motor.
Start the motor when the start button is pressed.
If the stop button is pressed, the motor needs to stop.
###Traditional Programming Equivalent:
    If I1 AND (I2 OR O1){
    	O1 = 1
    }Else{
    	O1 = 0
    }
###Input:
    SOR XIC I1 BST XIC I2 NXB XIC O1 BND OTE O1 EOR
Output:
       |   I1      I2      O1  |
    01 |--| |--+--| |--+--( )--|
       |       |   O1  |       |
       |       +--| |--+       |
    
    
##Example 2 - Motor Starter (Non-Traditional Ladder Style)
I1 = stop button, I2 = Start Button, O1 = Motor.
Start the motor when the start button is pressed.
If the stop button is pressed, the motor needs to stop.
Note that this is generally considered a bad practice in ladder logic - Typically you want to only ever change the
state of an output in one instruction to avoid race conditions.  This is a simple example so a race is unlikely, but
for more complicated systems it is a definite possibility.
###Traditional Programming Equivalent:
    If I1 AND I2{
    	O1 = 1
    }
    If NOT I2{
    	O1 = 0
    }
    
###Input:
    SOR XIC I1 XIO I2 OTL O1 EOR SOR XIC I2 OTU 01 EOR
###Output:
    
       |   I1   I2                   O1  |
    01 |--| |--|/|------------------(L)--|
       |                                 |
       |   I2                        O1  |
    02 |--| |-----------------------(U)--|
    
    
##Example 3 - Motor Starter With Light
I1 = Stop button, I2 = Start Button, O1 = Motor, O2 = Light
Start the motor when the start button is pressed.
If the stop button is pressed, the motor needs to stop.
A light should indicate that the motor is not running.
Traditional Programming Equivalent:
    If I1 AND (I2 OR O1){
    	O1 = 1
    }Else{
    	O1 = 0
    }
    If NOT O1{
    	O2 = 1
    }Else{
    	O2 = 0
    }
    
###Input:
    SOR XIC I1 BST XIC I2 NXB XIC O1 BND OTE O1 EOR SOR XIO O1 OTE O2 EOR
###Output:
       |   I1      I2      O1  |
    01 |--| |--+--| |--+--( )--|
       |       |   O1  |       |
       |       +--| |--+       |
       |  O1               O2  |
    02 |-|/|--------------( )--|
    
    
##Example 4 Motor Starter With Local/Remote Select
I1 = Stop, I2 = Local Start, I3 & I4 = Remote Start buttons, I5 = Local/Remote Toggle Switch, O1 = Motor
If the system is in local mode, start the motor when the local start button is pressed.
If not in local, start the motor when either remote start is pressed.
If the stop button is pressed, the motor needs to stop.
###Traditional Programming Equivalent:
    If I1 AND ((I2 AND I5) OR ((I3 OR I4) AND NOT I5) OR O1){
    	O1 = 1
    }Else{
    	O1 = 0
    }
    
###Input:
    SOR XIC I1 BST XIC I2 XIC I5 NXB BST XIC I3 NXB XIC I4 BND XIO I5 NXB XIC O1 BND OTE O1 EOR
###Output:
       |   I1      I2        I5      O1  |
    01 |--| |--+--| |-------| |--+--( )--|
       |       |     I3      I5  |       |
       |       +--+-| |--+--|/|--+       |
       |       |  |  I4  |       |       |
       |       |  +-| |--+       |       |
       |       |   O1            |       |
       |       +--| |------------+       |
    
#Notes/Hints
Here are some resources on the language itself:
https://en.wikipedia.org/wiki/Ladder_logic
http://library.automationdirect.com/understanding-ladder-logic/
The actual mnemonics and representations used for each instruction varies by PLC brand / manufacturer, but the core
functionality is the same.  For example, in popular German PLCs, xic becomes A (for and), xio becomes AN (for and not),
branch becomes A(O ? O ?...) (for and (or or or)).  The Germans don't typically use the ladder representation at all
though - it's all done directly with the mnemonics.
Modern PLCs support many more languages than ladder (https://en.wikipedia.org/wiki/IEC_61131-3) and many now have some
basic memory management allowing memory and IO addresses to be referenced by name rather than address.
# Credit
This challenge was suggested by user /u/unitconversion, many thanks. If you have a challenge idea, please share it on
/r/dailyprogrammer_ideas and there's a good chance we'll use it. 
"""


def main():
    pass


if __name__ == "__main__":
    main()
