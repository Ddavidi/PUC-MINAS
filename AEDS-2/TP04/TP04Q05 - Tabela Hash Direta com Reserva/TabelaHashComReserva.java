/*
   ==UserScript==
 @name         TP04Q05 - Tabela Hash Direta com Reserva
 @namespace    https://github.com/Ddavidi/PUC-MINAS
 @description  VERDE PUC MINAS - TP04Q05 - Tabela Hash Direta com Reserva
 @author       @ddavidi_
   ==/UserScript==
*/

import java.io.File;
import java.util.Arrays;
import java.util.Scanner;

public class TabelaHashComReserva {
    public static void main(String[] args) {

        Show[] shows = Show.lerArquivo();
        Hash hash = new Hash();
        Scanner sc = new Scanner(System.in);
        String entrada = sc.nextLine();

        while (!entrada.equals("FIM")) {
            try {
                int index = Integer.parseInt(entrada.substring(1));
                if (index >= 0 && index < shows.length && shows[index] != null) {
                    hash.inserir(shows[index - 1].clone());
                } else {
                    System.out.println("Índice inválido ou show não encontrado.");
                }
            } catch (NumberFormatException e) {
                System.out.println("Erro: entrada inválida. Certifique-se de usar o formato correto (Xn).");
            } catch (StringIndexOutOfBoundsException e) {
                System.out.println("Erro: formato de entrada incorreto. Certifique-se de usar o formato correto (Xn).");
            } catch (NullPointerException e) {
                System.out.println("Erro: valor nulo encontrado.");
            }
            entrada = sc.nextLine();
        }

        entrada = sc.nextLine().trim();
        while(!entrada.equals("FIM")) {
            if (!entrada.isEmpty()) {
                System.out.printf(" (Posicao: %s) ", Hash.hash(entrada));
                boolean encontrado = hash.pesquisar(entrada);
                if (encontrado) {
                    System.out.println("SIM");
                }else {
                System.out.println("NAO");
                }
            }
            entrada = sc.nextLine().trim();
        }
        sc.close();
    }
}

class Show {
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
    private String description;

    public Show() {
        this.show_id = "NaN";
        this.type = "NaN";
        this.title = "NaN";
        this.director = "NaN";
        this.cast = new String[1];
        this.country = "NaN";
        this.date_added = new Date();
        this.release_year = 1900;
        this.rating = "NaN";
        this.duration = "NaN";
        this.listed_in = new String[1];
        this.description = "NaN";
    }

    public Show(String show_id, String type, String title, String director, String[] cast, String country,
                Date date_added, int release_year, String rating, String duration, String[] listed_in, String description) {
        this.show_id = show_id;
        this.type = type;
        this.title = title;
        this.director = director;
        this.cast = Arrays.copyOf(cast, cast.length);
        this.country = country;
        this.date_added = date_added;
        this.release_year = release_year;
        this.rating = rating;
        this.duration = duration;
        this.listed_in = Arrays.copyOf(listed_in, listed_in.length);
        this.description = description;
    }
    
    // Getters
    public String getShow_id() { return show_id; }
    public String getType() { return type; }
    public String getTitle() { return title; }
    public String getDirector() { return director; }
    public String[] getCast() { return cast; }
    public String getCountry() { return country; }
    public Date getDate_added() { return date_added; }
    public int getRelease_year() { return release_year; }
    public String getRating() { return rating; }
    public String getDuration() { return duration; }
    public String[] getListed_in() { return listed_in; }
    public String getDescription() { return description; }

    // Setters
    public void setShow_id(String show_id) { this.show_id = show_id; }
    public void setType(String type) { this.type = type; }
    public void setTitle(String title) { this.title = title; }
    public void setDirector(String director) { this.director = director; }
    public void setCast(String[] cast) { this.cast = Arrays.copyOf(cast, cast.length); }
    public void setCountry(String country) { this.country = country; }
    public void setDate_added(Date date_added) { this.date_added = date_added; }
    public void setRelease_year(int release_year) { this.release_year = release_year; }
    public void setRating(String rating) { this.rating = rating; }
    public void setDuration(String duration) { this.duration = duration; }
    public void setListed_in(String[] listed_in) { this.listed_in = Arrays.copyOf(listed_in, listed_in.length); }
    public void setDescription(String description) { this.description = description; }

    // Clone
    public Show clone(){
        Show novo = new Show();
        novo.setShow_id(this.show_id);
        novo.setType(this.type);
        novo.setTitle(this.title);
        novo.setDirector(this.director);
        novo.setCast(this.cast);
        novo.setCountry(this.country);
        novo.setDate_added(this.date_added);
        novo.setRelease_year(this.release_year);
        novo.setRating(this.rating);
        novo.setDuration(this.duration);
        novo.setListed_in(this.listed_in);
        novo.setDescription(this.description);
        return novo;
    }

    public static Show[] lerArquivo() {
        Show[] lista = new Show[1370];
        int index = 0;
        File arquivo = new File("/tmp/disneyplus.csv");

        try (Scanner sc = new Scanner(arquivo)) {
            sc.nextLine(); // pula o cabeçalho do arquivo CSV
            while (sc.hasNextLine()) {
                String linha = sc.nextLine();
                lista[index] = new Show();
                lista[index++].ler(linha);
            }
        } catch (java.io.FileNotFoundException e) {
            System.out.println("Erro: arquivo não encontrado: " + e.getMessage());
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Erro: linha com número incorreto de colunas no arquivo.");
        }
        return lista;
    }

    public void ler(String linha) {
        try {
            String[] partes = linha.split(",(?=([^\"]*\"[^\"]*\")*[^\"]*$)", -1);
            this.show_id = partes[0].trim().isEmpty() ? "NaN" : partes[0].trim();
            this.type = partes[1].trim().isEmpty() ? "NaN" : partes[1].replace("\"", "").trim();
            this.title = partes[2].trim().isEmpty() ? "NaN" : partes[2].replace("\"", "").trim();
            this.director = partes[3].trim().isEmpty() ? "NaN" : partes[3].replace("\"", "").trim();
            this.cast = partes[4].trim().isEmpty() ? new String[]{"NaN"} : separarString(partes[4]);
            ordenarCast(this.cast);
            this.country = partes[5].trim().isEmpty() ? "NaN" : partes[5].replace("\"", "").trim();
            this.date_added = Date.parseData(partes[6].trim());
            this.release_year = partes[7].trim().isEmpty() ? 1900 : Integer.parseInt(partes[7].trim());
            this.rating = partes[8].trim().isEmpty() ? "NaN" : partes[8].trim();
            this.duration = partes[9].trim().isEmpty() ? "NaN" : partes[9].trim();
            this.listed_in = partes[10].trim().isEmpty() ? new String[]{"NaN"} : separarString(partes[10]);
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Erro: linha com número incorreto de colunas: " + linha);
        } catch (NumberFormatException e) {
            System.out.println("Erro: formato de número inválido na linha: " + linha);
        }
    }

    private String[] separarString(String str) {
        String[] partes = str.replace("\"", "").split(", ");
        for (int i = 0; i < partes.length; i++) {
            partes[i] = partes[i].trim();
        }
        return partes;
    }

    public void imprimir() {
        System.out.printf("=> %s ## %s ## %s ## %s ## [", show_id, title, type, director);

        for (int i = 0; i < cast.length; i++) {
            System.out.printf("%s", cast[i]);
            if (i < cast.length - 1) System.out.printf(", ");
        }

        System.out.printf("] ## %s ## %s ## %d ## %s ## %s ## [", country, date_added.toString(), release_year, rating, duration);

        for (int i = 0; i < listed_in.length; i++) {
            System.out.printf("%s", listed_in[i]);
            if (i < listed_in.length - 1) System.out.printf(", ");
        }

        System.out.printf("] ##\n");
    }

    public static void swap(String [] cast, int i, int j) {
        String aux = cast[i];
        cast[i] = cast[j];
        cast[j] = aux;
    }

    public static void ordenarCast(String[] cast) {
        for(int i = 0; i < cast.length; i++){
            int menor  = i;
            for(int j = i + 1; j < cast.length; j++){
                if(cast[menor].compareTo(cast[j]) > 0){
                    menor = j;
                }
            }
            if(menor != i){
                swap(cast, i, menor);
            }
        }
    }
}

class Date {
    private String month;
    private int day;
    private int year;

    public Date() {
        this("March", 1, 1900);
    }

    public Date(String month, int day, int year) {
        this.month = month;
        this.day = day;
        this.year = year;
    }

    public void setMonth(String month) { this.month = month; }
    public void setDay(int day) { this.day = day; }
    public void setYear(int year) { this.year = year; }

    public String getMonth() { return month; }
    public int getDay() { return day; }
    public int getYear() { return year; }

    public static Date parseData(String dataTexto) {
        if (dataTexto == null || dataTexto.trim().isEmpty() || dataTexto.equals("NaN")) {
            return new Date();
        }

        try {
            // Remove aspas, se existirem, e divide a string
            dataTexto = dataTexto.replace("\"", "").trim();
            String[] partes = dataTexto.split(" ");

            if (partes.length == 3) {
                String month = partes[0].trim();
                int day = Integer.parseInt(partes[1].replace(",", "").trim());
                int year = Integer.parseInt(partes[2].trim());
                return new Date(month, day, year);
            } else {
                throw new IllegalArgumentException("Formato de data inválido: " + dataTexto);
            }
        } catch (NumberFormatException e) {
            System.out.println("Erro ao processar data: " + dataTexto);
            return new Date(); // Retorna uma data padrão em caso de erro
        } catch (IllegalArgumentException e) {
            System.out.println("Erro ao processar data: " + dataTexto);
            return new Date(); // Retorna uma data padrão em caso de erro
        }
    }

    @Override
    public String toString() {
        return String.format("%s %d, %04d", month, day, year);
    }
}

class Hash{
    public Show array[];
    private static final int TAM = 21;
    private static final int TAMR = 9;
    private int res;

    public Hash() {
        this.array = new Show[TAM + TAMR];
        this.res = 0;
    }

    public static int hash(String titulo) {
        return toInteger(titulo) % TAM;
    }

    private static int toInteger(String titulo) {
        int soma = 0;
        for (char c : titulo.toCharArray()) {
            soma += (int) c;
        }
        return soma;
    }

    public void inserir(Show show) {
        int posicao = hash(show.getTitle());
        if(array[posicao] == null) {
            array[posicao] = show;
            res++;
        }
        else if(array[posicao] != show) {
            inserirReserva(show);
        }
    }

    private void inserirReserva(Show show) {
        for(int i = TAM; i < TAM + TAMR; i++) {
            if(array[i] == null) {
                array[i] = show;
                res++;
                i = TAM + TAMR;
            }
        }
    }

    public boolean pesquisar(String titulo) {
        int posicao = hash(titulo);
        boolean resp;
        if (array[posicao] == null) {
            resp = false;
        }
        else if (array[posicao].getTitle().equals(titulo)) {
            resp = true;
        }
        else {
            resp = pesquisarReserva(titulo);
        }
        return resp;
    }

    private boolean pesquisarReserva(String titulo) {
        boolean resp = false;
        for (int i = TAM + 1; i < TAM + TAMR; i++) {
            if (array[i] != null) {
                if (array[i].getTitle().equals(titulo)) {
                    resp = true;
                    i = TAM + TAMR;
                }
            }else {
                i = TAM + TAMR;
            }
        }
        return resp;
    }
}