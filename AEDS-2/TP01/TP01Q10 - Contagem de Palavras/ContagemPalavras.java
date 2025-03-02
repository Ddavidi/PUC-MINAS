/*
   ==UserScript==
 @name         TP01Q10 - Contagem de Palavras
 @namespace    https://github.com/Ddavidi/PUC-MINAS
 @description  VERDE PUC MINAS - TP01Q10 - Contagem de Palavras
 @author       @ddavidi_
   ==/UserScript==
*/

import java.util.Scanner;

class ContagemPalavras {
    public static boolean isFim(String entrada){
        return entrada.charAt(0) == 'F' && entrada.charAt(1) == 'I' && entrada.charAt(2) == 'M';
    }

    public static int tamanhoEntrada(String entrada){
        return entrada.length();
    }

    public static int contadorDePalavras(String entrada){
        int tam = tamanhoEntrada(entrada);
        int numPalavras = 0;

        for(int i=0; i<tam; i++){
            if(entrada.charAt(i) == ' ')
                numPalavras++;
        }

        return ++numPalavras;
    }

    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);

        String entrada = scan.nextLine().trim();

        while(!isFim(entrada)){ 
            System.out.println(contadorDePalavras(entrada));
            entrada = scan.nextLine().trim();
        }
    }
}