module gerador_jogadas(
  input        clock,
  input        reset,
  input        novaJogada,
  output reg [3:0] coluna,
  output reg [3:0] linha
);

  reg [3:0] auxLinha;
  reg [3:0] auxColuna;


  always @(posedge clock or posedge reset or posedge novaJogada) begin
    if(reset) begin
      auxLinha <= 4'b0001;
      auxColuna <= 4'b0001;
    end
    if (clock) begin
      if (auxLinha == 4'b1000) begin
        if (auxColuna == 4'b1000) begin
          auxColuna <= 4'b0001;
        end else begin
          auxColuna <= auxColuna + 4'b0001;
        end
        auxLinha <= 4'b0001;
      end else begin  
        auxLinha <= auxLinha + 4'b0001;
      end
    end
    if (novaJogada) begin
        coluna <= 4'b0001; 
        // coluna <= auxColuna;
        linha <= 4'b0001;
        // linha <= auxLinha;
    end 
  end

endmodule
