/*
   ==UserScript==
 @name         TP01Q12 - Validação de Senhas
 @namespace    https://github.com/Ddavidi/PUC-MINAS
 @description  VERDE PUC MINAS - TP01Q12 - Validação de Senhas
 @author       @ddavidi_
   ==/UserScript==
*/

import java.util.Scanner;

class ValidacaoSenhas {
    public static boolean senhaValida(String entrada){
        int tam = tamanhoEntrada(entrada);
        Boolean maiuscula = false, 
                minuscula = false,
                numero = false,
                caracterEspecial = false;

        for(int i=0; i<tam; i++){
            if(entrada.charAt(i) >= 'A' && entrada.charAt(i) <= 'Z') maiuscula = true;
            else if(entrada.charAt(i) >= 'a' && entrada.charAt(i) <= 'z') minuscula = true;
            else if(entrada.charAt(i) >= '0' && entrada.charAt(i) <= '9') numero = true;
            else caracterEspecial = true;
        }

        return maiuscula && minuscula && numero && caracterEspecial;
    }

    public static boolean isEnd(String entrada) {
        return entrada.charAt(0) == 'F' && entrada.charAt(1) == 'I' && entrada.charAt(2) == 'M';
    }

    public static int tamanhoEntrada(String entrada){
        return entrada.length();
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        
        String entrada = scan.nextLine();
        
        while(!isEnd(entrada)){
            System.out.println(senhaValida(entrada) ? "SIM" : "N\u00C3O");
            entrada = scan.nextLine();
        }
    }
}