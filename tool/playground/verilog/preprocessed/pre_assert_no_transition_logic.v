// Accellera Standard V2.3 Open Verification Library (OVL).
// Accellera Copyright (c) 2005-2008. All rights reserved.




    //Do nothing
  wire valid_test_expr;
  wire valid_start_state;
  wire valid_next_state;

  assign valid_test_expr = ~((^test_expr)^(^test_expr));
  assign valid_start_state = ~((^start_state)^(^start_state));
  assign valid_next_state = ~((^next_state)^(^next_state));



