# Simple-Algorithms

Showcase of my implementation of some algorithms covered in course CSCI-2300

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