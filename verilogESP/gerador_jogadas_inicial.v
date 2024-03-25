module gerador_jogadas_inicial(
  input        clock,
  input        reset,
  input        novaJogada,
  input  [1:0] numJogada,
  output reg [2:0] coluna,
  output reg [2:0] linha
);

  reg [2:0] coluna1;
  reg [2:0] linha1;
  reg [2:0] coluna2;
  reg [2:0] linha2;
  reg [2:0] coluna3;
  reg [2:0] linha3;

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

  always @* begin
    case(numJogada)
      2'b00: begin
        linha <= linha1;
        coluna <= coluna1;
      end
      2'b01: begin
        linha <= linha2; 
        coluna <= coluna2;
      end
      2'b10: begin
        linha <= linha3;
        coluna <= coluna3;
      end
      default: begin
        linha <= 3'b000;
        coluna <= 3'b000;
      end
    endcase
  end
endmodule