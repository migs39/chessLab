
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
    output reg geraNova,
    output reg numGerador,
    output reg [1:0] numJogada
);

    // Define estados
    parameter inicial = 5'b00000;  // 0
    parameter iniciaElementos = 5'b00001;  // 1
    parameter iniciaMemoria1 = 5'b01000;  // 8
    parameter esperaMemoria1 = 5'b10001;
    parameter iniciaMemoria2 = 5'b01011;  // B
    parameter esperaMemoria2 = 5'b10010;
    parameter iniciaMemoria3 = 5'b01100;  // C
    parameter espera = 5'b00010;  // 2
    parameter registra = 5'b00011;  // 3
    parameter compara = 5'b00100;  // 4
    parameter resetGen = 5'b00101; // 5
    parameter decresce = 5'b01110;  // E
    parameter contaPonto = 5'b01010;  // A
    parameter geraJogada = 5'b00110;  // 6 porque parece um g
    parameter salvaJogada = 5'b00111; // 7
    parameter fimJogada = 5'b01001; // 9 porque eh o fim dos decimais
    parameter fim = 5'b01111;  // F

    // Variaveis de estado
    reg [4:0] Eatual, Eprox;

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
            iniciaElementos: Eprox = iniciaMemoria1;
            iniciaMemoria1:  Eprox = esperaMemoria1;
            esperaMemoria1:  Eprox = iniciaMemoria2;
            iniciaMemoria2:  Eprox = esperaMemoria2;
            esperaMemoria2:  Eprox = iniciaMemoria3;
            iniciaMemoria3:  Eprox = espera;
            espera:          Eprox = fimT ? fim : (temJogada ? registra : espera);
            registra:        Eprox = compara;
            compara:         Eprox = acertou ? contaPonto : decresce;
            decresce:        Eprox = fimJogada;
            contaPonto:      Eprox = geraJogada;
            geraJogada:      Eprox = salvaJogada;
            salvaJogada:     Eprox = fimJogada;
            fimJogada:       Eprox = espera;
            fim:             Eprox = inicial;
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
        salvaNova = (Eatual == salvaJogada || Eatual == iniciaMemoria1 || Eatual == iniciaMemoria2 || Eatual == iniciaMemoria3) ? 1'b1 : 1'b0;
        numGerador = (Eatual == geraJogada || Eatual == salvaJogada )? 1'b1 : 1'b0;

        case (Eatual)
            iniciaElementos:  numJogada = 2'b00;
            iniciaMemoria1:   numJogada = 2'b00;
            esperaMemoria1:   numJogada = 2'b01;
            iniciaMemoria2:   numJogada = 2'b01;
            esperaMemoria2:   numJogada = 2'b10;
            iniciaMemoria3:   numJogada = 2'b10;
            default:          numJogada = 2'b00; 
        endcase

        case (Eatual)
            inicial:         db_estado = 4'b0000;  // 0
            iniciaElementos: db_estado = 4'b0001;  // 1
            iniciaMemoria1:   db_estado = 4'b1000;  // 8
            espera:          db_estado = 4'b0010;  // 2
            registra:        db_estado = 4'b0011;  // 3
            compara:         db_estado = 4'b0100;  // 4
            resetGen:        db_estado = 4'b0101;  // 5
            decresce:        db_estado = 4'b1110;  // E
            contaPonto:      db_estado = 4'b1010;  // A
            geraJogada:      db_estado = 4'b0110;  // 6 porque parece um g
            salvaJogada:     db_estado = 4'b0111;  // 7
            fimJogada:       db_estado = 4'b1001; // 9 porque eh o fim dos decimais
            fim:             db_estado = 4'b1111;  // F
            default:         db_estado = 4'b1101;  // D
        endcase
    end

endmodule
