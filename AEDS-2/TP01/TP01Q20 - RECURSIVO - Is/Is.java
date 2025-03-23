/*
   ==UserScript==
 @name         TP01Q06 - Is
 @namespace    https://github.com/Ddavidi/PUC-MINAS
 @description  VERDE PUC MINAS - TP01Q06 - Is
 @author       @ddavidi_
   ==/UserScript==
*/

import java.util.Scanner;

class Is {
    public static int tamanhoEntrada(String entrada) {
        return entrada.length();
    }

    public static boolean isFim(String entrada) {
        return entrada.charAt(0) == 'F' && entrada.charAt(1) == 'I' && entrada.charAt(2) == 'M';
    }

    public static boolean isInt(String entrada, int tam, int pos) {
        if (pos >= tam) {
            return true;
        }
        if (entrada.charAt(pos) < '0' || entrada.charAt(pos) > '9') {
            return false;
        }
        return isInt(entrada, tam, pos + 1);
    }

    public static boolean isReal(String entrada, int tam, int pos, int countPonto) {
        if (pos >= tam) {
            return countPonto <= 1;
        }
        char c = entrada.charAt(pos);
        if ((c < '0' || c > '9') && (c != ',' && c != '.')) {
            return false;
        }
        if (c == '.' || c == ',') {
            return isReal(entrada, tam, pos + 1, countPonto + 1);
        }
        return isReal(entrada, tam, pos + 1, countPonto);
    }

    public static boolean isConsoante(String entrada, int tam, int pos) {
        if (pos >= tam) {
            return true;
        }
        char c = entrada.charAt(pos);
        if (!((c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z'))) {
            return false;
        }
        if (c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U' ||
            c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
            return false;
        }
        return isConsoante(entrada, tam, pos + 1);
    }

    public static boolean isVogal(String entrada, int tam, int pos) {
        if (pos >= tam) {
            return true;
        }
        char c = entrada.charAt(pos);
        if (!(c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U' || 
              c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u')) {
            return false;
        }
        return isVogal(entrada, tam, pos + 1);
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String entrada = scan.nextLine();
        int tam = tamanhoEntrada(entrada);

        while (!isFim(entrada)) {
            System.out.print(isVogal(entrada, tam, 0) ? "SIM " : "NAO ");
            System.out.print(isConsoante(entrada, tam, 0) ? "SIM " : "NAO ");
            System.out.print(isInt(entrada, tam, 0) ? "SIM " : "NAO ");
            System.out.print(isReal(entrada, tam, 0, 0) ? "SIM\n" : "NAO\n");

            entrada = scan.nextLine();
            tam = tamanhoEntrada(entrada);
        }

        scan.close();
    }
}