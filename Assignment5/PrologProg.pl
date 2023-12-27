%Code to reverse a list
reverse_list([], []).
reverse_list([H|T], ReversedList):-
    reverse_list(T, ReversedTail),
    append(ReversedTail, [H], ReversedList).
%Base case
write_list([]):-
    nl.
%Print the list to the console
write_list([H|T]):-
    write(H),
    write(' '),
    write_list(T).
%Wrapper Predicate to read reverse and then write
main:-
    read(Input),
    reverse_list(Input, Result),
    write_list(Result).
