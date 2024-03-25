module proj_fluxo_dados (
 input clock,
 input [2:0] jogadaColuna,
 input [2:0] jogadaLinha,
 input novaJogada, 
 input registraR,
 input zeraR,
 input zeraG,
 input jogou,


 input [1:0] numJogada,

 input numGerador,
 input salvaNova,

 output [2:0]s_linhaGerada,
 output [2:0]s_colunaGerada,

 output acertou,
 output temJogada,

 output [2:0] linhaEsperada,
 output [2:0] colunaEsperada,
 output [2:0] db_linha,
 output [2:0] db_coluna
);

    wire [2:0] s_linha;
    wire [2:0] s_coluna;
    //output gerador padrao
    wire [2:0] s_linhaGerador;
    wire [2:0] s_colunaGerador;
    //outputs gerador inicial
    wire [2:0] s_linhaGerador_init;
    wire [2:0] s_colunaGerador_init;
    //inputs comparador
    wire [2:0] s_colunaMemoria;
    wire [2:0] s_linhaMemoria;

    wire acertouLinha;
    wire acertouColuna;


    memoria3bit mem(
        .clock(clock),
        .reset(zeraG),

        //iputs do gerador
        .novaJogada(salvaNova),
        .colunaGerada(s_colunaGerada),
        .linhaGerada(s_linhaGerada),

        .coluna(s_colunaMemoria),
        .linha(s_linhaMemoria)
    );

    seletorGerador seletor(
        .clock(clock),
        .numGerador(numGerador),
        .linhaGen1(s_linhaGerador_init),
        .colunaGen1(s_colunaGerador_init),
        .linhaGen2(s_linhaGerador),
        .colunaGen2(s_colunaGerador),
        .coluna(s_colunaGerada),
        .linha(s_linhaGerada)
    );

    gerador_jogadas gerador (
        .clock ( clock ),
        .reset  ( zeraG ),
        .novaJogada ( novaJogada ),
        .linha   ( s_linhaGerador ),
        .coluna  ( s_colunaGerador )
    );

    gerador_jogadas_inicial geradorInicial (
        .clock ( clock ),
        .reset  ( zeraG ),
        .novaJogada ( novaJogada ),
        .numJogada  ( numJogada ),
        .linha   ( s_linhaGerador_init ),
        .coluna  ( s_colunaGerador_init )
    );



    comparador_85 comparadorLinha (
        .A   ( s_linhaMemoria ),
        .B   ( s_linha ),
        .ALBi( 1'b0 ),
        .AGBi( 1'b0 ),
        .AEBi( 1'b1 ),
        .AEBo( acertouLinha )
    );

    comparador_85 comparadorColuna (
        .A   ( s_colunaMemoria ),
        .B   ( s_coluna ),
        .ALBi( 1'b0 ),
        .AGBi( 1'b0 ),
        .AEBi( 1'b1 ),
        .AEBo( acertouColuna )
    );

    registrador_3 registradorLinha (
        .clock( clock ),
        .clear( zeraR ),
        .enable( registraR ),
        .D( jogadaLinha ),
        .Q( s_linha )
    );

    registrador_3 registradorColuna (
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
    assign linhaEsperada = s_linhaMemoria;
    assign colunaEsperada = s_colunaMemoria;

    // comparaçao
    assign acertou = acertouLinha & acertouColuna;

    // saidas de depuracao
    assign db_coluna = s_coluna;
    assign db_linha = s_linha;

endmodule
