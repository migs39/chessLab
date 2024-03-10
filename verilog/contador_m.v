module contador_m #(parameter M=100, N=7)
  (
   input  wire          clock,
   input  wire          zera_s,
   input  wire          conta,
   input  wire          decresce,
   input  wire          tempoDrec,
   output reg  [N-1:0]  Q,
   output reg           fim
  );

  always @(posedge clock) begin
    if (clock) begin
      if (zera_s) begin
        Q <= 0;
      end else if (decresce) begin
        if (Q >= M-tempoDrec) begin
          Q <= M-1;
        end else begin
          Q <= Q + tempoDrec;
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
