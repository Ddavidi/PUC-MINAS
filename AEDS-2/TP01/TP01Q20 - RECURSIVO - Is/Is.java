/*
   ==UserScript==
 @name         TP01Q20 - RECURSIVO - Is
 @namespace    https://github.com/Ddavidi/PUC-MINAS
 @description  VERDE PUC MINAS - TP01Q20 - RECURSIVO - Is
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

    public static boolean isInt(String entrada, int tam) {
        if (tam == 0) {
            return true;
        }

        char atual = entrada.charAt(tam - 1);
        if (atual < '0' || atual > '9') {
            return false;
        }

        return isInt(entrada, tam - 1);
    }

    public static boolean isReal(String entrada, int tam) {
        return isRealHelper(entrada, tam, false);
    }

    private static boolean isRealHelper(String entrada, int tam, boolean temPonto) {
        if (tam == 0) {
            return temPonto;
        }

        char atual = entrada.charAt(tam - 1);

        if (atual == ',') {
            if (temPonto) {
                return false;
            }
            return isRealHelper(entrada, tam - 1, true);
        }

        if (atual < '0' || atual > '9') {
            return false;
        }

        return isRealHelper(entrada, tam - 1, temPonto);
    }

    public static boolean isConsoante(String entrada, int tam) {
        if (tam == 0) {
            return true;
        }

        char atual = entrada.charAt(tam - 1);

        if ((atual >= 'A' && atual <= 'Z') || (atual >= 'a' && atual <= 'z')) {
            if (atual == 'A' || atual == 'E' || atual == 'I' || atual == 'O' || atual == 'U'
                    || atual == 'a' || atual == 'e' || atual == 'i' || atual == 'o' || atual == 'u') {
                return false;
            }
        }

        return isConsoante(entrada, tam - 1);
    }

    public static boolean isVogal(String entrada, int tam) {
        if (tam == 0) {
            return true;
        }

        char atual = entrada.charAt(tam - 1);

        boolean ehVogal = (atual == 'A' || atual == 'E' || atual == 'I' || atual == 'O' || atual == 'U'
                || atual == 'a' || atual == 'e' || atual == 'i' || atual == 'o' || atual == 'u');

        if (!ehVogal) {
            return false;
        }

        return isVogal(entrada, tam - 1);
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        String entrada = scan.nextLine();

        int tam = tamanhoEntrada(entrada);

        while (!isFim(entrada)) {
            System.out.print(isVogal(entrada, tam) ? "SIM " : "NAO ");
            System.out.print(isConsoante(entrada, tam) ? "SIM " : "NAO ");
            System.out.print(isInt(entrada, tam) ? "SIM " : "NAO ");
            System.out.print(isReal(entrada, tam) ? "SIM\n" : "NAO\n");

            entrada = scan.nextLine();

            tam = tamanhoEntrada(entrada);
        }
    }
}
