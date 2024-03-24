module memoria3bit(
  input        clock,
  input        reset,

  //iputs do gerador inicial
  input        novaJogadaInit,
  input        colunaGerada1,
  input        linhaGerada1,
  input        colunaGerada2,
  input        linhaGerada2,
  input        colunaGerada3,
  input        linhaGerada3,
  
  //iputs do gerador padrao
  input        novaJogada,
  input        colunaGerada,
  input        linhaGerada,

  output reg [2:0] coluna1,
  output reg [2:0] linha1,
  output reg [2:0] coluna2,
  output reg [2:0] linha2,
  output reg [2:0] coluna3,
  output reg [2:0] linha3
);


reg [2:0] memoria [5:0]; //memoria 3 bit

always @ (posedge reset or posedge clock)
begin
    if (reset) begin
        memoria[0] <= 3'b000; //coluna
        memoria[1] <= 3'b000; //linha
        memoria[2] <= 3'b000; //coluna
        memoria[3] <= 3'b000; //linha
        memoria[4] <= 3'b000; //coluna
        memoria[5] <= 3'b000; //linha
    end else begin 
        // coloca 1 jogada
        if (novaJogada) begin
            //atualiza colunas
            memoria [0] <= memoria [2];
            memoria [2] <= memoria [4];
            memoria [4] <= colunaGerada;
            //atualiza linhas
            memoria [1] <= memoria [3];
            memoria [3] <= memoria [5];
            memoria [5] <= linhaGerada;
        // coloca 3 jogadas
        end else if (novaJogadaInit) begin
            //atualiza colunas
            memoria[0] <= colunaGerada1;
            memoria[2] <= colunaGerada2;
            memoria[4] <= colunaGerada3;
        
            //atualiza linhas
            memoria[1] <= linhaGerada1;
            memoria[3] <= linhaGerada2;
            memoria[5] <= linhaGerada3;
        end 
    end 
end

always @*
begin
    coluna1 = memoria[0];
    coluna2 = memoria[2];
    coluna3 = memoria[4];
    linha1 = memoria[1];
    linha2 = memoria[3];
    linha3 = memoria[5];
end

endmodule