
module unidade_controle (
    input clock,
    input reset,
    input iniciar,
    input fimT,
    input acertou,
    input temJogada,
    input terminar,

    output reg registraR,
    output reg zeraT,
    output reg zeraR,
    output reg zeraP,
    output reg zeraG,
    output reg contaP,
    output reg contaT,
    output reg decresceT,
    output reg [3:0] db_estado,
    output reg salvaNova,
    output reg salvaInicial,
    output reg geraNova
);

    // Define estados
    parameter inicial = 4'b0000;  // 0
    parameter iniciaElementos = 4'b0001;  // 1
    parameter iniciaMemoria = 4'b1000;  // 8
    parameter espera = 4'b0010;  // 2
    parameter registra = 4'b0011;  // 3
    parameter compara = 4'b0100;  // 4s
    parameter resetGen = 4'b0101; // 5'
    parameter decresce = 4'b1110;  // E
    parameter contaPonto = 4'b1010;  // A
    parameter geraJogada = 4'b0110;  // 6 porque parece um g
    parameter salvaJogada = 4'b0111; // 7
    parameter fimJogada = 4'b1001; // 9 porque eh o fim dos decimais
    parameter fim = 4'b1111;  // F

    // Variaveis de estado
    reg [3:0] Eatual, Eprox;

    // Memoria de estado
    always @(posedge clock or posedge reset) begin
        if (reset)
            Eatual <= inicial;
        else
            Eatual <= Eprox;
    end

    // Logica de proximo estado
    always @* begin
        case (Eatual)
            resetGen:        Eprox = inicial;
            inicial:         Eprox = iniciar ? iniciaElementos : inicial; 
            iniciaElementos: Eprox = iniciaMemoria;
            iniciaMemoria:   Eprox = espera;
            espera:          Eprox = fimT ? fim : (temJogada ? registra : espera);
            registra:        Eprox = compara;
            compara:         Eprox = acertou ? contaPonto : decresce;
            decresce:        Eprox = fimJogada;
            contaPonto:      Eprox = geraJogada;
            geraJogada:      Eprox = salvaJogada;
            salvaJogada:     Eprox = fimJogada;
            fimJogada:       Eprox = espera;
            fim:             Eprox = terminar ? inicial : fim;
            default:         Eprox = resetGen;
        endcase
    end

    // Logica de saida (maquina Moore)
    always @* begin

        registraR = (Eatual == registra) ? 1'b1 : 1'b0;
        zeraT = (Eatual == iniciaElementos) ? 1'b1 : 1'b0;
        zeraR = (Eatual == inicial) ? 1'b1 : 1'b0;
        zeraP = (Eatual == iniciaElementos) ? 1'b1 : 1'b0;
        zeraG = (Eatual == resetGen) ? 1'b1 : 1'b0;
        contaP = (Eatual == contaPonto) ? 1'b1 : 1'b0;
        contaT = (Eatual == inicial || Eatual == iniciaElementos || Eatual == fim ) ? 1'b0 : 1'b1; // saida invertida por conta dos estados escolhidos
        decresceT = (Eatual == decresce) ? 1'b1 : 1'b0;
        geraNova = (Eatual == geraJogada || Eatual == iniciaElementos) ? 1'b1 : 1'b0;
        salvaInicial = (Eatual == iniciaMemoria) ? 1'b1 : 1'b0;
        salvaNova = (Eatual == salvaJogada) ? 1'b1 : 1'b0;


        case (Eatual)
            inicial:         db_estado = 4'b0000;  // 0
            iniciaElementos: db_estado = 4'b0001;  // 1
            iniciaMemoria:   db_estado = 4'b1000;  // 8
            espera:          db_estado = 4'b0010;  // 2
            registra:        db_estado = 4'b0011;  // 3
            compara:         db_estado = 4'b0100;  // 4
            resetGen:        db_estado = 4'b0101;  // 5
            decresce:        db_estado = 4'b1110;  // E
            contaPonto:      db_estado = 4'b1010;  // A
            geraJogada:      db_estado = 4'b0110;  // 6 porque parece um g
            salvaJogada:     db_estado = 4'b0110;  // 7
            fimJogada:       db_estado = 4'b1001; // 9 porque eh o fim dos decimais
            fim:             db_estado = 4'b1111;  // F
            default:         db_estado = 4'b1101;  // D
        endcase
    end

endmodule
