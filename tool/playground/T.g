grammar T;
<<<<<<< HEAD
<<<<<<< HEAD
s : a* ;

a : 'var' INT ';'
  | 'var' INT '.' 
  ;
INT : [0-9]+ ;
WS : [ \t\n]+ -> skip ;
=======
=======
>>>>>>> 710d1115c0ec8e8e2933f633eda4cf9fcfd5bc0c
s : (ID | ID ID?) ID ;
//s2 : ID INT | ID INT | ID INT INT;
ID : 'a'..'z'+ ;
INT : '0'..'9'+;
WS : (' '|'\n') {skip();} ;
<<<<<<< HEAD
>>>>>>> 710d1115c0ec8e8e2933f633eda4cf9fcfd5bc0c
=======
>>>>>>> 710d1115c0ec8e8e2933f633eda4cf9fcfd5bc0c
