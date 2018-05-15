# Simple-Algorithms

Showcase of my implementation of some algorithms covered in RPI CS courses

## Edit Distance

(part of this section is referenced from [this book](http://cseweb.ucsd.edu/~dasgupta/book/index.html))

>A natural measure of the distance between two strings is the extent to which they can be aligned, or matched up.

For example, string `"SNOWY"` and `"SUNNY"` has these two alignments (there are more than these):

```
    S N O W Y
    S U N N Y
    cost: 4

    S - N O W Y
    S U N N - Y
    cost: 3
```
>The “−” indicates a “gap”; any number of these can be placed in either string.
>Edit distance is so named because it can also be thought of as the minimum number of edits—**insertions**, **deletions**, and **substitutions** of characters—needed to transform the first string into the second. 

The book's figure 6.4 has a detailed illustration of this algorithm.

## Turing Machine

Credit: [Prof. Malik's lecture slide](http://www.cs.rpi.edu/~magdon/courses/FOCS-Slides/SlidesLect25.pdf)

A turing machine(TM) is a "machine" consisting of a finite number of states, a pointer capable of moving left/right on a infinite-long paper tape and reading/writing characters. It is capable of solving decision problems.(turing-decidable languages).

The implementation here is **not** a universal turing machine, which means one instance can solve one specific problem. However, with a proper algorithm fed into the machine, it can still be universal, and simulate other turing machines(be programmable)
