/* -*- Mode:Prolog; coding:iso-8859-1; indent-tabs-mode:nil; prolog-indent-width:8; prolog-paren-indent:4; tab-width:8; -*- */


/* -*- Mode:Prolog; coding:iso-8859-1; indent-tabs-mode:nil; prolog-indent-width:8; prolog-paren-indent:4; tab-width:8; -*- 
Constraint store

Author: Tony Lindgren
Coauthor: Laura Galera (laga6199), America Castrejon (amca6849)

*/
:- use_module([library(clpfd)]).

zebra:-
        % Define variabels and their domain      
        House_colors = [Red, Green, White, Yellow, Blue],
        domain(House_colors, 1,5), % Domain integers, 1 to 5  
        Nationality = [English, Swede, Dane, Norwegian, German],
        domain(Nationality,1,5),
        Pet = [Dog, Birds, Cats, Horse, Zebra],
        domain(Pet,1,5),
        Smokes = [Pall_mall, Dunhill, Blend, Blue_master, Prince],
        domain(Smokes,1,5),
        Drinks = [Tea, Coffee, Milk, Beer, Water],
        domain(Drinks,1,5),     
        % Define constraints and relations
        % All different constraints
        all_different(House_colors), 
        all_different(Nationality),
        all_different(Pet),
        all_different(Smokes),
        all_different(Drinks),
        % Specific constraints    
        Red #= English, % The English man lives in the red house
        Dog #= Swede, % The Swede has a dog
        Tea #= Dane, % The Dane drinks tea
        Green #= White-1, %The green house is immediately to the left of the white house.
        Green #= Coffee, % They drink coffee in the green house
        Birds #=  Pall_mall, % The man who smokes Pall Mall has birds 
        Yellow #= Dunhill, %In the yellow house they smoke Dunhill
        Milk #= 3, %In the middle house they drink milk
        Norwegian #= 1, %The Norwegian lives in the first house
        Blend #= Cats-1 #\/ Blend #= Cats+1, %The man who smokes Blend lives in the house next to the house with cats 
        Dunhill #= Horse-1 #\/ Dunhill #= Horse+1, %In a house next to the house where they have a horse, they smoke Dunhill.
        Blue_master #= Beer, %The man who smokes Blue Master drinks beer
        German #= Prince, %The German smokes Prince
        Norwegian #= Blue-1 #\/ Norwegian #= Blue+1, %The Norwegian lives next to the blue house
        Water #= Blend-1 #\/ Water #= Blend+1, % They drink water in a house next to the house where they smoke Blend.     
        % append variables to one list
        append(House_colors, Nationality, Temp1),
        append(Temp1, Pet, Temp2),
        append(Temp2, Drinks, Temp3),
        append(Temp3, Smokes, VariableList),
        % find solution
        labeling([], VariableList),                                           
        % connect answers with right objects
        sort([Red-red, Green-green, White-white, Yellow-yellow, Blue-blue], House_color_connection),
        sort([English-english, Swede-swede, Dane-dane, Norwegian-norwegian, German-german], Nation_connection),  
        sort([Dog-dog, Birds-birds, Cats-cats, Horse-horse, Zebra-zebra], Pet_connection),
        sort([Pall_mall-pall_mall, Dunhill-dunhill, Blend-blend, Blue_master-blue_master, Prince-prince], Smokes_connection),
        sort([Tea-tea, Coffee-coffee, Beer-beer, Milk-milk, Water-water], Drinks_connection),
        % print solution
        Format = '~w~15|~w~30|~w~45|~w~60|~w~n',
        format(Format, ['house 1', 'house 2', 'house 3', 'house 4', 'house 5']),
        format(Format, House_color_connection),
        format(Format, Pet_connection),
        format(Format, Smokes_connection),
        format(Format, Drinks_connection),
        format(Format, Nation_connection).                                                        

            
        
