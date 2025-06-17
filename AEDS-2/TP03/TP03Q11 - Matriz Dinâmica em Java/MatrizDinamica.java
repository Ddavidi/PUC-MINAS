/*
   ==UserScript==
 @name         TP03Q11 - Matriz Dinâmica em Java
 @namespace    https://github.com/Ddavidi/PUC-MINAS
 @description  VERDE PUC MINAS - TP03Q11 - Matriz Dinâmica em Java
 @author       @ddavidi_
   ==/UserScript==
*/


import java.util.*;

class Celula {
    private int elem;
    public Celula inf, sup, prox, ant;

    public Celula() {
        elem = 0;
        inf = sup = prox = ant = null;
    }

    public Celula(int elem) {
        this.elem = elem;
        inf = sup = prox = ant = null;
    }

    public Celula(int elem, Celula inf, Celula sup, Celula prox, Celula ant) {
        this.elem = elem;
        this.inf = inf;
        this.sup = sup;
        this.prox = prox;
        this.ant = ant;
    }

    public int getElem() {
        return elem;
    }

    public void setElem(int elem) {
        this.elem = elem;
    }
}

class Matriz {
    private Celula primeiro;
    private int linha, coluna;

    public Matriz() {
        primeiro = null;
        linha = coluna = 0;
    }

    public Matriz(int linha, int coluna) {
        if (linha > 0 && coluna > 0) {
            this.linha = linha;
            this.coluna = coluna;
            iniciaMatriz();
        }
    }

    public int getColuna() {
        return coluna;
    }

    public int getLinha() {
        return linha;
    }

    public Celula getPrimeiro() {
        return primeiro;
    }

    public void iniciaMatriz() {
        Celula[][] tmp = new Celula[linha][coluna];
        for (int i = 0; i < linha; i++) {
            for (int j = 0; j < coluna; j++) {
                tmp[i][j] = new Celula();
            }
        }
        for(int i = 0; i < linha; i++){
            for(int j = 0; j < coluna; j++){
                if (i > 0) {
                    tmp[i][j].sup = tmp[i - 1][j];
                }
                if (i < linha - 1) {
                    tmp[i][j].inf = tmp[i + 1][j];
                }
                if (j > 0) {
                    tmp[i][j].ant = tmp[i][j - 1];
                }
                if (j < coluna - 1) {
                    tmp[i][j].prox = tmp[i][j + 1];
                }
            }
        }
        this.primeiro = tmp[0][0];
    }

    public Celula buscaCelula(int linha, int coluna) {
        Celula atual = primeiro;
        for (int i = 0; i < linha; i++) {
            atual = atual.inf;
        }
        for (int i = 0; i < coluna; i++) {
            atual = atual.prox;
        }
        return atual;
    }

    public void inserirElem(int elemento, int linha, int coluna) {
        if (linha >= 0 && linha < this.linha && coluna >= 0 && coluna < this.coluna) {
            Celula buscado = buscaCelula(linha, coluna);
            buscado.setElem(elemento);
        }

    }

    public int buscaValor(int linha, int coluna) {
        int buscado = -404;
        if (linha >= 0 && linha < this.linha && coluna >= 0 && coluna < this.coluna) {
            buscado = buscaCelula(linha, coluna).getElem();
        }
        return buscado;
    }

    public void imprimir(){
        for(int i = 0; i < linha; i++){
            for(int j = 0; j < coluna; j++){
                if(j > 0){
                    System.out.printf(" ");
                }
                System.out.print(buscaValor(i, j));
            }
            System.out.println(" ");
        }
    }

    private boolean saoIguais(Matriz b) {
        return (this.linha == b.getLinha() && this.coluna == b.getColuna());
    }

    public Matriz soma(Matriz somado) {
        Matriz resultado = new Matriz();
        if (saoIguais(somado)) {
            resultado = new Matriz(linha, coluna);
            for (int i = 0; i < linha; i++) {
                for (int j = 0; j < coluna; j++) {
                    int soma = buscaValor(i, j) + somado.buscaValor(i, j);
                    resultado.inserirElem(soma, i, j);
                }
            }
        }
        return resultado;
    }

    public Matriz multiplicacao(Matriz multiplicado){
        Matriz resultado = new Matriz();
        if(coluna == multiplicado.getLinha()){
            resultado = new Matriz(linha, coluna);
            for (int i = 0; i < linha; i++) {
                for (int j = 0; j < coluna; j++) {
                    int acumulador = 0;
                    for(int k = 0; k < coluna; k++){
                        acumulador += this.buscaValor(i, k) * multiplicado.buscaValor(k, j);
                    }
                    resultado.inserirElem(acumulador, i, j);
                }
            }
        }
        return resultado;
    }

    public void mostrarDiagonalPrincipal(){
        int tamDiagonal = Math.min(linha, coluna);
        for(int i = 0; i < tamDiagonal; i++){
            if(i > 0){
                System.out.printf(" ");
            }
            System.out.print(buscaValor(i, i));
        }
        System.out.println(" ");
    }

    public void mostrarDiagonalSecundaria(){
        int tamDiagonal = Math.min(linha, coluna);
        for(int i = 0; i < tamDiagonal; i++){
            int j = tamDiagonal - i - 1;
            if(i > 0){
                System.out.printf(" ");
            }
            System.out.print(buscaValor(i, j));
        }
        System.out.println(" ");
    }

}

public class MatrizDinamica {
    public static void main(String[] args){
        Scanner ler = new Scanner(System.in, "UTF-8");
        int n = Integer.parseInt(ler.nextLine());
        // Entrada e registro de dados
        for(int i = 0; i < n; i++){
            // Leitura da primeira Matriz
            int l1 = ler.nextInt();
            int c1 = ler.nextInt();
            Matriz primeira = new Matriz(l1, c1);
            for(int j = 0; j < l1; j++){
                for(int k = 0; k < c1; k++){
                    int valor = ler.nextInt();
                    primeira.inserirElem(valor, j, k);
                }
            }
            int l2 = ler.nextInt();
            int c2 = ler.nextInt();
            Matriz segunda = new Matriz(l2, c2);
            for(int j = 0; j < l2; j++){
                for(int k = 0; k < c2; k++){
                    int valor = ler.nextInt();
                    segunda.inserirElem(valor, j, k);
                }
            }
            primeira.mostrarDiagonalPrincipal();
            primeira.mostrarDiagonalSecundaria();
            Matriz soma = primeira.soma(segunda);
            soma.imprimir();
            Matriz multiplicacao = primeira.multiplicacao(segunda);
            multiplicacao.imprimir();
        }
        ler.close();
    }
}