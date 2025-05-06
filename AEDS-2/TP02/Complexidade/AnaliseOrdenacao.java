import java.io.FileWriter;
import java.io.IOException;
import java.util.Random;

public class AnaliseOrdenacao {
    static class Metricas {
        long comparacoes;
        long movimentacoes;
        long tempoMillis;

        Metricas() {
            comparacoes = 0;
            movimentacoes = 0;
            tempoMillis = 0;
        }
    }

    // Ordenação por Seleção
    public static void selectionSort(int[] arr, Metricas metricas) {
        int n = arr.length;
        for (int i = 0; i < n - 1; i++) {
            int minIdx = i;
            for (int j = i + 1; j < n; j++) {
                metricas.comparacoes++;
                if (arr[j] < arr[minIdx]) {
                    minIdx = j;
                }
            }
            if (minIdx != i) {
                int temp = arr[i];
                arr[i] = arr[minIdx];
                arr[minIdx] = temp;
                metricas.movimentacoes += 3; // Três movimentações por troca
            }
        }
    }

    // Ordenação por Inserção
    public static void insertionSort(int[] arr, Metricas metricas) {
        int n = arr.length;
        for (int i = 1; i < n; i++) {
            int chave = arr[i];
            int j = i - 1;
            metricas.movimentacoes++; // Armazenar chave
            while (j >= 0) {
                metricas.comparacoes++;
                if (arr[j] <= chave) break;
                arr[j + 1] = arr[j];
                metricas.movimentacoes++;
                j--;
            }
            arr[j + 1] = chave;
            metricas.movimentacoes++;
        }
    }

    // Ordenação por Bolha
    public static void bubbleSort(int[] arr, Metricas metricas) {
        int n = arr.length;
        boolean trocou;
        for (int i = 0; i < n - 1; i++) {
            trocou = false;
            for (int j = 0; j < n - i - 1; j++) {
                metricas.comparacoes++;
                if (arr[j] > arr[j + 1]) {
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                    metricas.movimentacoes += 3; // Três movimentações por troca
                    trocou = true;
                }
            }
            if (!trocou) break;
        }
    }

    // Quicksort
    public static void quickSort(int[] arr, int low, int high, Metricas metricas) {
        if (low < high) {
            int pi = particionar(arr, low, high, metricas);
            quickSort(arr, low, pi - 1, metricas);
            quickSort(arr, pi + 1, high, metricas);
        }
    }

    private static int particionar(int[] arr, int low, int high, Metricas metricas) {
        int pivo = arr[high];
        int i = low - 1;
        metricas.movimentacoes++; // Armazenar pivo
        for (int j = low; j < high; j++) {
            metricas.comparacoes++;
            if (arr[j] <= pivo) {
                i++;
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
                metricas.movimentacoes += 3; // Três movimentações por troca
            }
        }
        int temp = arr[i + 1];
        arr[i + 1] = arr[high];
        arr[high] = temp;
        metricas.movimentacoes += 3; // Três movimentações por troca
        return i + 1;
    }

    // Gera vetor aleatório
    private static int[] gerarVetorAleatorio(int tamanho) {
        Random rand = new Random();
        int[] arr = new int[tamanho];
        for (int i = 0; i < tamanho; i++) {
            arr[i] = rand.nextInt(1000000); // Números até 1 milhão
        }
        return arr;
    }

    // Copia vetor
    private static int[] copiarVetor(int[] original) {
        int[] copia = new int[original.length];
        System.arraycopy(original, 0, copia, 0, original.length);
        return copia;
    }

    public static void main(String[] args) {
        int[] tamanhos = {100, 1000, 10000, 100000};
        String[] algoritmos = {"SelectionSort", "InsertionSort", "BubbleSort", "QuickSort"};
        try (FileWriter writer = new FileWriter("resultados_ordenacao.csv")) {
            writer.write("Algoritmo,Tamanho,Tempo_ms,Comparacoes,Movimentacoes\n");

            for (int tamanho : tamanhos) {
                int[] vetorOriginal = gerarVetorAleatorio(tamanho);

                for (String algoritmo : algoritmos) {
                    int[] vetor = copiarVetor(vetorOriginal);
                    Metricas metricas = new Metricas();
                    long inicio = System.currentTimeMillis();

                    switch (algoritmo) {
                        case "SelectionSort":
                            selectionSort(vetor, metricas);
                            break;
                        case "InsertionSort":
                            insertionSort(vetor, metricas);
                            break;
                        case "BubbleSort":
                            bubbleSort(vetor, metricas);
                            break;
                        case "QuickSort":
                            quickSort(vetor, 0, vetor.length - 1, metricas);
                            break;
                    }

                    metricas.tempoMillis = System.currentTimeMillis() - inicio;
                    writer.write(String.format("%s,%d,%d,%d,%d\n",
                            algoritmo, tamanho, metricas.tempoMillis,
                            metricas.comparacoes, metricas.movimentacoes));
                }
            }
        } catch (IOException e) {
            System.err.println("Erro ao escrever no arquivo CSV: " + e.getMessage());
        }
    }
}