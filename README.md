# Minimum Spanning Tree (MST)

A program created using Python which includes Prims & Kruskal algorithms to find the smallest possible sum of weights for the edges of a spanning tree.

To learn more about MST [click here.](https://en.wikipedia.org/wiki/Minimum_spanning_tree)

## Installation
Make sure that you have numpy & networkx & matplotlib installed, if not, use the package manager [pip](https://pip.pypa.io/en/stable/) to install.

```bash
pip install numpy networkx matplotlib
```

## Usage
To run the program, run main.py
```bash
python main.py
```
you will be prompted to choose one of the test graphs, a starting vertex, and whether you want the result graph to be drawn.

## Examples
The first two columns in each graph represents the vertices and the third column represents the weight between the two vertices.
### Graph 1
``` bash 
0 1 2
0 2 3
1 3 2
1 4 4
2 3 1
2 5 1
3 5 1
3 6 3
4 6 2
5 6 1
```
![image of graph 1](https://i.imgur.com/jWq0Pjn.png)

### Graph 2
``` bash
0 1 2
0 2 4
1 3 6
1 4 2
2 3 4
2 5 1
3 5 9
3 6 6
4 6 4
5 6 7
6 3 3
```
![image of graph 2](https://i.imgur.com/EPldikF.png)

### Graph 3
``` bash
0 1 4
0 2 8
0 4 7
0 13 2
1 3 3
1 5 5
2 8 2
2 9 4
2 7 3
3 5 8
3 4 2
3 11 13
3 14 16
4 5 3
4 6 1
4 10 11
6 8 4
6 7 1
6 16 2
7 8 6
7 10 10
9 10 7
9 11 6
9 12 7
10 16 10
10 12 7
11 12 4
11 13 1
12 17 6
12 15 4
14 15 1
14 17 1
15 17 1
```
![image of graph 3](https://i.imgur.com/s7lW6pk.png)

## License
[MIT](https://choosealicense.com/licenses/mit/)
