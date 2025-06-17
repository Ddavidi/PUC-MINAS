/*
   ==UserScript==
 @name         TP03Q10 - Quicksort com LISTA DINÂMICA DUPLAMENTE ENCADEADA em Java
 @namespace    https://github.com/Ddavidi/PUC-MINAS
 @description  VERDE PUC MINAS - TP03Q10 - Quicksort com LISTA DINÂMICA DUPLAMENTE ENCADEADA em Java
 @author       @ddavidi_
   ==/UserScript==
*/

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class Quicksort3 {
    public static int comp = 0;
    public static int mov = 0;
    
    public static boolean isFim(String entrada) {
        return entrada.equals("FIM");
    }
    
    public static void ordenar(ListaDuplamenteEncadeada lista) {
        if (lista.tamanho <= 1) return;
        
        // Converter lista para array para facilitar o quicksort
        Shows[] array = listaParaArray(lista);
        quickSort(array, 0, array.length - 1);
        arrayParaLista(array, lista);
    }
    
    private static Shows[] listaParaArray(ListaDuplamenteEncadeada lista) {
        Shows[] array = new Shows[lista.tamanho];
        No atual = lista.primeiro.proximo;
        int i = 0;
        
        while (atual != lista.ultimo && i < array.length) {
            array[i] = atual.show;
            atual = atual.proximo;
            i++;
        }
        return array;
    }
    
    private static void arrayParaLista(Shows[] array, ListaDuplamenteEncadeada lista) {
        No atual = lista.primeiro.proximo;
        int i = 0;
        
        while (atual != lista.ultimo && i < array.length) {
            atual.show = array[i];
            atual = atual.proximo;
            i++;
        }
    }
    
    private static void quickSort(Shows[] array, int baixo, int alto) {
        if (baixo < alto) {
            int indicePivo = particionar(array, baixo, alto);
            quickSort(array, baixo, indicePivo - 1);
            quickSort(array, indicePivo + 1, alto);
        }
    }
    
    private static int particionar(Shows[] array, int baixo, int alto) {
        // Usar mediana de três para escolher o pivô
        int meio = baixo + (alto - baixo) / 2;
        medianaDeTres(array, baixo, meio, alto);
        
        Shows pivo = array[alto];
        int i = baixo - 1;
        
        for (int j = baixo; j < alto; j++) {
            comp++;
            
            // Comparar por data primeiro, depois por título
            int comparacaoData = array[j].getDate_added().compareTo(pivo.getDate_added());
            boolean menorQuePivo = false;
            
            if (comparacaoData < 0) {
                menorQuePivo = true;
            } else if (comparacaoData == 0) {
                comp++;
                if (array[j].getTitle().compareToIgnoreCase(pivo.getTitle()) < 0) {
                    menorQuePivo = true;
                }
            }
            
            if (menorQuePivo) {
                i++;
                trocar(array, i, j);
                mov += 3;
            }
        }
        
        trocar(array, i + 1, alto);
        mov += 3;
        return i + 1;
    }
    
    private static void medianaDeTres(Shows[] array, int a, int b, int c) {
        // Ordenar os três elementos para que o mediano fique no final
        if (compararShows(array[a], array[b]) > 0) {
            trocar(array, a, b);
            mov += 3;
        }
        if (compararShows(array[b], array[c]) > 0) {
            trocar(array, b, c);
            mov += 3;
        }
        if (compararShows(array[a], array[b]) > 0) {
            trocar(array, a, b);
            mov += 3;
        }
        // Colocar a mediana no final
        trocar(array, b, c);
        mov += 3;
    }
    
    private static int compararShows(Shows a, Shows b) {
        comp++;
        int comparacaoData = a.getDate_added().compareTo(b.getDate_added());
        if (comparacaoData == 0) {
            comp++;
            return a.getTitle().compareToIgnoreCase(b.getTitle());
        }
        return comparacaoData;
    }
    
    private static void trocar(Shows[] array, int i, int j) {
        if (i != j) {
            Shows temp = array[i];
            array[i] = array[j];
            array[j] = temp;
        }
    }
    
    public static Shows buscarShowPorId(String id) throws Exception {
        File file = new File("/tmp/disneyplus.csv");
        Scanner scan = new Scanner(file);
        Shows resultado = null;
        // Pular a primeira linha (cabeçalho)
        if (scan.hasNextLine()) {
            scan.nextLine();
        }
        while (scan.hasNextLine()) {
            String linha = scan.nextLine();
            Shows show = Shows.ler(linha);
            if (show != null && show.getShowid().equals(id) && resultado == null) {
                resultado = show;
            }
        }
    
        scan.close();
        return resultado;
    }
    
    public static void main(String[] args) throws Exception {
        Scanner scanner = new Scanner(System.in);
        ListaDuplamenteEncadeada lista = new ListaDuplamenteEncadeada();
        
        // Resetar contadores
        comp = 0;
        mov = 0;
        
        String entrada = scanner.nextLine();
        while (!isFim(entrada)) {
            Shows show = buscarShowPorId(entrada);
            if (show != null) {
                lista.inserir(show);
            }
            entrada = scanner.nextLine();
        }
        
        // Registrar tempo de início
        long tempoInicio = System.currentTimeMillis();
        
        // Ordena completamente a lista
        ordenar(lista);
        
        // Registrar tempo de fim
        long tempoFim = System.currentTimeMillis();
        long tempoExecucao = tempoFim - tempoInicio;
        
        // Criar arquivo de log
        criarArquivoLog(tempoExecucao);
        
        // Imprime todos os shows ordenados
        lista.imprimir();
        scanner.close();
    }
    
    public static void criarArquivoLog(long tempoExecucao) {
    
        try {
            FileWriter arq = new FileWriter("846072_sequencial.txt");
            arq.write("846072" + '\t' + comp + '\t' + mov + '\t' + tempoExecucao);
            arq.close();
        } catch (IOException e) {
            System.out.println(e.getMessage());
        }
    }
}

class No {
    Shows show;
    No anterior;
    No proximo;
    
    public No(Shows show) {
        this.show = show;
        this.anterior = null;
        this.proximo = null;
    }
}

class ListaDuplamenteEncadeada {
    No primeiro;
    No ultimo;
    int tamanho;
    
    public ListaDuplamenteEncadeada() {
        // Criar nós sentinela
        primeiro = new No(null);
        ultimo = new No(null);
        primeiro.proximo = ultimo;
        ultimo.anterior = primeiro;
        tamanho = 0;
    }
    
    public void inserir(Shows show) {
        No novoNo = new No(show);
        
        // Inserir antes do nó último
        novoNo.anterior = ultimo.anterior;
        novoNo.proximo = ultimo;
        ultimo.anterior.proximo = novoNo;
        ultimo.anterior = novoNo;
        
        tamanho++;
    }
    
    public void imprimir() {
        No atual = primeiro.proximo;
        while (atual != ultimo) {
            atual.show.imprimir();
            atual = atual.proximo;
        }
    }
    
    public boolean estaVazia() {
        return tamanho == 0;
    }
}

class Shows{
    private String show_id;
    private String type;
    private String title;
    private String director;
    private String[] cast;
    private String country;
    private Date date_added;
    private int release_year;
    private String rating;
    private String duration;
    private String[] listed_in;

    public Shows(){
        this.show_id = "";
        this.type = "";
        this.title = "";
        this.director = "";
        this.cast = new String[0];
        this.country = "";
        this.date_added = new Date();
        this.release_year = 0;
        this.rating = "";
        this.duration = "";
        this.listed_in = new String[0];
    }

    // Construtor com parâmetros
    public Shows(String show_id, String type, String title, String director, String[] cast,
                 String country, Date date_added, int release_year, String rating,
                 String duration, String[] listed_in) {
        this.show_id = show_id;
        this.type = type;
        this.title = title;
        this.director = director;
        this.cast = cast;
        this.country = country;
        this.date_added = date_added;
        this.release_year = release_year;
        this.rating = rating;
        this.duration = duration;
        this.listed_in = listed_in;
    }
    
    public String getShowid() {
        return show_id;
    }
    
    public void setShowid(String show_id) {
        this.show_id = show_id;
    }
    
    public String getType() {
        return type;
    }
    
    public void setType(String type) {
        this.type = type;
    }
    
    public String getTitle() {
        return title;
    }
    
    public void setTitle(String title) {
        this.title = title;
    }
    
    public String getDirector() {
        return director;
    }
    
    public void setDirector(String director) {
        this.director = director;
    }
    
    public String[] getCast() {
        return cast;
    }
    
    public void setCast(String[] cast) {
        this.cast = cast;
    }
    
    public String getCountry() {
        return country;
    }
    
    public void setCountry(String country) {
        this.country = country;
    }
    
    public Date getDate_added() {
        return date_added;
    }
    
    public void setDate_added(Date date_added) {
        this.date_added = date_added;
    }
    
    public int getRelease_year() {
        return release_year;
    }
    
    public void setRelease_year(int release_year) {
        this.release_year = release_year;
    }
    
    public String getRating() {
        return rating;
    }
    
    public void setRating(String rating) {
        this.rating = rating;
    }
    
    public String getDuration() {
        return duration;
    }
    
    public void setDuration(String duration) {
        this.duration = duration;
    }
    
    public String[] getListed_in() {
        return listed_in;
    }
    
    public void setListed_in(String[] listed_in) {
        this.listed_in = listed_in;
    }
    
    public Shows clone() {
        // Clonar arrays cast e listed_in
        String[] castClone = new String[this.cast.length];
        for (int i = 0; i < this.cast.length; i++) {
            castClone[i] = this.cast[i];
        }
        String[] listedInClone = new String[this.listed_in.length];
        for (int i = 0; i < this.listed_in.length; i++) {
            listedInClone[i] = this.listed_in[i];
        }
        // Clonar a data
        Date dateClone = this.date_added != null ? this.date_added.clone() : null;
        
        return new Shows(this.show_id, this.type, this.title, this.director, castClone, this.country,
            dateClone, this.release_year, this.rating, this.duration, listedInClone);
    }
    
    public static Shows ler(String linha) {
        String[] partes = new String[12];
        StringBuilder campo = new StringBuilder();
        int i = 0;
        int j = 0;
    
        while (i < linha.length() && j < 12) {
            if (linha.charAt(i) == '"') {
                i++; 
                while (i < linha.length()) {
                    if (i + 1 < linha.length() && linha.charAt(i) == '"' && linha.charAt(i + 1) == '"' ) {
                        i += 2; 
                    } else if (linha.charAt(i) == '"') {
                        i++; 
                        break;
                    } else {
                        campo.append(linha.charAt(i));
                        i++;
                    }
                }
                partes[j] = campo.toString();
                j++;
                campo.setLength(0);
                if (i < linha.length() && linha.charAt(i) == ',') {
                    i++; 
                }
            } else if (linha.charAt(i) == ',') {
                partes[j] = campo.length() == 0 ? "NaN" : campo.toString();
                j++;
                campo.setLength(0);
                i++;
            } else {
                campo.append(linha.charAt(i));
                i++;
            }
        }
    
        if (campo.length() > 0 && j < 12) {
            partes[j] = campo.toString();
            j++;
        } else if (j < 12) {
            partes[j] = "NaN";
        }
    
        while (j < 12) {
            partes[j] = "NaN";
            j++;
        }
    
        String show_id = partes[0];
        String type = partes[1];
        String title = partes[2];
        String director = partes[3];
        String[] cast = partes[4].equals("NaN") ? new String[0] : partes[4].split(",\\s*");
        String country = partes[5];
    
        //date_added for "NaN", atribuir "March 1, 1900"
        Date date_added;
        if (partes[6].equals("NaN")) {
            date_added = Date.parse("March 1, 1900");
        } else {
            date_added = Date.parse(partes[6]);
        }
    
        int release_year;
        try {
            release_year = Integer.parseInt(partes[7]);
        } catch (NumberFormatException e) {
            release_year = -1;
        }
    
        String rating = partes[8];
        String duration = partes[9];
        String[] listed_in = partes[10].equals("NaN") ? new String[0] : partes[10].split(",\\s*");
        
        return new Shows(show_id, type, title, director, cast, country, date_added,
                         release_year, rating, duration, listed_in);
    }
    
    public void imprimir() {
        String castStr = "[NaN]";
        if (cast != null && cast.length > 0) {
            // Bubble sort para ordenar o cast
            String[] castCopy = new String[cast.length];
            System.arraycopy(cast, 0, castCopy, 0, cast.length);
            
            for (int i = 0; i < castCopy.length - 1; i++) {
                for (int j = 0; j < castCopy.length - 1 - i; j++) {
                    if (castCopy[j].compareTo(castCopy[j + 1]) > 0) {
                        String temp = castCopy[j];
                        castCopy[j] = castCopy[j + 1];
                        castCopy[j + 1] = temp;
                    }
                }
            }
            castStr = "[";
            for (int i = 0; i < castCopy.length; i++) {
                castStr += castCopy[i];
                if (i < castCopy.length - 1) {
                    castStr += ", ";
                }
            }
            castStr += "]";
        }
    
        // Formata LISTED_IN manualmente
        String listedInStr = "[NaN]";
        if (listed_in != null && listed_in.length > 0) {
            listedInStr = "[";
            for (int i = 0; i < listed_in.length; i++) {
                listedInStr += listed_in[i];
                if (i < listed_in.length - 1) {
                    listedInStr += ", ";
                }
            }
            listedInStr += "]";
        }
        System.out.printf("=> %s ## %s ## %s ## %s ## %s ## %s ## %s ## %s ## %s ## %s ## %s ##\n",
                show_id != null ? show_id : "NaN",
                title != null ? title : "NaN",
                type != null ? type : "NaN",
                director != null ? director : "NaN",
                castStr,
                country != null ? country : "NaN",
                date_added,  
                release_year != -1 ? release_year : "NaN",
                rating != null ? rating : "NaN",
                duration != null ? duration : "NaN",
                listedInStr);
        }
    }

class Date{
    private String mes;
    private int dia;
    private int ano;

    public Date() {
        this.mes = "March";
        this.dia = 1;
        this.ano = 1900;
    }

    public Date(String mes, int dia, int ano) {
        this.mes = mes;
        this.dia = dia;
        this.ano = ano;
    }

    public static Date parse(String data) {
        if (data == null || data.equals("NaN")) {
            return new Date("March", 1, 1900);
        }

        // Exemplo de data: "September 9, 2021"
        String[] partes = data.split(" ");
        if (partes.length < 3) {
            return new Date("March", 1, 1900);
        }

        String mes = partes[0];
        int dia;
        int ano;
        try {
            dia = Integer.parseInt(partes[1].replace(",", ""));
            ano = Integer.parseInt(partes[2]);
        } catch (NumberFormatException e) {
            return new Date("March", 1, 1900);
        }

        return new Date(mes, dia, ano);
    }

    public String getMes() {
        return mes;
    }

    public void setMes(String mes) {
        this.mes = mes;
    }

    public int getDia() {
        return dia;
    }

    public void setDia(int dia) {
        this.dia = dia;
    }

    public int getAno() {
        return ano;
    }

    public void setAno(int ano) {
        this.ano = ano;
    }

    public Date clone() {
        return new Date(this.mes, this.dia, this.ano);
    }
    
    @Override
    public String toString() {
        return mes + " " + dia + ", " + ano;
    }
    
    public int compareTo(Date outraData) {
        if (outraData == null) return 1;
        
        // Comparar primeiro pelo ano
        if (this.ano != outraData.ano) {
            return this.ano - outraData.ano;
        }
        
        if (!this.mes.equals(outraData.mes)) {
            return converterMesParaNumero(this.mes) - converterMesParaNumero(outraData.mes);
        }
        return this.dia - outraData.dia;
    }
    
    private int converterMesParaNumero(String mes) {
        switch (mes.toLowerCase()) {
            case "january": return 1;
            case "february": return 2;
            case "march": return 3;
            case "april": return 4;
            case "may": return 5;
            case "june": return 6;
            case "july": return 7;
            case "august": return 8;
            case "september": return 9;
            case "october": return 10;
            case "november": return 11;
            case "december": return 12;
            default: return 0;
        }
    }
}