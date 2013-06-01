// Accellera Standard V2.3 Open Verification Library (OVL).
// Accellera Copyright (c) 2005-2008. All rights reserved.



`endmodule //Required to pair up with already used "`module" in file assert_never_unknown_async.vlib

//Module to be replicated for assert checks
//This module is bound to the PSL vunits with assert checks
module assert_never_unknown_async_assert (reset_n, test_expr, xzcheck_enable);
       parameter width = 8;
       input reset_n, xzcheck_enable;
       input [width-1:0] test_expr;
endmodule

