/*
   ==UserScript==
 @name         TP02Q01 - Classe em Java
 @namespace    https://github.com/Ddavidi/PUC-MINAS
 @description  VERDE PUC MINAS - TP02Q01 - Classe em Java
 @author       @ddavidi_
   ==/UserScript==
*/

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;


class Principal {
    public static boolean isFim(String entrada){
        return entrada.charAt(0) == 'F' && entrada.charAt(1) == 'I' && entrada.charAt(2) == 'M';
    }

    public static void main (String[] args) throws FileNotFoundException{
        File file = new File("disneyplus2.csv");

        Scanner scanner = new Scanner(System.in);
        Scanner scan = new Scanner(file);

        Show shows[] = new Show[1369];
        int i = 0;

        if (scan.hasNext()) {
            scan.nextLine();
        }

        while (scan.hasNext()) {
            String linha = scan.nextLine();
            shows[i] = Show.ler(linha);
            i++;
        }

        /*for (int j = 0; j < i; j++) {
            shows[j].mostreShow(shows[j].getSHOW _ID());
        }*/

       // QUESTAO 01
       String entrada = scanner.nextLine();

        while(!isFim(entrada)){
            for (int j = 0; j < i; j++) {
                shows[j].mostreShow(entrada);
            }
            entrada = scanner.nextLine();
        }
    }
}