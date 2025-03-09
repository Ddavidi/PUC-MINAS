/*
   ==UserScript==
 @name         TP01Q04 - Alteração Aleatória
 @namespace    https://github.com/Ddavidi/PUC-MINAS
 @description  VERDE PUC MINAS - TP01Q04 - Alteração Aleatória
 @author       @ddavidi_
   ==/UserScript==
*/

import java.util.Random;
import java.util.Scanner;

class AlteracaoAleatoria {
    public static int tamEntrada(String entrada){
        return entrada.length();
    }

    public static void alteracaoAleatoria(String entrada, Random gerador){
        char primeiraMinusculaAleatoria = (char)('a' + (Math.abs(gerador.nextInt()) % 26));
        char segundaMinusculaAleatoria = (char)('a' + (Math.abs(gerador.nextInt()) % 26));
        int tam = tamEntrada(entrada);

        for(int i = 0; i<tam; i++){
            if(entrada.charAt(i) == primeiraMinusculaAleatoria){
                System.out.print(segundaMinusculaAleatoria);
            }
            else{
                System.out.print(entrada.charAt(i));
            }
        } 

        System.out.println();
    }

    public static boolean isEnd(String entrada){
        return entrada.charAt(0) == 'F' && entrada.charAt(1) == 'I' && entrada.charAt(2) == 'M';
    }

    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        Random gerador = new Random();
        gerador.setSeed(4);

        String entrada = scan.nextLine();

        while(!isEnd(entrada)){
            alteracaoAleatoria(entrada, gerador);
            entrada = scan.nextLine();
        }
    }
}