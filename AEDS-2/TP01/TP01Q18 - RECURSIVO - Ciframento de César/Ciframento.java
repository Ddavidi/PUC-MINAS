/*
   ==UserScript==
 @name         TP01Q03 - Ciframento
 @namespace    https://github.com/Ddavidi/PUC-MINAS
 @description  VERDE PUC MINAS - TP01Q03 - Ciframento
 @author       @ddavidi_
   ==/UserScript==
*/

import java.util.Scanner;

public class Ciframento {
    public static String encrypt(String str, int index) {
        if (index == str.length()) {
            return ""; 
        }

        char currentChar = str.charAt(index);

        if (Character.isLetterOrDigit(currentChar) || Character.isWhitespace(currentChar) || isPrintable(currentChar)) {
            currentChar = (char) (currentChar + 3);
        }

        return currentChar + encrypt(str, index + 1); 
    }
    
    private static boolean isPrintable(char c) {
        return c >= 32 && c <= 126; 
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in, "UTF-8");
        String input = "";

        while (!input.equals("FIM")) {
            input = sc.nextLine();
            if (!input.equals("FIM")) { System.out.println(encrypt(input, 0)); }
        }

        sc.close();
    }
}
