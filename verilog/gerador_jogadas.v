module gerador_jogadas(
  input        clock,
  input        novaJogada,
  output reg [3:0] coluna,
  output reg [3:0] linha
);

  reg [2:0] auxLinha;
  reg [2:0] auxColuna;


  always @(posedge clock) begin
    if (auxLinha == 3'b111) begin
        if (auxColuna == 3'b111) begin
            auxColuna <= 3'b000;
        end else begin
            auxColuna <= auxColuna + 3'b001;
        end
        auxLinha <= 3'b000;
    end else begin
      auxLinha <= auxLinha + 3'b001;
    end
    if (novaJogada) begin
        coluna = 4'b0010;//(auxColuna ^ 3'b011) + 4'b0001;
        linha = 4'b0010;//(auxLinha ^ 3'b101)  + 4'b0001; 
    end 
  end

endmodule
