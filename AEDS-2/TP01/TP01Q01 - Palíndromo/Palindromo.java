/*
   ==UserScript==
 @name         TP01Q01 - Palindromo
 @namespace    https://github.com/Ddavidi/PUC-MINAS
 @description  VERDE PUC MINAS - TP01Q01 - Palindromo
 @author       @ddavidi_
   ==/UserScript==
*/

import java.util.Scanner;

class Palindromo {
    public static boolean isFim(String entrada){
        return entrada.charAt(0) == 'F' && entrada.charAt(1) == 'I' && entrada.charAt(2) == 'M';
    }

    public static int tamanhoEntrada(String entrada){
        return entrada.length();
    }

    public static boolean isPalindromo(String entrada){
        int tam = tamanhoEntrada(entrada);
        boolean flag = true;

        for(int i=0; i<tam/2; i++){
            if(entrada.charAt(i) != entrada.charAt(tam - 1 - i)){
                flag = false;
                i = tam/2;
            }
        }

        return flag;
    }

    public static void main (String[] args) {
        Scanner scan = new Scanner(System.in);

        String entrada = scan.nextLine();

        while(!isFim(entrada)){
            System.out.println(isPalindromo(entrada) ? "SIM" : "NAO");
            entrada = scan.nextLine();
        }
    }
}