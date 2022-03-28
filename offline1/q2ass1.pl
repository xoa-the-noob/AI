parent('Hasib','Rakib').
parent('Rakib','Sohel').
parent('Rakib','Rebeka').
parent('Rashid','Hasib').
parent('Sohel','Anne').
parent('Rebeka','Sam').

male('Hasib').
male('Rakib').
male('Sohel').
male('Rashid').

female('Rebeka').

sister(X,Y):-
     parent(Z,X),parent(Z,Y),female(X),X\=Y.

brother(X,Y):-
     parent(Z,X),parent(Z,Y),male(X),X\=Y.

uncle(X,Z):-
    parent(Y,Z),brother(X,Y).

aunt(X,Z):-
    parent(Y,Z),sister(X,Y).






