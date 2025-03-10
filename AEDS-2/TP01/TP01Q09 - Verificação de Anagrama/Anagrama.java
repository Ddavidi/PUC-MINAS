/*
   ==UserScript==
 @name         TP01Q09 - Verificação de Anagrama
 @namespace    https://github.com/Ddavidi/PUC-MINAS
 @description  VERDE PUC MINAS - TP01Q09 - Verificação de Anagrama
 @author       @ddavidi_
   ==/UserScript==
*/

import java.util.Scanner;

public class Anagrama {
    public static String to_lower_case(String string) {
        int string_size = string.length();
        char[] string_to_char_array = new char[string_size];
        for(int i = 0; i < string_size; i++) { string_to_char_array[i] = string.charAt(i); }

        for(int i = 0; i < string_size; i++) {
            char temp = string_to_char_array[i];

            switch(temp) {
                case 'A': string_to_char_array[i] = 'a'; break;
                case 'B': string_to_char_array[i] = 'b'; break;
                case 'C': string_to_char_array[i] = 'c'; break;
                case 'D': string_to_char_array[i] = 'd'; break;
                case 'E': string_to_char_array[i] = 'e'; break;
                case 'F': string_to_char_array[i] = 'f'; break;
                case 'G': string_to_char_array[i] = 'g'; break;
                case 'H': string_to_char_array[i] = 'h'; break;
                case 'I': string_to_char_array[i] = 'i'; break;
                case 'J': string_to_char_array[i] = 'j'; break;
                case 'K': string_to_char_array[i] = 'k'; break;
                case 'L': string_to_char_array[i] = 'l'; break;
                case 'M': string_to_char_array[i] = 'm'; break;
                case 'N': string_to_char_array[i] = 'n'; break;
                case 'O': string_to_char_array[i] = 'o'; break;
                case 'P': string_to_char_array[i] = 'p'; break;
                case 'Q': string_to_char_array[i] = 'q'; break;
                case 'R': string_to_char_array[i] = 'r'; break;
                case 'S': string_to_char_array[i] = 's'; break;
                case 'T': string_to_char_array[i] = 't'; break;
                case 'U': string_to_char_array[i] = 'u'; break;
                case 'V': string_to_char_array[i] = 'v'; break;
                case 'W': string_to_char_array[i] = 'w'; break;
                case 'X': string_to_char_array[i] = 'x'; break;
                case 'Y': string_to_char_array[i] = 'y'; break;
                case 'Z': string_to_char_array[i] = 'z'; break;
                default: break;
            }
        }

        return new String(string_to_char_array);
    }
    
    public static boolean anagram_checker(String s1, String s2) {
        if (s1.length() != s2.length()) return false;
        s1 = to_lower_case(s1);
        s2 = to_lower_case(s2);
    
        boolean[] used = new boolean[s2.length()];
        for (int i = 0; i < s2.length(); i++) {
            boolean found = false;
            for (int j = 0; j < s1.length(); j++) {
                if (!used[j] && s2.charAt(i) == s1.charAt(j)) {
                    used[j] = true;
                    found = true;
                    j = s1.length();
                }
            }
            if (!found) return false;
        }
        return true;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String first = "";
        boolean result;
        
        while(!first.equals("FIM")) {
            first = sc.next();
            if (!first.equals("FIM")) {
                sc.next(); 
                String second = sc.next();

                result = anagram_checker(first, second);
            System.out.println(result ? "SIM" : "N\u00C3O");
            }
        }

        sc.close();
    }
}