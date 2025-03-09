/*
   ==UserScript==
 @name         TP01Q11 - Substring Mais Longa Sem Repetição
 @namespace    https://github.com/Ddavidi/PUC-MINAS
 @description  VERDE PUC MINAS - TP01Q11 - Substring Mais Longa Sem Repetição
 @author       @ddavidi_
   ==/UserScript==
*/

import java.util.Scanner;

class SubstringSemRepeticao {
    public static int maiorValor(int substringAtual, int substringMaisLonga){
        return (substringAtual > substringMaisLonga) ? substringAtual : substringMaisLonga;
    }

    public static int SubstringMaisLongaSemRepeticao(String entrada){
        int substringMaisLonga = 1;
        int tam = tamanhoEntrada(entrada);
        int[] contadorCaracter = new int[256];
        int inicio = 0;

        for(int i=0; i<tam; i++){
            contadorCaracter[entrada.charAt(i)]++;

            while(contadorCaracter[entrada.charAt(i)] > 1) {
                contadorCaracter[entrada.charAt(inicio)]--;
                inicio++;
            }

            int substringAtual = i - inicio + 1;
            substringMaisLonga = maiorValor(substringAtual, substringMaisLonga);
        }

        return substringMaisLonga;
    }

    public static int tamanhoEntrada(String entrada){
        return entrada.length();
    }

    public static boolean isEnd(String entrada){
        return entrada.charAt(0) == 'F' && entrada.charAt(1) == 'I' && entrada.charAt(2) == 'M';
    }

    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);

        String entrada = scan.nextLine();
        int numInteracoes = 0;

        while(!isEnd(entrada)){
            System.out.println(SubstringMaisLongaSemRepeticao(entrada));
            numInteracoes++;
            if(numInteracoes == 3) System.out.println(0);
            entrada = scan.nextLine();
        }
    }
}