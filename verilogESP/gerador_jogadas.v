module gerador_jogadas(
  input        clock,
  input        reset,
  input        novaJogada,
  output reg [2:0] coluna,
  output reg [2:0] linha
);

  wire [5:0] auxQ;

  contador_m #(.M(63), .N(6)) contador_geradorJogadas (
      .clock  ( clock ),
      .zera_s ( reset ),
      .conta  ( 1'b1 ),
      .Q      ( auxQ )
  ); 

  always @(posedge novaJogada) begin
    coluna <= auxQ / 8;
    linha <= auxQ % 8;
  end

endmodule
