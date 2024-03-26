module seletorGerador(
  input        clock,
  input        numGerador,
  input [2:0]  linhaGen1,
  input [2:0]  colunaGen1,
  input [2:0]  linhaGen2,
  input [2:0]  colunaGen2,
  output reg [2:0] coluna,
  output reg [2:0] linha
);
  always @* begin
    case(numGerador)
      1'b0: begin
        linha <= linhaGen1;
        coluna <= colunaGen1;
      end
      1'b1: begin
        linha <= linhaGen1; 
        coluna <= colunaGen2;
      end
      default: begin
        linha <= 3'b000;
        coluna <= 3'b000;
      end
    endcase
  end
endmodule