/*
   ==UserScript==
 @name         TP01Q05 - Álgebra Booleana
 @namespace    https://github.com/Ddavidi/PUC-MINAS
 @description  VERDE PUC MINAS - TP01Q05 - Álgebra Booleana
 @author       @ddavidi_
   ==/UserScript==
*/

import java.util.*;

class Pilha{

    private int [] array; //array da pilha
    private int TAM_MAX; //tamanho maximo da pilha
    private int tam; //tamanho atual da pilha

    /**
     * Construtor sem parametros da pilha: seta o tamanho maximo da pilha como 50
     */
    public Pilha (){
        this(50);
    }

    /**
     * Construtor com parametros da pilha
     * @param tam - define o tamano maximo da pilha
     */
    public Pilha (int tam){
        this.TAM_MAX = tam;
        this.tam = 0;
        this.array = new int [TAM_MAX];
    }

    /**
     * Metodo get para o atributo tam da classe
     * @return - atributo tam
     */
    public int getTam(){
        return this.tam;
    }

    /**
     * Adiciona um numero ao topo da pilha
     * @param num - numero adicionado
     * @throws Exception - caso a pilha esteja cheia
     */
    public void push(int num) throws Exception{
        if (tam < TAM_MAX){
            tam++;
            array[tam - 1] = num;
        }else{
            throw new Exception("Erro no Pilha.push: Pilha Cheia!");
        }
    }

    /**
     * Retira o numero no topo da pilha 
     * @return - numero no topo da pilha
     * @throws Exception - caso a pilha estea vazia
     */
    public int pop() throws Exception{
        int resp = 0;
        if (tam > 0){
            resp = array[tam - 1];
            tam--;
        }else{
            throw new Exception("Erro no Pilha.pop: Pilha Vazia!");
        }
        return resp;
    }
    
    /**
     * Metodo que mostra o numero no topo da pilha sem retirá-lo
     * @return - o numero no topo da pilha
     * @throws Exception - caso a pilha esteja vazia
     */
    public int seeTop() throws Exception{
        int resp = 0;
        if (tam > 0){
            resp = array[tam - 1];
        }else{
            throw new Exception ("Erro no Pilha.seeTop: Pilha Vazia!");
        }
        return resp;
    }
}

public class AlgebraBooleana{
    public static void main (String [] args){
        Scanner scan = new Scanner(System.in);
        try{
            String stream = scan.nextLine();
            while (stream.charAt(0) != '0'){
                if (algebraBooleana(stream) == true){
                    System.out.println("1");        
                }
                else{
                    System.out.println("0");
                }
                stream = scan.nextLine();
            }
        }catch (Exception e){
            e.printStackTrace();
        } 
        finally{
            scan.close();
        }
    }

    /**
     * Metdodo que retorna um array de chars identico à String passada como paramentro
     * @param str - String para ser transformada
     * @return - array de chars correspondente
     */
    public static char [] myToCharArray (String str){
        char [] resp = new char [str.length()];
        for (int i = 0; i < resp.length; i++){
            resp[i] = str.charAt(i);
        }
        return resp;
    }

    /**
     * Metodo que retorna uma String a partir de um array de chars
     * @param str - array de chars a ser transformado
     * @return - objeto da clase String correspondente
     */
    public static String myToString (char [] array){
        String resp = "";
        for (int i = 0; i < array.length; i++){
            resp += array[i];
        }
        return resp;
    }

    /**
     * Metodo que recebe uma expressao booleana formatada de acrodo com o molde da questao, e retorna 1 para verdadeiro e 0 para falso
     * @param linha - expressao no formato de String
     * @return - 1 para verdadeiro, 0 para falso
     * @throws Exception - caso alguma das excecoes da Classe Pilha nao forem cumpridas
     */
    public static boolean algebraBooleana (String linha) throws Exception{
        boolean resp = false;
        Pilha operacoes = new Pilha();
        Pilha valores = new Pilha(100);
        char [] charArray = myToCharArray(linha);
        int numVariaveis = (int)charArray[0] - 48;
        int [] variaveis = new int [numVariaveis];
        int pos = 2;
        for (int j = 0; j < numVariaveis; j++){
            variaveis[j] = (int)charArray[pos] - 48;
            pos += 2;
        }
        while (pos < charArray.length){
            if (charArray[pos] == 'a'){
                operacoes.push(1);
                pos += 2;
            }
            else if (charArray[pos] == 'n'){
                operacoes.push(2);
                pos +=2;
            }
            else if (charArray[pos] == 'o'){
                operacoes.push(3);
                pos++;
            }
            else if (charArray[pos] == '('){
                valores.push(2);
            }
            else if ((int)charArray[pos] >= 65 && (int)charArray[pos] < 91){
                valores.push(variaveis[(int)charArray[pos] - 65]);
            }
            else if (charArray[pos] == ')'){
                int operacao = operacoes.pop();
                Pilha operacionandos = new Pilha (30);
                while (valores.getTam() > 0 && valores.seeTop() < 2){
                    operacionandos.push(valores.pop());
                }
                if (valores.getTam() > 0){
                    valores.pop();
                }
                if (operacao == 1){
                    while (operacionandos.getTam() > 1){
                        if (operacionandos.pop() * operacionandos.pop() == 1){
                            operacionandos.push(1);
                        }
                        else{
                            operacionandos.push(0);
                        }
                    }
                    valores.push(operacionandos.pop());
                }
                else if (operacao == 2){
                    while (operacionandos.getTam() > 0){
                        if (operacionandos.pop() == 0){
                            valores.push(1);
                        }
                        else {
                            valores.push(0);
                        }
                    }
                }
                else if (operacao == 3){
                    while (operacionandos.getTam() > 1){
                        if (operacionandos.pop() + operacionandos.pop() > 0){
                            operacionandos.push(1);
                        }
                        else {
                            operacionandos.push(0);
                        }
                    }
                    valores.push(operacionandos.pop());
                }
            }
            pos++;
        }
        if (valores.pop() == 1){
            resp = true;
        }
        else{
            resp = false;
        }
        return resp;
    }
}

