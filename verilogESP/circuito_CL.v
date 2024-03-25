module circuito_CL (
 input clock,
// input terminar,
// input reset,
 output [6:0] pontos1,
 output [6:0] pontos2,
 output db_acertou,
 output [6:0] linhaEsperada,
 output [6:0] colunaEsperada,
 output [6:0] db_estado,
 //inputs esp
 input [2:0] jogadaFileira,
 input [2:0] jogadaColuna,
 input iniciar,
 input fimT,
 //outputs esp
 output [2:0] colunaGerada,
 output [2:0] linhaGerada,
 output salvaNova,
 output decresceT
);
	 reg reset = 1'b0;
    wire registraRWire;

    wire zeraRWire;

    wire zeraGWire;

    wire contaTWire;

    wire acertouWire;
    wire temJogadaWire;
    wire novaJogadaWire;
    wire salvaInicialWire;
    wire salvaNovaWire;

    wire [1:0]numJogada;
    wire numGerador;

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
        .zeraR              ( zeraRWire ),
        .zeraG              ( zeraGWire ),
        .jogou              ( iniciar ),

        .numJogada          (numJogada),


        .numGerador         (numGerador),
        .salvaNova          (salvaNovaWire),

        //saida
        .s_linhaGerada        (linhaGerada),
        .s_colunaGerada       (colunaGerada),

        .acertou            ( acertouWire ),
        .temJogada          ( temJogadaWire ),
        .linhaEsperada      ( linhaEsperadaWire ),
        .colunaEsperada     ( colunaEsperadaWire ),
        .db_linha           ( db_linhaWire ),
        .db_coluna          ( db_colunaWire )
    );

    unidade_controle UC (
        //entrada
        .clock        ( clock ),
        .reset        ( reset ),
        .iniciar      ( iniciar ),
        .fimT         ( fimT ),
        .acertou      ( acertouWire ),
        .temJogada    ( temJogadaWire ),
        //.terminar     ( terminar ),

        //saida
        .registraR    ( registraRWire ),
        .zeraT        ( zeraT ),
        .zeraR        ( zeraRWire ),
        .zeraP        ( zeraP ),
        .zeraG        ( zeraGWire ),
        //.contaP       ( contaP ),
        //.contaT       ( contaT ),
        .decresceT    ( decresceT ),
        .db_estado    ( db_estadoWire ),
        .salvaNova    ( salvaNovaWire ),
        .geraNova     ( novaJogadaWire ),
        .numGerador   (numGerador),
        .numJogada    (numJogada)
    );

    hexa7seg Hex0 (
        .hexa               (linhaEsperadaWire),
        .display            (linhaEsperada)
    );

    hexa7segABC Hex1 (
        .hexa               (colunaEsperadaWire),
        .display            (colunaEsperada)
    );

    hexa7seg Hex5 (
        .hexa               (db_estadoWire),
        .display            (db_estado) 
    );


    assign db_acertou = acertouWire; 
    assign salvaNova = salvaNovaWire;
endmodule
