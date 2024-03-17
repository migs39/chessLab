module circuito_CL (
 input clock,
 input iniciar,
 input [2:0] jogadaFileira,
 input [2:0] jogadaColuna,
 input temJogada,
 input terminar,
 input reset,
 output [6:0] pontos1,
 output [6:0] pontos2,
 output errou,
 output db_acertou,
 output [6:0] linhaEsperada,
 output [6:0] colunaEsperada,
 output [6:0] db_estado
);

    wire fimTWire;
    wire registraRWire;
    wire zeraTWire;
    wire zeraRWire;
    wire zeraPWire;
    wire zeraGWire;
    wire contaPWire;
    wire contaTWire;
    wire decresceTWire;
    wire acertouWire;
    wire temJogadaWire;
    wire novaJogadaWire;
    wire salvaInicialWire;
    wire salvaNovaWire;

    wire [7:0]pontosWire;
    wire [2:0]linhaEsperadaWire;
    wire [2:0]colunaEsperadaWire;
    wire [2:0]db_linhaWire;
    wire [2:0]db_colunaWire;
    wire [3:0]db_estadoWire;
 

    proj_fluxo_dados FD(
        //entrada
        .clock              ( clock ),
        .jogadaColuna       ( jogadaColuna ),
        .jogadaLinha        ( jogadaFileira ),
        .novaJogada         ( novaJogadaWire ),
        .registraR          ( registraRWire ),
        .zeraT              ( zeraTWire ),
        .zeraR              ( zeraRWire ),
        .zeraP              ( zeraPWire ),
        .zeraG              ( zeraGWire ),
        .contaP             ( contaPWire ),
        .contaT             ( contaTWire ),
        .decresceT          ( decresceTWire ),
        .jogou              ( temJogada ),
        .salvaInicial       ( salvaInicialWire ),
        .salvaNova          ( salvaNovaWire ),
        //saida
        .fimT               ( fimTWire ),
        .acertou            ( acertouWire ),
        .temJogada          ( temJogadaWire ),
        .linhaEsperada      ( linhaEsperadaWire ),
        .colunaEsperada     ( colunaEsperadaWire ),
        .pontos             ( pontosWire ),
        .db_linha           ( db_linhaWire ),
        .db_coluna          ( db_colunaWire )
    );

    unidade_controle UC (
        //entrada
        .clock        ( clock ),
        .reset        ( reset ),
        .iniciar      ( iniciar ),
        .fimT         ( fimTWire ),
        .acertou      ( acertouWire ),
        .temJogada    ( temJogadaWire ),
        .terminar     ( terminar ),
        //saida
        .registraR    ( registraRWire ),
        .zeraT        ( zeraTWire ),
        .zeraR        ( zeraRWire ),
        .zeraP        ( zeraPWire ),
        .zeraG        ( zeraGWire ),
        .contaP       ( contaPWire ),
        .contaT       ( contaTWire ),
        .decresceT    ( decresceTWire ),
        .db_estado    ( db_estadoWire ),
        .salvaInicial ( salvaInicialWire ),
        .salvaNova    ( salvaNovaWire ),
        .geraNova     ( novaJogadaWire )
    );

    hexa7seg Hex0 (
        .hexa               (linhaEsperadaWire),
        .display            (linhaEsperada)
    );

    hexa7segABC Hex1 (
        .hexa               (colunaEsperadaWire),
        .display            (colunaEsperada)
    );

    hexa7seg Hex2 (
        .hexa               (pontosWire[3:0]), 
        .display            (pontos1)
    );

    hexa7seg Hex3 (
        .hexa               (pontosWire[7:4]), 
        .display            (pontos2)
    );

    hexa7seg Hex5 (
        .hexa               (db_estadoWire),
        .display            (db_estado) 
    );

    assign db_acertou = acertouWire; 
    assign errou = decresceTWire; 
endmodule
