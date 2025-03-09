/*
   ==UserScript==
 @name         TP01Q07 - Inversão de Strings
 @namespace    https://github.com/Ddavidi/PUC-MINAS
 @description  VERDE PUC MINAS - TP01Q07 - Inversão de Strings
 @author       @ddavidi_
   ==/UserScript==
*/

import java.util.Scanner;

class InversaoString {
    public static int tamanhoEntrada(String entrada){
        return entrada.length();
    }

    public static void inversaoString(String entrada){
        int tam = tamanhoEntrada(entrada);

        for(int i=tam-1; i>=0; i--){
            System.out.print(entrada.charAt(i));
        }
        
        System.out.println();
    }
    
    public static boolean isEnd(String entrada){ 
        return entrada.charAt(0) == 'F' && entrada.charAt(1) == 'I' && entrada.charAt(2) == 'M';
    }

    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);

        String entrada = scan.nextLine();

        while(!isEnd(entrada)){
            inversaoString(entrada);
            entrada = scan.nextLine();
        }
    }
}