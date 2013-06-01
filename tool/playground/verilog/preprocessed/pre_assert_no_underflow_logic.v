// Accellera Standard V2.3 Open Verification Library (OVL).
// Accellera Copyright (c) 2005-2008. All rights reserved.




    //Do nothing
  wire valid_test_expr;
  assign valid_test_expr = ~((^test_expr) ^ (^test_expr));







    //Do nothing

  always @(posedge clk)
    begin
      if (`OVL_RESET_SIGNAL != 1'b0)
        begin
          if (valid_test_expr == 1'b1)
            begin
              // Do Nothing
            end
          else
            ovl_error_t(`OVL_FIRE_XCHECK,"test_expr contains X or Z");
        end
    end

