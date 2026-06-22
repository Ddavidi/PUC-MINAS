/*
   ==UserScript==
 @name         T04Q04 - Árvore Alvinegra em Java
 @namespace    https://github.com/Ddavidi/PUC-MINAS
 @description  VERDE PUC MINAS - T04Q04 - Árvore Alvinegra em Java
 @author       @ddavidi_
   ==/UserScript==
*/

import java.io.File;
import java.util.Arrays;
import java.util.Scanner;

public class ArvoreAlvinegraJava {
    public static void main(String[] args) {

        Show[] shows = Show.lerArquivo();
        ArvoreAlvinegra arvore = new ArvoreAlvinegra();
        Scanner sc = new Scanner(System.in);
        String entrada = sc.nextLine();

        while (!entrada.equals("FIM")) {
            try {
                int index = Integer.parseInt(entrada.substring(1));
                if (index >= 0 && index < shows.length && shows[index] != null) {
                    try {
                        arvore.inserir(shows[index - 1].clone());
                    } catch (Exception e) {
                        System.out.println("Erro ao inserir: " + e.getMessage());
                    }
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
                boolean encontrado = arvore.pesquisar(entrada);
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
        } catch (Exception e) {
            System.out.println("Erro ao processar data: " + dataTexto);
            return new Date(); // Retorna uma data padrão em caso de erro
        }
    }

    @Override
    public String toString() {
        return String.format("%s %d, %04d", month, day, year);
    }
}

class No {
    public Show show;
    public boolean cor;
    public No esq, dir;

    public No(Show show) {
        this.show = show;
        this.cor = false;
        this.esq = null;
        this.dir = null;
    }

    public No(Show show, boolean cor) {
        this.show = show;
        this.cor = cor;
        this.esq = null;
        this.dir = null;
    }
}


class  ArvoreAlvinegra {
    private No raiz;

    public ArvoreAlvinegra() {
        this.raiz = null;
    }

    public boolean pesquisar(String titulo) {
        System.out.print("=>raiz  ");
        return pesquisarRecursivo(raiz, titulo);
    }

    private boolean pesquisarRecursivo(No no, String titulo) {
        if (no == null) {
            return false;
        }
        if (titulo.equals(no.show.getTitle())) {
            return true;
        }
        if (titulo.compareTo(no.show.getTitle()) < 0) {
            System.out.print("esq ");
            return pesquisarRecursivo(no.esq, titulo);
        } else {
            System.out.print("dir ");
            return pesquisarRecursivo(no.dir, titulo);
        }
    }

    public void inserir(Show show) throws Exception {
        // Se a arvore estiver vazia
        if (raiz == null) {
            raiz = new No(show);

        } else if (raiz.esq == null && raiz.dir == null) {
            if (show.getTitle().compareTo(raiz.show.getTitle()) < 0) {
                raiz.esq = new No(show);
            } else {
                raiz.dir = new No(show);
            }

        } else if (raiz.esq == null) {
            if (show.getTitle().compareTo(raiz.show.getTitle()) < 0) {
                raiz.esq = new No(show);

            } else if (show.getTitle().compareTo(raiz.dir.show.getTitle()) < 0) {
                raiz.esq = new No(raiz.show);
                raiz.show = show;

            } else {
                raiz.esq = new No(raiz.show);
                raiz.show = raiz.dir.show;
                raiz.dir.show = show;
            }
            raiz.esq.cor = raiz.dir.cor = false;

        } else if (raiz.dir == null) {
            if (show.getTitle().compareTo(raiz.show.getTitle()) > 0) {
                raiz.dir = new No(show);

            } else if (show.getTitle().compareTo(raiz.esq.show.getTitle()) > 0) {
                raiz.dir = new No(raiz.show);
                raiz.show = show;

            } else {
                raiz.dir = new No(raiz.show);
                raiz.show = raiz.esq.show;
                raiz.esq.show = show;
            }
            raiz.esq.cor = raiz.dir.cor = false;

        } else {
            inserir(show, null, null, null, raiz);
        }
        raiz.cor = false;
    }


    private void inserir(Show show, No bisavo, No avo, No pai, No i) throws Exception {
        if (i == null) {
            if (show.getTitle().compareTo(pai.show.getTitle()) < 0) {
                i = pai.esq = new No(show, true);
            } else {
                i = pai.dir = new No(show, true);
            }
            if (pai.cor) {
                balancear(bisavo, avo, pai, i);
            }
        } else {
            if (i.esq != null && i.dir != null && i.esq.cor && i.dir.cor) {
                i.cor = true;
                i.esq.cor = i.dir.cor = false;
                if(i == raiz) {
                    raiz.cor = false;
                } else if (pai.cor) {
                    balancear(bisavo, avo, pai, i);
                }
            }
            if (show.getTitle().compareTo(i.show.getTitle()) < 0) {
                inserir(show, avo, pai, i, i.esq);
            } else if (show.getTitle().compareTo(i.show.getTitle()) > 0) {
                inserir(show, avo, pai, i, i.dir);
            } else {
                throw new Exception("Erro inserir (elemento repetido)!");
            }
        }
    }
  

    private void balancear(No bisavo, No avo, No pai, No i) {
        if (pai.cor == true) {
            if (pai.show.getTitle().compareTo(avo.show.getTitle()) > 0) {
                if (i.show.getTitle().compareTo(pai.show.getTitle()) > 0) {
                avo = rotacaoEsq(avo);
                } else {
                avo = rotacaoDirEsq(avo);
                }
            } else {
                if (i.show.getTitle().compareTo(pai.show.getTitle()) < 0) {
                avo = rotacaoDir(avo);
                } else {
                avo = rotacaoEsqDir(avo);
                }
            }
            if (bisavo == null) {
                raiz = avo;
            } else if (avo.show.getTitle().compareTo(bisavo.show.getTitle()) < 0) {
                bisavo.esq = avo;
            } else {
                bisavo.dir = avo;
            }
            avo.cor = false;
            avo.esq.cor = avo.dir.cor = true;
        }
    }


    private No rotacaoDir(No no) {
        No noEsq = no.esq;
        No noEsqDir = noEsq.dir;

        noEsq.dir = no;
        no.esq = noEsqDir;

        return noEsq;
    }

    private No rotacaoEsq(No no) {
        No noDir = no.dir;
        No noDirEsq = noDir.esq;

        noDir.esq = no;
        no.dir = noDirEsq;
        return noDir;
    }

    private No rotacaoDirEsq(No no) {
        no.dir = rotacaoDir(no.dir);
        return rotacaoEsq(no);
    }

    private No rotacaoEsqDir(No no) {
        no.esq = rotacaoEsq(no.esq);
        return rotacaoDir(no);
    }
}
