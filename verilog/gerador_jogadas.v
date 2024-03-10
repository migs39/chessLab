module gerador_jogadas(
    input        clock,
    input        novaJogada,
    output [3:0] coluna,
    output [3:0] linha
);
    reg auxLinha;
    reg auxColuna;

    always @(posedge clock) begin
        if (novaJogada) begin
            auxLinha <= $urandom_range(8, 1);
            auxColuna <= $urandom_range(8, 1);
        end 
    end

    assign coluna = auxColuna;
    assign linha = auxLinha;

endmodule
