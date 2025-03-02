/*
   ==UserScript==
 @name         TP01Q08 - Soma de Dígitos
 @namespace    https://github.com/Ddavidi/PUC-MINAS
 @description  VERDE PUC MINAS - TP01Q08 - Soma de Dígitos
 @author       @ddavidi_
   ==/UserScript==
*/

import java.util.Scanner;

class SomaDigitos {
    public static boolean isFim(String entrada){
        return entrada.charAt(0) == 'F' && entrada.charAt(1) == 'I' && entrada.charAt(2) == 'M';
    }

    public static int tamanhoEntrada(String entrada){
        return entrada.length();
    }

    public static int somaDigitos(String entrada, int tam, int soma){
        if(tam < 0){
            return soma;
        }
        else{
            soma += Character.getNumericValue(entrada.charAt(tam));
            return somaDigitos(entrada, tam-1, soma);
        }
    }

    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);

        String entrada = scan.nextLine();
        int tam = tamanhoEntrada(entrada);
        
        while(!isFim(entrada)){     
            System.out.println(somaDigitos(entrada, tam-1, 0));
            entrada = scan.nextLine();
            tam = tamanhoEntrada(entrada);
        }
    }
}
