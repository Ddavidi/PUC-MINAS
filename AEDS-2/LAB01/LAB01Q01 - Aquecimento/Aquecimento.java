/*
   ==UserScript==
 @name         LAB01Q01 - Aquecimento
 @namespace    https://github.com/Ddavidi/PUC-MINAS
 @description  VERDE PUC MINAS - LAB01Q01 - Aquecimento
 @author       @ddavidi_
   ==/UserScript==
*/

import java.util.Scanner;

public class Aquecimento {
    public static boolean isFim(String entrada) {
        return entrada.equals("FIM");
    }

    public static int tamString(String entrada) {
        return entrada.length();
    }

    public static int retornaQntInteiro(String entrada) {
        int tam = tamString(entrada);
        int j = 0;

        for (int i = 0; i < tam; i++) {
            if (entrada.charAt(i) >= 'A' && entrada.charAt(i) <= 'Z') {
                j++;
            }
        }

        return j;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String entrada = scanner.nextLine();
        
        while (!isFim(entrada)) {
            int qntInteiro = retornaQntInteiro(entrada);
            System.out.println(qntInteiro);
            
            entrada = scanner.nextLine();
        }
        
        scanner.close();
    }
}