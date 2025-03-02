/*
   ==UserScript==
 @name         TP01Q03 - Ciframento
 @namespace    https://github.com/Ddavidi/PUC-MINAS
 @description  VERDE PUC MINAS - TP01Q03 - Ciframento
 @author       @ddavidi_
   ==/UserScript==
*/

import java.util.Scanner;

class ciframentoDeCesar {
    public static void cifrandoEntrada(String entrada){
        int tam = entrada.length();

        for(int i=0; i<tam; i++){
            int caracterCifrado = ((int) entrada.charAt(i)) + 3;
            System.out.print((char) caracterCifrado);
        }

        System.out.println();
    }

    public static boolean isFim(String entrada){
        return entrada.charAt(0) == 'F' && entrada.charAt(1) == 'I' && entrada.charAt(2) == 'M';
    }

    public static void main(String[] args){
        Scanner scan = new Scanner(System.in, "UTF-8");

        String entrada = scan.nextLine();

        while(!isFim(entrada)){
            cifrandoEntrada(entrada);
            entrada = scan.nextLine();
        }

        scan.close();
    }
}