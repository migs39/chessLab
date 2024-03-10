module circuito_exp5 (
 input clock,
 input iniciar,
 input jogadaFileira [3:0],
 input jogadaColuna [3:0],
 input temJogada,
 input terminar,
 input reset,
 output pontos1 [6:0],
 output pontos2 [6:0],
 output errou,,
 output db_acertou,
 output [6:0] linhaEsperada,
 output [6:0] colunaEsperada,
 output [6:0] db_estado
);

    wire fimTWire;
    wire registraRWire;
    wire zeraTwire;
    wire zeraRwire;
    wire zeraPwire;
    wire contaPwire;
    wire contaTwire;
    wire decresceTWire;
    wire fimTWire;
    wire acertouWire;
    wire temJogadaWire;

    wire [7:0]pontosWire;
    wire [3:0]linhaEsperadaWire;
    wire [3:0]colunaEsperadaWire;
    wire [3:0]db_linhaWire;
    wire [3:0]db_colunaWire;
 

    proj_fluxo_dados FD(
        //entrada
        .clock              ( clock ),
        .jogadaColuna       ( jogadaColuna ),
        .jogadaFileira      ( jogadaFileira ),
        .novaJogada         ( jogadaFeita ),
        .registraR          ( registraRWire ),
        .zeraT              ( zeraTWire ),
        .zeraR              ( zeraRwire ),
        .zeraP              ( zeraPWire ),
        .contaP             ( zeraTWire ),
        .contaT             ( contaTWire ),
        .decresceT          ( decresceTWire ),
        .temJogada          ( temJogada ),
        //saida
        .fimT               ( fimTWire ),
        .acertou            ( acertouWire ),
        .temJogada          ( temJogadaWire ),
        .linhaEsperada      ( linhaEsperadaWire ),
        .colunaEsperada     ( colunaEsperadaWire ),
        .pontos             ( pontosWire ),
        .db_linha           ( db_linhaWire ),
        .db_coluna          ( db_colunaWire ),
    );

    exp5_unidade_controle UC (
        //entrada
        .clock        ( clock ),
        .reset        ( reset ),
        .iniciar      ( iniciar ),
        .fimT         ( fimTWire ),
        .acertou      ( acertouWire ),
        .temJogada    ( temJogadaWire ),
        .terminar     ( terminar ),
        //saida
        .registraR    ( registarRWire ),
        .zeraT        ( zeraTwire ),
        .zeraR        ( zeraRWire ),
        .zeraP        ( zeraPWire ),
        .contaP       ( contaPWire ),
        .contaT       ( contaTwire ),
        .decresceT    ( decresceTWire ),
        .db_estado    ( db_estadoWire )
    );

    hexa7seg Hex0 (
        .hexa               (linhaEsperada),
        .display            (linhaEsperadaWire)
    );

    hexa7segABC Hex1 (
        .hexa               (colunaEsperada),
        .display            (colunaEsperadaWire)
    );

    hexa7seg Hex2 (
        .hexa               (pontosWire[3:0]), //nao sei se ta certa essa notacao
        .display            (pontos1)
    );

    hexa7seg Hex3 (
        .hexa               (pontosWire[7:4]), //nao sei se ta certa essa notacao
        .display            (pontos2)
    );

    hexa7seg Hex5 (
        .hexa               (db_estadoWire),
        .display            (db_estado) 
    );

    assign db_acertou = acertouWire; //Tem q adicionar um timer nisso pra mostrar por algum tempinho
    assign errou = decresceTWire; //Tem q adicionar um timer nisso pra mostrar por algum tempinho
endmodule
