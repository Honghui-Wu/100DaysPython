# Blind Auction Project

The goal is to build a blind auction program using a dictionary.  

***Demo***  
https://appbrewery.github.io/python-day9-demo/

***Clearing the Output***
There are several ways of clearing the output. The easiest is to simply print "\n" many times so that the output scrolls down many lines.

e.g.  
print("\n" * 20)

***Functionality***
1. Each person writes their name and bid.
2. The program asks if there are others who need to bid. If so, then the computer clears the output (prints several blank lines) then loops back to asking name and bid.
3. Each person's name and bid are saved to a dictionary.
4. Once all participants have placed their bid, the program works out who has the highest bid and prints it.