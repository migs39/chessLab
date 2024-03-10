module proj_fluxo_dados (
 input clock,
 input [3:0] jogadaColuna,
 input [3:0] jogadaLinha,
 input novaJogada, 
 input registraR,
 input zeraT,
 input zeraR,
 input zeraP,
 input contaP,
 input contaT,
 input decresceT,
 input jogou,
 output fimT,
 output acertou,
 output temJogada,
 output [3:0] linhaEsperada,
 output [3:0] colunaEsperada,
 output [7:0] pontos,
 output [3:0] db_linha,
 output [3:0] db_coluna
);

    wire [3:0] s_linha;
    wire [3:0] s_coluna;
    wire [3:0] s_linhaGerador;
    wire [3:0] s_colunaGerador; 
    wire acertouLinha;
    wire acertouColuna;

    gerador_jogadas gerador (
        .clock ( clock ),
        .novaJogada ( novaJogada ),
        .linha   ( s_linhaGerador ),
        .coluna  ( s_colunaGerador )
    );

    contador_m #(.M(30000), .N(15)) contador_timer (
        .clock  ( clock ),
        .zera_s ( zeraT ),
        .conta  ( contaT ),
        .decresce ( decresceT ),
    //    .tempoDrec ( 4'd1000 ),
        // .Q      (  ),
        .fim    ( fimT )
    ); 

    contador_m #(.M(255), .N(8)) contador_pontos (
        .clock  ( clock ),
        .zera_s ( zeraP ),
        .conta  ( contaP ),
        .decresce ( 1'b0 ),
    //    .tempoDrec ( 4'd0 ),
        .Q      ( pontos )
        //.fim    ( )
    ); 

    comparador_85 comparadorLinha (
        .A   ( s_linhaGerador ),
        .B   ( s_linha ),
        .ALBi( 1'b0 ),
        .AGBi( 1'b0 ),
        .AEBi( 1'b1 ),
        .AEBo( acertouLinha )
    );

    comparador_85 comparadorColuna (
        .A   ( s_colunaGerador ),
        .B   ( s_coluna ),
        .ALBi( 1'b0 ),
        .AGBi( 1'b0 ),
        .AEBi( 1'b1 ),
        .AEBo( acertouColuna )
    );

    registrador_4 registradorLinha (
        .clock( clock ),
        .clear( zeraR ),
        .enable( registraR ),
        .D( jogadaLinha ),
        .Q( s_linha )
    );

    registrador_4 registradorColuna (
        .clock( clock ),
        .clear( zeraR ),
        .enable( registraR ),
        .D( jogadaColuna ),
        .Q( s_coluna )
    );

    edge_detector detector(
        .clock(clock),
        .sinal(jogou),
        .reset(zeraR),
        .pulso(temJogada)
    );
    
    // jogadas esperadas
    assign linhaEsperada = s_linhaGerador;
    assign colunaEsperada = s_colunaGerador;

    // comparaçao
    assign acertou = acertouLinha & acertouColuna;

    // saidas de depuracao
    assign db_coluna = s_coluna;
    assign db_linha = s_linha;

endmodule
