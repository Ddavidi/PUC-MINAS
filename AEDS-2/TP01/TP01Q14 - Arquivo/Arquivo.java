/*
   ==UserScript==
 @name         TP01Q14 - Arquivo
 @namespace    https://github.com/Ddavidi/VERDE-PUC-MINAS
 @description  VERDE PUC MINAS - TP01Q14 - Arquivo
 @author       @ddavidi_
   ==/UserScript==
*/

import java.io.File;
import java.io.IOException;
import java.io.PrintWriter;
import java.io.RandomAccessFile;
import java.util.Scanner;

public class Arquivo {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        try {
            PrintWriter arquivo = new PrintWriter(new File("pub.in"));

            int n = scan.nextInt();

            for(int i=0; i < n; i++) {
                double valor = scan.nextDouble();
                arquivo.printf("%f%n", valor);
            }

            arquivo.close();

            RandomAccessFile arquivoLeitura = new RandomAccessFile("pub.in", "r");

            long tamanhoArquivo = arquivoLeitura.length();
            long i = tamanhoArquivo;

            while (i > 0) {
                i--;
                arquivoLeitura.seek(i);
                              
                if (i == 0 || arquivoLeitura.readByte() == '\n') {
                    if (i != 0) arquivoLeitura.seek(i + 1); 
                    System.out.println(arquivoLeitura.readLine());
                }
            }

            arquivoLeitura.close();
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            scan.close();
        }    
    }
}