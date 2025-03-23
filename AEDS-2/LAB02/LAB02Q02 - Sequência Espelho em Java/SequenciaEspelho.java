/*
   ==UserScript==
 @name         LAB02Q02 - Sequência Espelho em Java
 @namespace    https://github.com/Ddavidi/PUC-MINAS
 @description  VERDE PUC MINAS - LAB02Q02 - Sequência Espelho em Java
 @author       @ddavidi_
   ==/UserScript==
*/

import java.util.Scanner;

public class SequenciaEspelho {
    public static int tamanhoEntrada(String entrada){
        return entrada.length();
    }

    public static void mostraInvertido(String entrada){
        int tam = tamanhoEntrada(entrada);

        for(int i=tam-1; i>=0; i--){
            System.out.print(entrada.charAt(i));
        }

        System.out.println();
    }

    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);

        while(scan.hasNext()){
            int intervalo1 = scan.nextInt();
            int intervalo2 = scan.nextInt();
            String sequenciaEspelho = "";

            for(int i=intervalo1; i<=intervalo2; i++){
                sequenciaEspelho += i;
            }

            System.out.print(sequenciaEspelho);
            
            mostraInvertido(sequenciaEspelho);
        }

        scan.close();
    }
}