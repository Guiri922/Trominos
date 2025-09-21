# Tromino
This repo is the solution for the [Golomb's Teorem](https://en.wikipedia.org/wiki/Tromino). 

For the explanation of the code on spanish, I made a PDF that explains the 
process, you can read it [here](https://google.com)

## Implementation
The function receives the tuple `(n,pos)` where `n` is the size of the 
board ($2^n\times 2^n$) and pos is another tuple `(x,y)` of the position of 
the empty space we want.

First, the code will check if the board if $2\times 2$ and if is, I'll just 
return the 3 positions where there is not an empty space.
