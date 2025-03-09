/*
   ==UserScript==
 @name         TP01Q18 - RECURSIVO - Ciframento de César
 @namespace    https://github.com/Ddavidi/PUC-MINAS
 @description  VERDE PUC MINAS - TP01Q18 - RECURSIVO - Ciframento de César
 @author       @ddavidi_
   ==/UserScript==
*/

import java.util.Scanner;

class CiframentoDeCesar {
    public static void cifrandoEntrada(String entrada, int pos) {
        if (pos >= entrada.length()) {
            System.out.println();
            return;
        }
        int caracterCifrado = ((int) entrada.charAt(pos)) + 3;
        System.out.print((char) caracterCifrado);
        cifrandoEntrada(entrada, pos + 1);
    }

    public static void cifrandoEntrada(String entrada) {
        cifrandoEntrada(entrada, 0);
    }

    public static boolean isFim(String entrada) {
        return entrada.equals("FIM");
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String entrada = scan.nextLine();
        while (!isFim(entrada)) {
            cifrandoEntrada(entrada);
            entrada = scan.nextLine();
        }
        scan.close();
    }
}