/*
   ==UserScript==
 @name         TP01Q14 - Arquivo
 @namespace    https://github.com/Ddavidi/VERDE-PUC-MINAS
 @description  VERDE PUC MINAS - TP01Q14 - Arquivo
 @author       @ddavidi_
   ==/UserScript==
*/

import java.io.RandomAccessFile;
import java.util.Scanner;

class Arquivo{
    static Scanner sc = new Scanner(System.in);
    public static void main(String[] args) throws Exception{
        RandomAccessFile arquivo = new RandomAccessFile("fileName.txt", "rw");
        int n = Integer.parseInt(sc.nextLine());
        float input;
        for(int i = 0; i < n; i++){
            input = Float.parseFloat(sc.nextLine());
            arquivo.writeFloat(input);
        }
        float output;
        for(long i = n - 1; i >= 0; i--){
            arquivo.seek(i*Float.BYTES);
            output = arquivo.readFloat();
            if(output % 1 == 0){
                System.out.println((int)output);
            } else {
                System.out.println(output);
            }
        }
        arquivo.close();
    }
}
