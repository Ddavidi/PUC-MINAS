/*
   ==UserScript==
 @name         TP01Q13 - Leitura de Página HTML
 @namespace    https://github.com/Ddavidi/VERDE-PUC-MINAS
 @description  VERDE PUC MINAS - TP01Q13 - Leitura de Página HTML
 @author       @ddavidi_
   ==/UserScript==
*/

import java.io.*;
import java.net.*;
import java.nio.charset.StandardCharsets;
import java.util.*;

public class HTML {

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        String pageName = sc.nextLine();
        while (!pageName.equals("FIM")) {
            String url = sc.nextLine();
            String content = getHTMLContent(url);
            int[] counts = countOccurrences(content);
            System.out.printf("a(%d) e(%d) i(%d) o(%d) u(%d) \u00e1(%d) \u00e9(%d) \u00ed(%d) \u00f3(%d) \u00fa(%d) \u00e0(%d) \u00e8(%d) \u00ec(%d) \u00f2(%d) \u00f9(%d) \u00e3(%d) \u00f5(%d) \u00e2(%d) \u00ea(%d) \u00ee(%d) \u00f4(%d) \u00fb(%d) consoante(%d) <br>(%d) <table>(%d) %s\n",
                    counts[0] - 1, counts[1] - 1, counts[2], counts[3], counts[4],
                    counts[5], counts[6], counts[7], counts[8], counts[9],
                    counts[10], counts[11], counts[12], counts[13], counts[14],
                    counts[15], counts[16], counts[17], counts[18], counts[19],
                    counts[20], counts[21], counts[22] - 3, counts[23], counts[24], pageName);
            pageName = sc.nextLine();
        }

        sc.close();
    }

    private static String getHTMLContent(String urlString) throws IOException {
        StringBuilder content = new StringBuilder();
        URL url = new URL(urlString);
        
        try (BufferedReader in = new BufferedReader(new InputStreamReader(url.openStream(), StandardCharsets.UTF_8))) {
            String inputLine;
            while ((inputLine = in.readLine()) != null) {
                content.append(inputLine).append("\n");
            }
        }
        return content.toString();
    }

    private static int[] countOccurrences(String content) {
        int[] counts = new int[26];
        String[] patterns = {"<br>", "<table>"};
        String[] accentedVowels = {"\u00e1", "\u00e9", "\u00ed", "\u00f3", "\u00fa", "\u00e0", "\u00e8", "\u00ec", "\u00f2", "\u00f9", "\u00e3", "\u00f5", "\u00e2", "\u00ea", "\u00ce", "\u00f4", "\u00fb"};
        
        // Contagem de caracteres
        for (char c : content.toCharArray()) {
            switch (c) {
                case 'a': counts[0]++; break;
                case 'e': counts[1]++; break;
                case 'i': counts[2]++; break;
                case 'o': counts[3]++; break;
                case 'u': counts[4]++; break;
                case 'b': case 'c': case 'd': case 'f': case 'g': case 'h': case 'j': case 'k': case 'l': case 'm': case 'n':
                case 'p': case 'q': case 'r': case 's': case 't': case 'v': case 'w': case 'x': case 'y': case 'z':
                    counts[22]++; break;
            }
        }

        for (String vowel : accentedVowels) {
            counts[5 + Arrays.asList(accentedVowels).indexOf(vowel)] = countPattern(content, vowel);
        }

        counts[23] = countPattern(content, "<br>");
        counts[24] = countPattern(content, "<table>");
        
        return counts;
    }

    private static int countPattern(String content, String pattern) {
        int count = 0;
        int index = 0;
        while ((index = content.indexOf(pattern, index)) != -1) {
            count++;
            index += pattern.length();
        }

        return count;
    }
}