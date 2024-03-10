module contador_m #(parameter M=100, N=7)
  (
   input  wire          clock,
   input  wire          zera_s,
   input  wire          conta,
   input  wire          decresce,
   output reg  [N-1:0]  Q,
   output reg           fim
  );

  always @(posedge clock) begin
    if (clock) begin
      if (zera_s) begin
        Q <= 0;
      end else if (decresce) begin 
        if (Q >= M-1000) begin
          Q <= M-1;
        end else begin
          Q <= Q + 1000;
        end
      end else if (conta) begin
        if (Q == M-1) begin
          Q <= Q;
        end else begin
          Q <= Q + 1;
        end
      end
    end
  end

  // Saidas
  always @ (Q)
      if (Q == M-1)   fim = 1;
      else            fim = 0;

endmodule
