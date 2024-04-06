module memoria3bit(
  input        clock,
  input        reset,

  //iputs do gerador
  input        novaJogada,
  input        colunaGerada,
  input        linhaGerada,

  output reg [2:0] coluna,
  output reg [2:0] linha
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
        end 
    end 
end

always @*
begin
    coluna = memoria[0];
    linha = memoria[1];

end

endmodule