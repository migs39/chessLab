module gerador_jogadas(
  input        clock,
  input        reset,
  input        novaJogada,
  output reg [3:0] coluna,
  output reg [3:0] linha
);

  reg [2:0] auxLinha;
  reg [2:0] auxColuna;


  always @(posedge clock) begin
    if(reset) begin
      auxLinha <= 3'b000;
      auxColuna <= 3'b000;
    end
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
        coluna <= 4'b0001;// {1'b0, auxColuna}; //+ // ^ 4'b1010 
        linha <= 4'b0001;// {1'b0, auxLinha}; //+ // ^ 4'b1010 
    end 
  end

endmodule
