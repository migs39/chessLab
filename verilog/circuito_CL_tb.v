
`timescale 1ns/1ns

module circuito_CL_tb;

    // Sinais para conectar com o DUT
    // valores iniciais para fins de simulacao (ModelSim)
    reg        clock_in   = 1;
    reg        reset_in   = 0;
    reg        iniciar_in = 0;
    reg  [3:0] colunas_in  = 4'b0000;
    reg  [3:0] linhas_in  = 4'b0000;
    reg        temJogada_in  = 0;
    reg        terminar_in  = 0;

    wire       acertou_out;
    wire       errou_out  ;
    wire       pronto_out ;

    wire [6:0] db_pontos1_out   ;
    wire [6:0] db_pontos2_out   ;
    wire [6:0] db_linhaEsperada_out    ;
    wire [6:0] db_estado_out     ;
    wire [6:0] db_colunaEsperada_out;
    wire [3:0] coluna_tb ;
    wire [3:0] linha_tb ;

    // Configuração do clock
    parameter clockPeriod = 20; // in ns, f=50MHz

    // Identificacao do caso de teste
    reg [31:0] caso = 0;

    // Gerador de clock
    always #((clockPeriod / 2)) clock_in = ~clock_in;

    // instanciacao do DUT (Device Under Test)
    circuito_CL dut(
      .clock (clock_in) ,
      .iniciar (iniciar_in) ,
      .jogadaFileira (linhas_in) ,
      .jogadaColuna (colunas_in) ,
      .temJogada (temJogada_in) ,
      .terminar (terminar_in) ,
      .reset (reset_in) ,
      .pontos1 (db_pontos2_out) ,
      .pontos2 (db_pontos1_out) ,
      .errou (errou_out) ,
      .db_acertou (acertou_out) ,
      .linhaEsperada (db_linhaEsperada_out) ,
      .colunaEsperada (db_colunaEsperada_out) ,
      .db_estado (db_estado_out) ,
      .db_coluna_tb (coluna_tb) ,
      .db_linha_tb (linha_tb)
    );

    // geracao dos sinais de entrada (estimulos)
    initial begin
      $display("Inicio da simulacao");

      // condicoes iniciais
      caso       = 0;
      clock_in   = 1;
      reset_in   = 0;
      iniciar_in = 0;
      colunas_in  = 4'b0000;
      linhas_in = 4'b0000;
      #clockPeriod;

      /*
       * Cenario de Teste 1 - acerta as 16 jogadas
       */

      // Teste 1. resetar circuito
      caso = 1;
      // gera pulso de reset
      @(negedge clock_in);
      reset_in = 1;
      #(clockPeriod);
      reset_in = 0;
      // espera
      #(10*clockPeriod);

      // Teste 2. iniciar=1 por 5 periodos de clock
      caso = 2;
      iniciar_in = 1;
      #(5*clockPeriod);
      iniciar_in = 0;
      // espera
      #(1000*clockPeriod);

      // Teste 3. jogar + contar 1 ponto
      caso = 3;
      @(negedge clock_in);
      colunas_in  = coluna_tb;
      linhas_in = linha_tb;
      #(10*clockPeriod);
      temJogada_in = 1'b1;
      #(2*clockPeriod);
      temJogada_in = 1'b0;
      // espera entre jogadas
      #(10*clockPeriod);

      // Teste 4. errar + esperar timeOut
      caso = 4;
      @(negedge clock_in);
      colunas_in = 4'b0010;
      linhas_in = 4'b0010;
      #(10*clockPeriod);
      temJogada_in = 1'b1;
      #(2*clockPeriod);
      temJogada_in = 1'b0;
      // espera timeOut
      #(30000*clockPeriod);

      // Teste 5. terminar
      caso = 5;
      @(negedge clock_in);
      terminar_in = 1'b1;
      #(10*clockPeriod);
      terminar_in = 1'b0;
      // espera
      #(10*clockPeriod);


      // final dos casos de teste da simulacao
      caso = 99;
      #100;
      $display("Fim da simulacao");
      $stop;
    end

  endmodule
