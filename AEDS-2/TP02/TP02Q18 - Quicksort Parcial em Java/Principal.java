/*
   ==UserScript==
 @name         TP02Q18 - Quicksort Parcial em Java
 @namespace    https://github.com/Ddavidi/PUC-MINAS
 @description  VERDE PUC MINAS - TP02Q18 - Quicksort Parcial em Java
 @author       @ddavidi_
   ==/UserScript==
*/

import java.io.File;
import java.util.Arrays;
import java.util.Scanner;

public class Principal {
    public static void main(String[] args) {
        Show[] lista = Show.lerArquivo();
        Scanner sc = new Scanner(System.in);
        String entrada = sc.nextLine();
        Show[] arrayShows = new Show[1370];
        int i = 0;

        while (!entrada.equals("FIM")) {
            try {
                int index = Integer.parseInt(entrada.substring(1));
                if (index >= 0 && index < lista.length && lista[index] != null) {
                    try {
                        arrayShows[i++] = lista[index - 1].clone();
                    } catch (CloneNotSupportedException e) {
                        System.out.println("Erro ao clonar o objeto Show: " + e.getMessage());
                    }
                } else {
                    System.out.println("Índice inválido ou show não encontrado.");
                }
            } catch (NumberFormatException e) {
                System.out.println("Erro: entrada inválida. Certifique-se de usar o formato correto (Xn).");
            } catch (ArrayIndexOutOfBoundsException | NullPointerException e) {
                System.out.println("Erro inesperado: " + e.getMessage());
            }
            entrada = sc.nextLine();
        }

        Show.quickSort(arrayShows, i);
        int limit = Math.min(i, 10);
        for (int j = 0; j < limit; j++) {
            if (arrayShows[j] != null) {
                arrayShows[j].imprimir();
            }
        }

        sc.close();
    }
}

class Show implements Cloneable {
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
    @Override
    public Show clone() throws CloneNotSupportedException {
        return (Show) super.clone();
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
        } catch (Exception e) {
            System.out.println("Erro ao ler o arquivo: " + e.getMessage());
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
        } catch (NumberFormatException | ArrayIndexOutOfBoundsException | NullPointerException e) {
            System.out.println("Erro ao processar linha: " + linha + " - " + e.getMessage());
        }
    }

    private String[] separarString(String str) {
        String[] partes = str.replace("\"", "").split(", ");
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

    public static void quickSort(Show[] array, int n) {
        quickSort(array, 0, n - 1);
    }

    private static void quickSort(Show[] array, int left, int right) {
        if (left < right) {
            int pivotIndex = partition(array, left, right);
            quickSort(array, left, pivotIndex - 1);
            quickSort(array, pivotIndex + 1, right);
        }
    }

    private static int partition(Show[] array, int left, int right) {
        Show pivot = array[right];
        int i = left - 1;

        for (int j = left; j < right; j++) {
            if (compare(array[j], pivot) <= 0) {
                i++;
                swap(array, i, j);
            }
        }

        swap(array, i + 1, right);
        return i + 1;
    }

    private static int compare(Show a, Show b) {
        if (a == null || b == null) return 0;

        int cmpDate = compareDate(a.getDate_added(), b.getDate_added());
        if (cmpDate != 0) return cmpDate;

        return a.getTitle().compareTo(b.getTitle());
    }

    private static int compareDate(Date d1, Date d2) {
        if (d1.getYear() != d2.getYear()) return d1.getYear() - d2.getYear();
        if (d1.getMonth().equals(d2.getMonth()) == false) return getMonthNumber(d1.getMonth()) - getMonthNumber(d2.getMonth());
        return d1.getDay() - d2.getDay();
    }

    private static int getMonthNumber(String month) {
        switch (month.toLowerCase()) {
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
            default: return 0; // Se for "NaN" ou inválido
        }
    }

    private static void swap(Show[] array, int i, int j) {
        Show temp = array[i];
        array[i] = array[j];
        array[j] = temp;
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
            System.out.println("Erro ao processar data (NumberFormatException): " + dataTexto);
            return new Date(); // Retorna uma data padrão em caso de erro
        } catch (IllegalArgumentException e) {
            System.out.println("Erro ao processar data (IllegalArgumentException): " + dataTexto);
            return new Date(); // Retorna uma data padrão em caso de erro
        }
    }

    @Override
    public String toString() {
        return String.format("%s %d, %04d", month, day, year);
    }
}