/*
   ==UserScript==
 @name         TP01Q19 - RECURSIVO - Álgebra Booleana
 @namespace    https://github.com/Ddavidi/PUC-MINAS
 @description  VERDE PUC MINAS - TP01Q19 - RECURSIVO - Álgebra Booleana
 @author       @ddavidi_
   ==/UserScript==
*/

import java.util.*;

class Pilha {
    private int[] array;
    private int TAM_MAX;
    private int tam;

    public Pilha() {
        this(50);
    }

    public Pilha(int tam) {
        this.TAM_MAX = tam;
        this.tam = 0;
        this.array = new int[TAM_MAX];
    }

    public int getTam() {
        return this.tam;
    }

    public void push(int num) throws Exception {
        if (tam < TAM_MAX) {
            tam++;
            array[tam - 1] = num;
        } else {
            throw new Exception("Erro no Pilha.push: Pilha Cheia!");
        }
    }

    public int pop() throws Exception {
        int resp = 0;
        if (tam > 0) {
            resp = array[tam - 1];
            tam--;
        } else {
            throw new Exception("Erro no Pilha.pop: Pilha Vazia!");
        }
        return resp;
    }

    public int seeTop() throws Exception {
        int resp = 0;
        if (tam > 0) {
            resp = array[tam - 1];
        } else {
            throw new Exception("Erro no Pilha.seeTop: Pilha Vazia!");
        }
        return resp;
    }
}

public class AlgebraBooleana {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        try {
            String stream = scan.nextLine();
            while (stream.charAt(0) != '0') {
                if (algebraBooleana(stream)) {
                    System.out.println("1");
                } else {
                    System.out.println("0");
                }
                stream = scan.nextLine();
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            scan.close();
        }
    }

    public static char[] myToCharArray(String str) {
        char[] resp = new char[str.length()];
        for (int i = 0; i < resp.length; i++) {
            resp[i] = str.charAt(i);
        }
        return resp;
    }

    public static String myToString(char[] array) {
        String resp = "";
        for (int i = 0; i < array.length; i++) {
            resp += array[i];
        }
        return resp;
    }

    public static boolean algebraBooleana(String linha) throws Exception {
        char[] charArray = myToCharArray(linha);
        int numVariaveis = charArray[0] - '0';
        int[] variaveis = new int[numVariaveis];
        int pos = 2;
        for (int j = 0; j < numVariaveis; j++) {
            variaveis[j] = charArray[pos] - '0';
            pos += 2;
        }
        Pilha operacoes = new Pilha();
        Pilha valores = new Pilha(100);
        return avaliaExpressao(charArray, variaveis, pos, operacoes, valores);
    }

    private static boolean avaliaExpressao(char[] charArray, int[] variaveis, int pos, Pilha operacoes, Pilha valores) throws Exception {
        if (pos >= charArray.length) {
            return valores.pop() == 1;
        }

        if (charArray[pos] == 'a') { 
            operacoes.push(1);
            return avaliaExpressao(charArray, variaveis, pos + 3, operacoes, valores);
        } else if (charArray[pos] == 'n') { 
            operacoes.push(2);
            return avaliaExpressao(charArray, variaveis, pos + 3, operacoes, valores);
        } else if (charArray[pos] == 'o') { 
            operacoes.push(3);
            return avaliaExpressao(charArray, variaveis, pos + 2, operacoes, valores);
        } else if (charArray[pos] == '(') {
            valores.push(2); 
            return avaliaExpressao(charArray, variaveis, pos + 1, operacoes, valores);
        } else if (charArray[pos] >= 'A' && charArray[pos] <= 'Z') {
            valores.push(variaveis[charArray[pos] - 'A']);
            return avaliaExpressao(charArray, variaveis, pos + 1, operacoes, valores);
        } else if (charArray[pos] == ')') {
            int operacao = operacoes.pop();
            Pilha operandos = new Pilha(30);
            while (valores.getTam() > 0 && valores.seeTop() < 2) {
                operandos.push(valores.pop());
            }
            if (valores.getTam() > 0) {
                valores.pop(); 
            }
            if (operacao == 1) { 
                int resultado = 1;
                while (operandos.getTam() > 0) {
                    resultado *= operandos.pop();
                }
                valores.push(resultado);
            } else if (operacao == 2) { 
                int valor = operandos.pop();
                valores.push(valor == 0 ? 1 : 0);
            } else if (operacao == 3) {
                int resultado = 0;
                while (operandos.getTam() > 0) {
                    resultado = (operandos.pop() > 0 || resultado > 0) ? 1 : 0;
                }
                valores.push(resultado);
            }
            return avaliaExpressao(charArray, variaveis, pos + 1, operacoes, valores);
        }

        return avaliaExpressao(charArray, variaveis, pos + 1, operacoes, valores);
    }
}