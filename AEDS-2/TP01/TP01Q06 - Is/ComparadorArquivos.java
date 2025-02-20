import java.io.*;
import java.util.*;

public class ComparadorArquivos {
    public static void main(String[] args) {
        String caminhoArquivo1 = "pub.out";
        String caminhoArquivo2 = "saida.txt";

        try {
            List<String> linhasArquivo1 = lerArquivo(caminhoArquivo1);
            List<String> linhasArquivo2 = lerArquivo(caminhoArquivo2);

            compararArquivos(linhasArquivo1, linhasArquivo2);
        } catch (IOException e) {
            System.err.println("Erro ao ler os arquivos: " + e.getMessage());
        }
    }

    public static List<String> lerArquivo(String caminho) throws IOException {
        List<String> linhas = new ArrayList<>();
        try (BufferedReader br = new BufferedReader(new FileReader(caminho))) {
            String linha;
            while ((linha = br.readLine()) != null) {
                linhas.add(linha);
            }
        }
        return linhas;
    }

    public static void compararArquivos(List<String> arquivo1, List<String> arquivo2) {
        int maxLinhas = Math.max(arquivo1.size(), arquivo2.size());

        for (int i = 0; i < maxLinhas; i++) {
            String linha1 = (i < arquivo1.size()) ? arquivo1.get(i) : "Linha ausente";
            String linha2 = (i < arquivo2.size()) ? arquivo2.get(i) : "Linha ausente";

            if (!linha1.equals(linha2)) {
                System.out.println("Diferença na linha " + (i + 1) + ":");
                System.out.println("Arquivo 1: " + linha1);
                System.out.println("Arquivo 2: " + linha2);
                System.out.println("-------------------");
            }
        }

        if (arquivo1.equals(arquivo2)) {
            System.out.println("Os arquivos são idênticos.");
        }
    }
}