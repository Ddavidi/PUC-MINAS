/*
   ==UserScript==
 @name         LABP2Q1 - Aquecimento em Java
 @namespace    https://github.com/Ddavidi/PUC-MINAS
 @description  VERDE PUC MINAS - LABP2Q1 - Aquecimento em Java
 @author       @ddavidi_
   ==/UserScript==
*/


import java.util.Scanner;

public class AquecimentoJava {

    public static class Pessoa {
        String nome;
        int peso;

        public Pessoa(String nome, int peso){
            this.nome = nome;
            this.peso = peso;
        }

        public static Pessoa ler(String linha){
            String[] linhaDividida = linha.split(" ");
            String nome = "";
            for(int i=0; i<linhaDividida.length-1;i++){
                nome += linhaDividida[i] + " ";
            }

            nome = nome.trim();

            int peso = Integer.parseInt(linhaDividida[linhaDividida.length-1]);

            return new Pessoa(nome, peso);
        }

        public static void ordenar(Pessoa[] atletas){
            int N = atletas.length;
            int maiorIndex;

            for(int i=0;i<N-1;i++){
                maiorIndex = i;
                for(int j=i+1; j<N;j++){
                    if(atletas[j].peso > atletas[maiorIndex].peso){
                        maiorIndex = j;
                    }

                    else if (atletas[j].peso == atletas[maiorIndex].peso) {
                        if(atletas[j].nome.compareTo(atletas[maiorIndex].nome) < 0){
                            maiorIndex = j;
                        }
                    }
                }

                swap(atletas, i, maiorIndex);
            }
        }

        public static void swap(Pessoa[] atletas, int i, int maiorIndex){
            Pessoa tmp = atletas[i];
            atletas[i] = atletas[maiorIndex];
            atletas[maiorIndex] = tmp;
        }

    }

    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);

        int N = scan.nextInt();
        scan.nextLine(); // quebra de linha pendente
        Pessoa[] atletas = new Pessoa[N];

        // cria preenchendo os atletas
        for(int i=0; i<N; i++){
            String linha = scan.nextLine();
            atletas[i] = Pessoa.ler(linha);
        }

        Pessoa.ordenar(atletas);

        for(int i=0; i<N; i++){
            System.out.println(atletas[i].nome + " " + atletas[i].peso);
        }

        scan.close();
    }
}