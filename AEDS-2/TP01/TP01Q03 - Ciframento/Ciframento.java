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
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = "";

        while (!input.equals("FIM")) {
            input = sc.nextLine();
            if (!input.equals("FIM")) {
                StringBuilder encryptedResult = new StringBuilder();

                for (int i = 0; i < input.length(); i++) {
                    encryptedResult.append((char) (input.charAt(i) + 3));
                }

                System.out.println(encryptedResult);
            }
        }

        sc.close();
    }
}
