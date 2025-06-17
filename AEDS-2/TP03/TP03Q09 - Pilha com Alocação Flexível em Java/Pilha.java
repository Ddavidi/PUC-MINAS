import java.io.*;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Locale;

class Show {
    private String showID;
    private String type;
    private String title;
    private String director;
    private String[] cast;
    private String country;
    private Date dateAdded;
    private int releaseYear;
    private String rating;
    private String duration;
    private String[] listedIn;

    // Construtor
    public Show() {
        this.showID = null;
        this.type = null;
        this.title = null;
        this.director = null;
        this.cast = null;
        this.country = null;
        this.dateAdded = null;
        this.releaseYear = 0;
        this.rating = null;
        this.duration = null;
        this.listedIn = null;
    }

    // Getters e Setters
    public String getShowID() { return showID; }
    public void setShowID(String showID) { this.showID = showID; }
    
    public String getType() { return type; }
    public void setType(String type) { this.type = type; }
    
    public String getTitle() { return title; }
    public void setTitle(String title) { this.title = title; }
    
    public String getDirector() { return director; }
    public void setDirector(String director) { this.director = director; }
    
    public String[] getCast() { return cast; }
    public void setCast(String[] cast) { this.cast = cast; }
    
    public String getCountry() { return country; }
    public void setCountry(String country) { this.country = country; }
    
    public Date getDateAdded() { return dateAdded; }
    public void setDateAdded(Date dateAdded) { this.dateAdded = dateAdded; }
    
    public int getReleaseYear() { return releaseYear; }
    public void setReleaseYear(int releaseYear) { this.releaseYear = releaseYear; }
    
    public String getRating() { return rating; }
    public void setRating(String rating) { this.rating = rating; }
    
    public String getDuration() { return duration; }
    public void setDuration(String duration) { this.duration = duration; }
    
    public String[] getListedIn() { return listedIn; }
    public void setListedIn(String[] listedIn) { this.listedIn = listedIn; }

    // Método para ordenar array de strings (Bubble Sort)
    private void ordenarArray(String[] array) {
        if (array == null) return;
        
        boolean trocou;
        int n = array.length;
        do {
            trocou = false;
            for (int i = 0; i < n - 1; i++) {
                if (array[i] != null && array[i+1] != null && 
                    array[i].compareTo(array[i+1]) > 0) {
                    String temp = array[i];
                    array[i] = array[i+1];
                    array[i+1] = temp;
                    trocou = true;
                }
            }
            n--;
        } while (trocou);
    }

    // Método para separar e ordenar strings por vírgula
    private String[] separarEOrdenar(String texto) {
        if (texto == null || texto.trim().isEmpty()) {
            return new String[]{"NaN"};
        }
        
        // Contar vírgulas para determinar tamanho do array
        int count = 1;
        for (int i = 0; i < texto.length(); i++) {
            if (texto.charAt(i) == ',') count++;
        }
        
        String[] resultado = new String[count];
        int index = 0;
        StringBuilder sb = new StringBuilder();
        
        for (int i = 0; i < texto.length(); i++) {
            char c = texto.charAt(i);
            if (c == ',') {
                resultado[index++] = sb.toString().trim();
                sb.setLength(0);
            } else {
                sb.append(c);
            }
        }
        resultado[index] = sb.toString().trim();
        
        ordenarArray(resultado);
        return resultado;
    }

    // Método para converter data
    private Date converterData(String texto) {
        if (texto == null || texto.trim().isEmpty()) {
            return null;
        }
        
        try {
            SimpleDateFormat sdf = new SimpleDateFormat("MMMM d, yyyy", Locale.ENGLISH);
            return sdf.parse(texto);
        } catch (ParseException e) {
            return null;
        }
    }

    // Método para parsear linha CSV
    public void parsearLinha(String linha) {
        if (linha == null) return;
        
        String[] campos = new String[20];
        for (int i = 0; i < campos.length; i++) {
            campos[i] = "";
        }
        
        StringBuilder campoAtual = new StringBuilder();
        boolean dentroAspas = false;
        int indiceCampo = 0;
        
        for (int i = 0; i < linha.length(); i++) {
            char c = linha.charAt(i);
            
            if (c == '"') {
                dentroAspas = !dentroAspas;
            } else if (c == ',' && !dentroAspas) {
                campos[indiceCampo] = campoAtual.toString();
                campoAtual.setLength(0);
                indiceCampo++;
            } else {
                campoAtual.append(c);
            }
        }
        campos[indiceCampo] = campoAtual.toString();
        
        // Atribuir valores aos campos
        this.showID = campos[0];
        this.type = campos[1].equalsIgnoreCase("movie") ? "Movie" : "TV Show";
        this.title = campos[2];
        this.director = campos[3].isEmpty() ? "NaN" : campos[3];
        this.country = campos[5].isEmpty() ? "NaN" : campos[5];
        this.rating = campos[8];
        this.duration = campos[9];
        
        this.cast = separarEOrdenar(campos[4]);
        
        this.listedIn = separarEOrdenar(campos[10]);
       
        this.dateAdded = converterData(campos[6]);
        
        this.releaseYear = campos[7].isEmpty() ? 0 : Integer.parseInt(campos[7]);
    }

    // Método para imprimir o show
    public void imprimir(int posicao) {
        String dateStr = "NaN";
        if (dateAdded != null) {
            SimpleDateFormat sdf = new SimpleDateFormat("MMMM d, yyyy", Locale.ENGLISH);
            dateStr = sdf.format(dateAdded);
        }
        
        StringBuilder elenco = new StringBuilder("[");
        if (cast != null) {
            for (int i = 0; i < cast.length; i++) {
                elenco.append(cast[i] != null ? cast[i] : "NaN");
                if (i < cast.length - 1) elenco.append(", ");
            }
        }
        elenco.append("]");
        
        StringBuilder categorias = new StringBuilder("[");
        if (listedIn != null) {
            for (int i = 0; i < listedIn.length; i++) {
                categorias.append(listedIn[i] != null ? listedIn[i] : "NaN");
                if (i < listedIn.length - 1) categorias.append(", ");
            }
        }
        categorias.append("]");
        
        if (posicao >= 0) {
            System.out.print("[" + posicao + "] ");
        }
        
        System.out.println("=> " + 
            (showID != null ? showID : "NaN") + " ## " +
            (title != null ? title : "NaN") + " ## " +
            (type != null ? type : "NaN") + " ## " +
            (director != null ? director : "NaN") + " ## " +
            elenco.toString() + " ## " +
            (country != null ? country : "NaN") + " ## " +
            dateStr + " ## " +
            releaseYear + " ## " +
            (rating != null ? rating : "NaN") + " ## " +
            (duration != null ? duration : "NaN") + " ## " +
            categorias.toString() + " ##");
    }
}


class PilhaSequencial {
    private Show[] lista;
    private int tamanho;
    private final int capacidadeMaxima;
    
    public PilhaSequencial(int capacidade) {
        this.capacidadeMaxima = capacidade;
        this.lista = new Show[capacidade];
        this.tamanho = 0;
    }
    
    // Empilhar (inserir no final)
    public void empilhar(Show show) {
        if (tamanho < capacidadeMaxima) {
            lista[tamanho] = show;
            tamanho++;
        }
    }
    
    // Desempilhar (remover do final)
    public Show desempilhar() {
        if (tamanho > 0) {
            tamanho--;
            Show removido = lista[tamanho];
            lista[tamanho] = null;
            return removido;
        }
        return null;
    }
    
    // Imprimir pilha em ordem reversa
    public void imprimirReverso() {
        for (int i = tamanho - 1; i >= 0; i--) {
            lista[i].imprimir(i);
        }
    }
    
    public int getTamanho() {
        return tamanho;
    }
}

public class Pilha {
    
    public static int converterString(String entrada) {
        if (entrada == null || entrada.isEmpty()) return 0;
        
        int valor = 0;
        int multiplicador = 1;
        
        for (int i = entrada.length() - 1; i > 0; i--) {
            int numero = entrada.charAt(i) - '0';
            valor += numero * multiplicador;
            multiplicador *= 10;
        }
        return valor;
    }
    
    // Método para verificar se é fim
    public static boolean ehFim(String entrada) {
        return "FIM".equals(entrada);
    }
    
    // Método para obter show por ID
    public static Show obterShowPorId(String entrada) {
        int id = converterString(entrada);
        Show show = new Show();
        
        try (BufferedReader br = new BufferedReader(new FileReader("/tmp/disneyplus.csv"))) {
            String linha;
            int contador = 0;
            boolean encontrado = false;
            
            while ((linha = br.readLine()) != null && !encontrado) {
                if (contador == id) {
                    show.parsearLinha(linha);
                    encontrado = true;
                }
                contador++;
            }
            
            if (!encontrado) {
                show = new Show(); // Retorna show vazio se não encontrado
            }
            
        } catch (IOException e) {
            System.err.println("Erro ao ler arquivo: " + e.getMessage());
        }
        
        return show;
    }
    
    // Método para separar comando e ID
    public static String[] separarComando(String entrada) {
        String[] resultado = new String[2];
        int espacoIndex = entrada.indexOf(' ');
        
        if (espacoIndex != -1) {
            resultado[0] = entrada.substring(0, espacoIndex);
            resultado[1] = entrada.substring(espacoIndex + 1);
        } else {
            resultado[0] = entrada;
            resultado[1] = "";
        }
        
        return resultado;
    }
    
    public static void main(String[] args) {
        try (BufferedReader reader = new BufferedReader(new InputStreamReader(System.in))) {
            PilhaSequencial pilha = new PilhaSequencial(500);
            
            // Leitura inicial dos shows
            String entrada = reader.readLine().trim();
            
            while (!ehFim(entrada)) {
                Show show = obterShowPorId(entrada);
                pilha.empilhar(show);
                entrada = reader.readLine().trim();
            }
            
            // Número de operações
            int n = Integer.parseInt(reader.readLine().trim());
            
            String[] removidos = new String[100];
            int indiceRemovidos = 0;
            
            // Processar operações
            for (int i = 0; i < n; i++) {
                entrada = reader.readLine().trim();
                String[] partes = separarComando(entrada);
                String comando = partes[0];
                String id = partes[1];
                
                if ("I".equals(comando)) {
                    // Inserir (empilhar)
                    Show show = obterShowPorId(id);
                    pilha.empilhar(show);
                } else if ("R".equals(comando)) {
                    // Remover (desempilhar)
                    Show removido = pilha.desempilhar();
                    if (removido != null && removido.getTitle() != null) {
                        removidos[indiceRemovidos++] = removido.getTitle();
                    }
                }
            }
            
            // Imprimir elementos removidos
            for (int i = 0; i < indiceRemovidos; i++) {
                System.out.println("(R) " + removidos[i]);
            }
            
            // Imprimir pilha em ordem reversa
            pilha.imprimirReverso();
            
        } catch (IOException e) {
            System.err.println("Erro de entrada/saída: " + e.getMessage());
        }
    }
}