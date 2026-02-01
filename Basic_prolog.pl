% Gender facts
male(mamun).
male(nazmul).

female(shama).
female(sokina).

% parents(Child, Father, Mother)
parents(mamun, nazmul, sokina).
parents(shama, nazmul, sokina).

% Sister relationship
sisterof(X, Y) :-
    female(X),
    parents(X, F, M),
    parents(Y, F, M),
    X \= Y.



?- sisterof(shama, mamun).
?- sisterof(X, mamun).
