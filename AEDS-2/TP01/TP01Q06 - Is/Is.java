/*
   ==UserScript==
 @name         TP01Q06 - Is
 @namespace    https://github.com/Ddavidi/PUC-MINAS
 @description  VERDE PUC MINAS - TP01Q06 - Is
 @author       @ddavidi_
   ==/UserScript==
*/

import java.util.Scanner;

class Is{
    public static int tamanhoEntrada(String entrada){
        return entrada.length();
    }

    public static boolean isFim(String entrada){
        return entrada.charAt(0) == 'F' && entrada.charAt(1) == 'I' && entrada.charAt(2) == 'M';
    }

    public static boolean isInt(String entrada, int tam){
        boolean flag = true;

        for(int i=0;i<tam;i++){
            if(entrada.charAt(i)<'0' || entrada.charAt(i)>'9'){
                flag = false;
            }
        }

        return flag;
    }

    public static boolean isReal(String entrada, int tam){
        boolean flag = true;
        boolean temPonto = true;

        for(int i=0;i<tam;i++){
            if(entrada.charAt(i) == ','){
                temPonto = true;
            }
            else if(entrada.charAt(i)<'0' || entrada.charAt(i) > '9') {
                flag = false;
            }
        }

        return flag && temPonto;
    }

    public static boolean isConsoante(String entrada, int tam){
        boolean flag = true;
        
        for(int i=0;i<tam;i++){
            if((entrada.charAt(i) >= 'A' && entrada.charAt(i) <= 'Z') || (entrada.charAt(i) >= 'a' && entrada.charAt(i) <= 'z')){  
                if ((entrada.charAt(i) == 'A' || entrada.charAt(i) == 'E' || entrada.charAt(i) == 'I' || entrada.charAt(i) == 'O' || entrada.charAt(i) == 'U'
                || entrada.charAt(i) != 'a' || entrada.charAt(i) != 'e' || entrada.charAt(i) != 'i' || entrada.charAt(i) != 'o' || entrada.charAt(i) != 'u')  
                || (entrada.charAt(i) < 97 || entrada.charAt(i) > 122)) {    
                    flag = false;
            }
        }
            else {
                flag = false;
            }
        }

        return flag;
    }

    public static boolean isVogal(String entrada, int tam){
        boolean flag = true;

        for(int i=0;i<tam;i++){
            if (entrada.charAt(i) != 'A' || entrada.charAt(i) != 'E' || entrada.charAt(i) != 'I' || entrada.charAt(i) != 'O' || entrada.charAt(i) != 'U' 
            || entrada.charAt(i) != 'a' || entrada.charAt(i) != 'e' || entrada.charAt(i) != 'i' || entrada.charAt(i) != 'o' || entrada.charAt(i) != 'u') {
                flag = false;
            }
        }

        return flag;
    }

    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);

        String entrada = scan.nextLine();
        
        int tam = tamanhoEntrada(entrada);

        while(!isFim(entrada)){
            System.out.print(isVogal(entrada, tam) ? "SIM " : "NAO ");
            System.out.print(isConsoante(entrada, tam) ? "SIM " : "NAO ");
            System.out.print(isInt(entrada, tam) ? "SIM " : "NAO ");
            System.out.print(isReal(entrada, tam) ? "SIM\n" : "NAO\n");

            entrada = scan.nextLine();

            tam = tamanhoEntrada(entrada);
        }
    }
}