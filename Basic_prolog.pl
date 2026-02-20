
male(mamun).
male(nazmul).

female(shama).
female(sokina).

% parents(Child, Father, Mother)
parents(mamun, nazmul, sokina).
parents(shama, nazmul, sokina).

sisterof(X, Y) :-
    female(X),
    parents(X, F, M),
    parents(Y, F, M),
    X \= Y.


Queries:
?- sisterof(shama, mamun).
?- sisterof(X, mamun).
