// Accellera Standard V2.3 Open Verification Library (OVL).
// Accellera Copyright (c) 2005-2008. All rights reserved.



`endmodule //Required to pair up with already used "`module" in file assert_always.vlib

//Module to be replicated for assert checks
//This module is bound to the PSL vunits with assert checks
module assert_always_assert (clk, reset_n, test_expr, xzcheck_enable);
       input clk, reset_n, test_expr, xzcheck_enable;
endmodule

//Module to be replicated for assume checks
//This module is bound to a PSL vunits with assume checks
module assert_always_assume (clk, reset_n, test_expr, xzcheck_enable);
       input clk, reset_n, test_expr, xzcheck_enable;
endmodule
