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
    public static boolean saoAnagramas(String str1, String str2) {
        if (str1.length() != str2.length()) {
            return false;
        }
        
        int[] contagem = new int[65536];
        
        for (char c : str1.toCharArray()) {
            contagem[c]++;
        }
        
        for (char c : str2.toCharArray()) {
            contagem[c]--;
        }
        
        for (int i = 0; i < 65536; i++) {
            if (contagem[i] != 0) {
                return false;
            }
        }
        
        return true;
    }
    
    public static boolean isEnd(String entrada) {
        return entrada.equals("FIM");
    }
    
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in, "UTF-8");
        
        String linha = scan.nextLine();
        
        while (!isEnd(linha)) {
            String[] partes = linha.split(" - ");
            String str1 = partes[0];
            String str2 = partes[1];
            System.out.println(saoAnagramas(str1, str2) ? "SIM" : "NÃO");
            linha = scan.nextLine();
        }
        
        scan.close();
    }
}