import java.util.Scanner;
import java.util.Locale;

public class leituraDados {
    public static void processarRegistro(int id, double preco, String tempo, String cidade) {
        System.out.printf("Registro lido: %d %.2f %s %s\n", id, preco, tempo, cidade);
      }

    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        scan.useLocale(Locale.US);

        int id;
        double preco;
        String tempo;
        String cidade;

        while((id = scan.nextInt()) != 0){
            preco = scan.nextDouble();
            tempo = scan.next();
            cidade = scan.nextLine().trim();
            processarRegistro(id, preco, tempo, cidade);
            }
            
        scan.close();
    }
}