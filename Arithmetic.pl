sum(X, Y, Z) :- Z is X + Y.
subtract(X, Y, Z) :- Z is X - Y.
multiply(X, Y, Z) :- Z is X * Y.
divide(X, Y, Z) :- Y =\= 0, Z is X / Y.


?- sum(10, 5, R).
?- multiply(4, 3, R).
?- divide(20, 4, R).
