module gerador_jogadas_inicial(
  input        clock,
  input        reset,
  input        novaJogada,
  output reg [2:0] coluna1,
  output reg [2:0] linha1,
  output reg [2:0] coluna2,
  output reg [2:0] linha2,
  output reg [2:0] coluna3,
  output reg [2:0] linha3
);

  wire [17:0] auxQ;
  reg [5:0] auxQ1;
  reg [5:0] auxQ2;
  reg [5:0] auxQ3;

  contador_m #(.M(262143), .N(18)) contador_geradorJogadasInicial (
      .clock  ( clock ),
      .zera_s ( reset ),
      .conta  ( 1'b1 ),
      .Q      ( auxQ )
  ); 

  always @(posedge novaJogada) begin
    auxQ1 <=  auxQ % 64;
    auxQ2 <=  ( auxQ >> 6 ) % 64; 
    auxQ3 <=  ( auxQ >> 12 );     
  end

  always @* begin
    //saida 1
    coluna1 = auxQ1 / 8;
    linha1 = auxQ1 % 8;
    //saida 2
    coluna2 = auxQ2 / 8;
    linha2 = auxQ2 % 8;
    //saida 3
    coluna3 = auxQ3 / 8;
    linha3 = auxQ3 % 8;
  end
endmodule