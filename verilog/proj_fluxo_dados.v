module proj_fluxo_dados (
 input clock,
 input [2:0] jogadaColuna,
 input [2:0] jogadaLinha,
 input novaJogada, 
 input registraR,
 input zeraT,
 input zeraR,
 input zeraP,
 input zeraG,
 input contaP,
 input contaT,
 input decresceT,
 input jogou,
 input salvaNova,
 input salvaInicial,

 output fimT,
 output acertou,
 output temJogada,
 output [2:0] linhaEsperada,
 output [2:0] colunaEsperada,
 output [7:0] pontos,
 output [2:0] db_linha,
 output [2:0] db_coluna
);

    wire [2:0] s_linha;
    wire [2:0] s_coluna;
    //output gerador padrao
    wire [2:0] s_linhaGerador;
    wire [2:0] s_colunaGerador;
    //outputs gerador inicial
    wire [2:0] s_linhaGerador1;
    wire [2:0] s_colunaGerador1;
    wire [2:0] s_linhaGerador2;
    wire [2:0] s_colunaGerador2;
    wire [2:0] s_linhaGerador3;
    wire [2:0] s_colunaGerador3;
    //outputs memoria 
    wire [2:0] s_linhaMemoria1;
    wire [2:0] s_colunaMemoria1;
    wire [2:0] s_linhaMemoria2;
    wire [2:0] s_colunaMemoria2; 
    wire [2:0] s_linhaMemoria3;
    wire [2:0] s_colunaMemoria3;  

    wire acertouLinha;
    wire acertouColuna;

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
        .linha1   ( s_linhaGerador1 ),
        .coluna1  ( s_colunaGerador1 ),
        .linha2  ( s_linhaGerador2 ),
        .coluna2  ( s_colunaGerador2 ),
        .linha3  ( s_linhaGerador3 ),
        .coluna3  ( s_colunaGerador3 )
    );


    memoria3bit memoriaJogadas (
        .clock( clock ),
        .reset( zeraG ),

  //iputs do gerador inicial
        .novaJogadaInit(salvaInicial),
        .colunaGerada1(s_colunaGerador1),
        .linhaGerada1(s_linhaGerador1),
        .colunaGerada2(s_colunaGerador2),
        .linhaGerada2(s_linhaGerador2),
        .colunaGerada3(s_colunaGerador3),
        .linhaGerada3(s_linhaGerador3),
  
  //iputs do gerador 1 jogada
        .novaJogada(salvaNova),
        .colunaGerada(s_linhaGerador),
        .linhaGerada(s_colunaGerador),

  //outputs
        .coluna1(s_colunaMemoria1),
        .linha1(s_linhaMemoria1),
        .coluna2(s_colunaMemoria2),
        .linha2(s_linhaMemoria2),
        .coluna3(s_colunaMemoria3),
        .linha3(s_linhaMemoria3)
    );

    contador_mod #(.M(30000), .N(15), .D(1000)) contador_timer (
        .clock  ( clock ),
        .zera_s ( zeraT ),
        .conta  ( contaT ),
        .decresce ( decresceT ),
        //.tempoDrec ( 4'd1000 ),
        //.Q      (  ),
        .fim    ( fimT )
    ); 

    contador_mod #(.M(255), .N(8), .D(1000)) contador_pontos (
        .clock  ( clock ),
        .zera_s ( zeraP ),
        .conta  ( contaP ),
        .decresce ( 1'b0 ),
    //    .tempoDrec ( 4'd0 ),
        .Q      ( pontos )
        //.fim    ( )
    ); 

    comparador_85 comparadorLinha (
        .A   ( s_linhaMemoria1 ),
        .B   ( s_linha ),
        .ALBi( 1'b0 ),
        .AGBi( 1'b0 ),
        .AEBi( 1'b1 ),
        .AEBo( acertouLinha )
    );

    comparador_85 comparadorColuna (
        .A   ( s_colunaMemoria1 ),
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
    assign linhaEsperada = s_linhaMemoria1;
    assign colunaEsperada = s_colunaMemoria1;

    // comparaçao
    assign acertou = acertouLinha & acertouColuna;

    // saidas de depuracao
    assign db_coluna = s_coluna;
    assign db_linha = s_linha;

endmodule
