
`timescale 1ns/1ns

module gerador_tb;

    // Sinais para conectar com o DUT
    // valores iniciais para fins de simulacao (ModelSim)
    reg        clock_in   = 1;
    reg        reset_in   = 0;
    reg        novaJogada_in = 0;

    wire [2:0] s_colunaGerador ;
    wire [2:0] s_linhaGerador ;
    wire [2:0] s_colunaGerador1 ;
    wire [2:0] s_linhaGerador1 ;
    wire [2:0] s_colunaGerador2 ;
    wire [2:0] s_linhaGerador2 ;
    wire [2:0] s_colunaGerador3 ;
    wire [2:0] s_linhaGerador3 ;
    

    // Configuração do clock
    parameter clockPeriod = 20; // in ns, f=50MHz

    // Identificacao do caso de teste
    reg [31:0] caso = 0;

    // Gerador de clock
    always #((clockPeriod / 2)) clock_in = ~clock_in;

    // instanciacao do DUT (Device Under Test)
    gerador_jogadas dut1 (
        .clock ( clock_in ),
        .reset  (reset_in),
        .novaJogada ( novaJogada_in ),
        .linha   ( s_linhaGerador ),
        .coluna  ( s_colunaGerador )
    );

    gerador_jogadas_inicial dut2 (
        .clock ( clock_in ),
        .reset  (reset_in),
        .novaJogada ( novaJogada_in ),
        .linha1   ( s_linhaGerador1 ),
        .coluna1  ( s_colunaGerador1 ),
        .linha2  ( s_linhaGerador2 ),
        .coluna2  ( s_colunaGerador2 ),
        .linha3  ( s_linhaGerador3 ),
        .coluna3  ( s_colunaGerador3 )
    );

    // geracao dos sinais de entrada (estimulos)
    initial begin
      $display("Inicio da simulacao");

      // condicoes iniciais
      caso       = 0;
      clock_in   = 1;
      reset_in   = 0;
      #clockPeriod;


      // Teste 1. gera 1 rodada
      caso = 1;
      @(negedge clock_in);
      novaJogada_in = 1;
      #(clockPeriod);
      novaJogada_in = 0;
      // espera
      #(5*clockPeriod);

      // Teste 2. gera 2 jogada
      caso = 2;
      @(negedge clock_in);
      novaJogada_in = 1;
      #(clockPeriod);
      novaJogada_in = 0;
      // espera
      #(5*clockPeriod);

      // Teste 3. reseta circuito
      caso = 3;
      @(negedge clock_in);
      reset_in = 1;
      #(clockPeriod);
      reset_in = 0;
      // espera
      #(5*clockPeriod);

      // Teste 4. gera 4 rodada
      caso = 4;
      @(negedge clock_in);
      novaJogada_in = 1;
      #(clockPeriod);
      novaJogada_in = 0;
      // espera
      #(260000*clockPeriod);

      // Teste 5. gera 5 jogada
      caso = 5;
      @(negedge clock_in);
      novaJogada_in = 1;
      #(clockPeriod);
      novaJogada_in = 0;
      // espera
      #(5*clockPeriod);

      // final dos casos de teste da simulacao
      caso = 99;
      #100;
      $display("Fim da simulacao");
      $stop;
    end

  endmodule