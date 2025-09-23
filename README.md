# Tromino
This repo is the solution for the [Golomb's Teorem](https://en.wikipedia.org/wiki/Tromino). 

For the explanation of the code on spanish, I'm currently making a paper with the full
explanation of why and how this code works including it complexity time.

## Implementation
The function receives the tuple `(n,pos)` where `n` is the size of the 
board ($2^n\times 2^n$) and pos is another tuple `(x,y)` of the position of 
the empty space we want.

First, the code will check if the board if $2\times 2$ or $1\times 1$ and if 
is, I'll just return the basic (and easy) cases. If not, the program divide 
the board in 4 diferent boards (each of $2^{n-1}\times 2^{n-1}$) and check 
where the empty space we've given is.

### Recursiveness
When it gets the board, it will make 4 diferent boards, using recursion 
will fill the board where the empty space is, and make the next (clockwise) 
with a space on the corner, then, the code make 2 copies for the boards 
with a space on the corners and rotate each matrix using an affine 
transformation and then, it moves the full board to the side is supposed to be.

After that, the code gives 4 boards with 4 holes in it, but 3 of those 4 
holes are aligned to form another trinomio, so it put it, after that it 
join all the boards and returns the list of Trinomios for fulling that board.

## IMPORTANT
I'm aware is not the most readable code, and I have plans to refactor some parts
to make it easier to read.
