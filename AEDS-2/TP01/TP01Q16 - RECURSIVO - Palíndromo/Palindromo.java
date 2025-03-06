/*
   ==UserScript==
 @name         TP01Q16 - RECURSIVO - Palíndromo
 @namespace    https://github.com/Ddavidi/PUC-MINAS
 @description  VERDE PUC MINAS - TP01Q16 - RECURSIVO - Palíndromo
 @author       @ddavidi_
   ==/UserScript==
 */

import java.util.Scanner;

class Palindromo {
    public static boolean isPalindromo(String entrada, int inicio, int fim){
        if(inicio >= fim)
            return true;
        
        if(entrada.charAt(inicio)!=entrada.charAt(fim))
            return false;

        return isPalindromo(entrada, inicio+1, fim-1);
    }

    public static int tamanhoEntrada(String entrada){
        return entrada.length();
    }

    public static boolean isPalindromoAuxiliar(String entrada){
        int tamanhoEntrada = tamanhoEntrada(entrada);

        if(tamanhoEntrada == 0) return true;

        return isPalindromo(entrada, 0, tamanhoEntrada-1);
    }

    public static boolean isFim(String entrada){
        return entrada.charAt(0) == 'F' && entrada.charAt(1) == 'I' && entrada.charAt(2) == 'M';
    }

    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);

        String entrada = scan.nextLine();

        while(!isFim(entrada)){
            System.out.println(isPalindromoAuxiliar(entrada) ? "SIM" : "NAO"); 
            entrada = scan.nextLine();
        }
    }
}

