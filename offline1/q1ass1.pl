parent('Hasib','Rakib').
parent('Rakib','Sohel').
parent('Rakib','Rebeka').
parent('Rashid','Hasib').

child('Rakib','Hasib').
child('Sohel','Rakib').
child('Rebeka','Rakib').
child('Hasib','Rashid').

male('Hasib').
female('Rebeka').

grandchild(X,Z):-
    child(X,Y),child(Y,Z).

sibling(X,Z):-
     child(X,Y),parent(Y,Z).
