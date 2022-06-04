from pyDatalog import pyDatalog
pyDatalog.create_terms('N,X0,X1,X2,X3,X4,X5,X6,X7')
pyDatalog.create_terms('ok,queens,next_queen')
# the queen in the first column can be in any row
queens(X0)                      <= (X0._in(range(8)))
# to find the queens in the first 2 columns, find the first one first, then find a second one
queens(X0,X1)                   <= queens(X0)                   & next_queen(X0,X1)
# repeat for the following queens
queens(X0,X1,X2)                <= queens(X0,X1)                & next_queen(X0,X1,X2)
queens(X0,X1,X2,X3)             <= queens(X0,X1,X2)             & next_queen(X0,X1,X2,X3)
queens(X0,X1,X2,X3,X4)          <= queens(X0,X1,X2,X3)          & next_queen(X0,X1,X2,X3,X4)
queens(X0,X1,X2,X3,X4,X5)       <= queens(X0,X1,X2,X3,X4)       & next_queen(X0,X1,X2,X3,X4,X5)
queens(X0,X1,X2,X3,X4,X5,X6)    <= queens(X0,X1,X2,X3,X4,X5)    & next_queen(X0,X1,X2,X3,X4,X5,X6)
queens(X0,X1,X2,X3,X4,X5,X6,X7) <= queens(X0,X1,X2,X3,X4,X5,X6) & next_queen(X0,X1,X2,X3,X4,X5,X6,X7)
# the second queen can be in any row, provided it is compatible with the first one
next_queen(X0,X1)                   <= queens(X1)                       & ok(X0,1,X1)
# to find the third queen, first find a queen compatible with the second one, then with the first# re-use the previous clause for maximum speed, thanks to memoization
next_queen(X0,X1,X2)                <= next_queen(X1,X2)                & ok(X0,2,X2)
# repeat for all queens
next_queen(X0,X1,X2,X3)             <= next_queen(X1,X2,X3)             & ok(X0,3,X3)
next_queen(X0,X1,X2,X3,X4)          <= next_queen(X1,X2,X3,X4)          & ok(X0,4,X4)
next_queen(X0,X1,X2,X3,X4,X5)       <= next_queen(X1,X2,X3,X4,X5)       & ok(X0,5,X5)
next_queen(X0,X1,X2,X3,X4,X5,X6)    <= next_queen(X1,X2,X3,X4,X5,X6)    & ok(X0,6,X6)
next_queen(X0,X1,X2,X3,X4,X5,X6,X7) <= next_queen(X1,X2,X3,X4,X5,X6,X7) & ok(X0,7,X7)
# it's ok to have one queen in row X1 and another in row X2 if they are separated by N columns
ok(X1, N, X2) <= (X1 != X2) & (X1 != X2+N) & (X1 != X2-N)
# give me one solution to the 8-queen puzzle
print(queens(X0,X1,X2,X3,X4,X5,X6,X7).data[0])
(4, 2, 0, 6, 1, 7, 5, 3)
