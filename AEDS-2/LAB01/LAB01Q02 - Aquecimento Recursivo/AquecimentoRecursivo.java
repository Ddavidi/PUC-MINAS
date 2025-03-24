/*
   ==UserScript==
 @name         LAB01Q02 - Aquecimento Recursivo
 @namespace    https://github.com/Ddavidi/PUC-MINAS
 @description  VERDE PUC MINAS - LAB01Q02 - Aquecimento Recursivo
 @author       @ddavidi_
   ==/UserScript==
*/

import java.util.Scanner;

public class AquecimentoRecursivo {
    public static boolean isFim(String entrada) {
        return entrada.equals("FIM");
    }

    public static int tamString(String entrada, int i) {
        if (i >= entrada.length()) {
            return 0;
        }
        return 1 + tamString(entrada, i + 1);
    }

    public static int retornaQntInteiro(String entrada, int i, int tam) {
        if (i >= tam) {
            return 0;
        }
        if (entrada.charAt(i) >= 'A' && entrada.charAt(i) <= 'Z') {
            return 1 + retornaQntInteiro(entrada, i + 1, tam);
        }
        return retornaQntInteiro(entrada, i + 1, tam);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String entrada = scanner.nextLine();
        
        while (!isFim(entrada)) {
            int tamanho = tamString(entrada, 0);
            int qntInteiro = retornaQntInteiro(entrada, 0, tamanho);
            System.out.println(qntInteiro);
            
            entrada = scanner.nextLine();
        }
        
        scanner.close();
    }
}