# Challenge #224 [Intermediate] - Detecting Four Sided Figures

It's a basic scanning challenge: can your program detect and count intersecting bounding boxes from an ASCII art input? A four-sided figure is an ASCII art rectangle. Note that it can overlap another one, as long as the four corners are fully connected.

## Formal Inputs & Outputs

Your program will be given an ASCII art chart showing boxes and lines. `-` and `|` characters indicate horizontal and vertical lines, respectively, while `+` characters show intersections.

Your program should emit an integer, N, of how many unique four sided figures it found. Rectangles and squares both count.

## Example Input
```
Example
                                +----+
                                |    |
+-------------------------+-----+----+
|                         |     |    |
|     +-------------------+-----+    |
|     |                   |     |    |
|     |                   |     |    |
+-----+-------------------+-----+    |
      |                   |     |    |
      |                   |     |    |
      +-------------------+-----+    |
                          |     |    |
                          |     |    |
                          |     |    |
                          +-----+----+
                                |    |
                                |    |
                                |    |
                                +----+
                                ```
## Example Output

For the above diagram your program should find 25 four sided figures.

## Challenge Input

This one adds a bit to the complexity by throwing in some three sided figures. This should catch more naive implementations.
```
Example
              +-----------+
              |           |
              |           |
              |           |
              |           |
+-------------+-----------+-------------+
|             |           |             |
|             |           |             |
|             |           |             |
|             |           |             |
+-------------+-----------+-------------+
              |           |
              |           |
              |           |
              |           |
+-------------+-----------+-------------+
|             |           |             |
|             |           |             |
|             |           |             |
|             |           |             |
+-------------+-----------+-------------+
              |           |
              |           |
              |           |
              |           |
              +-----------+
              ```
## Challenge Output

For the challenge diagram your program should find 25 four sided figures.