"""
[2015-02-11] Challenge #201 [Practical Exercise] Get Your Priorities Right!

https://www.reddit.com/r/dailyprogrammer/comments/2vkwgb/20150211_challenge_201_practical_exercise_get/

# [](#PEIcon) **(Practical Exercise)**: Get Your Priorities Right!
A [priority queue](http://en.wikipedia.org/wiki/Priority_queue) is a data structure similar to a standard queue, except
that entries in the queue have a *priority* associated with them - such that, when removing items from the queue, the
entry with the highest priority will be removed before ones with lower priority. This is similar to a hospital triage
system: patients with more severe wounds get treated quicker, even if they arrived later than a patient with a smaller
injury. Let's say I have a priority queue containing strings, where the priority value is a real number. I add these 3
objects to my priority queue, in no particular order:
| Patient | Priority |
|--------:|:---------|
| `"David Whatsit"` | 3.06 |
| `"Joan Smith"` | 4.33 |
| `"Bob Testing"` | 0.39 |
| `"Samuel Sample"` | 1.63 |
Here, if I was to *dequeue* four strings from the priority queue, the strings `"Joan Smith"`, `"David Whatsit"`,
`"Samuel Sample"` and `"Bob Testing"` would come out, in that order.
But what if we could assign *two* priorities to each object? Imagine a hospital (to keep with the theme), that needs to
keep a list of equipment supplies and their costs. It also needs to keep track of how long it will take to receive that
item.
| Item | Cost | Shipping Time |
|--------:|:--------|:--------|
| Hyperion Hypodermic Needle | £1.99 | 3 days |
| SuperSaver Syringe | £0.89 | 7 days |
| InjectXpress Platinum Plated Needle | £2.49 | 2 days |
Here, when the hospital is at normal running conditions with good supply stock, it would want to buy the cheapest
product possible - shipping time is of little concern. Thus, dequeueing by the *Lowest Cost* priority would give us the
SuperSaver syringe. However, in a crisis (where supply may be strained) we want supplies as fast as possible, and thus
dequeueing an item with the *Lowest Shipping Time* priority would give us the InjectXpress needle. This example isn't
the best, but it gives an example of a priority queue that utilizes *two priority values* for each entry.
Your task today for the (non-extension) challenge will be to implement a two-priority priority queue for strings, where
the priority is represented by a real number (eg. a floating-point value). The priority queue must be able to hold an
unbounded number of strings (ie. no software limit). **If your language of choice already supports priority queues with
1 priority, it might not be applicable to this challenge - read the specification carefully**.
# Specification
## Core
Your priority queue must implement *at least* these methods:
* `Enqueue`. This method accepts three parameters - a **string**, **priority value A**, and **priority value B**, where
the priority values are *real numbers* (see above). The **string** is inserted into the priority queue with the given
priority values **A** and **B** (how you store the queue in memory is up to you!)
* `DequeueA`. This method removes and returns the **string** from the priority queue with the highest **priority A**
value. If two entries have the same A priority, return whichever was enqueued first.
* `DequeueB`. This method removes and returns the **string** from the priority queue with the highest **priority B**
value. If two entries have the same B priority, return whichever was enqueued first.
* `Count`. This method returns the number of strings in the queue.
* `Clear`. This removes *all* entries from the priority queue.
## Additional
If you can, implement this method, too:
* `DequeueFirst`. This removes and returns the **string** from the priority queue that was **enqueued first**, ignoring
priority.
Depending on how you implemented your priority queue, this may not be feasible, so don't get too hung up on this one.
## Extension
Rather than making your priority queue only accept strings, make a **generic** priority queue, instead. A generic
object is compatible with many types. In C++, this will involve the use of
[templates](//en.wikipedia.org/wiki/Template_\(C%2B%2B\)). More reading resources
[here](//en.wikipedia.org/wiki/Generic_programming). For example, in C#, your class name might look like
`DualPriorityQueue<TEntry>`. Some dynamic languages such as Ruby or Python do not have static typing, so this will not
be necessary.
# Notes
## Making Use of your Language
The main challenge of this exercise is knowing your language and its features, and adapting your solution to them. For
example, in .NET-based languages, `Count` would be a property rather than a method, as that is more idiomatic in those
languages. Similarly, in some languages such as Ruby, F# or other functional language, overloading operators may be
more idiomatic than the usage of verbose `Enqueue` and `Dequeue` functions. How you do the specifics is up to you.
You should also be writing clean, legible code. Follow the style guide for your language, and use the correct
naming/capitalisation conventions, which differ from language to language. Consider writing [unit
tests](http://en.wikipedia.org/wiki/Unit_testing) for your code, as an exercise in good practice!
## Tips and Reading Material
If you are planning on using something like a heap for the priority queue, consider interleaving each item into two
heaps to store both priorities. How you will handle the dequeueing is part of the fun! If the concept of a priority
queue is new to you, here is some reading material.
* [University of Wisconsin-Madison: priority queue](http://pages.cs.wisc.edu/~vernon/cs367/notes/11.PRIORITY-Q.html)
* [Queues and Priority Queues](http://www.oopweb.com/Java/Documents/ThinkCSJav/Volume/chap16.htm)
Here's some more stuff on unit testing.
* [Unit testing on WikiBooks](http://en.wikibooks.org/wiki/Introduction_to_Software_Engineering/Testing/Unit_Tests)
* [MSDN: .NET unit tests](https://msdn.microsoft.com/en-us/library/hh694602.aspx)
* [Writing good unit tests](https://developer.salesforce.com/page/How_to_Write_Good_Unit_Tests)
# Finally...
I wonder what this data structure would be called? A double priority queue?
Got a good idea for a challenge? Head on over to /r/DailyProgrammer_Ideas and tell us!
"""


def main():
    pass


if __name__ == "__main__":
    main()
