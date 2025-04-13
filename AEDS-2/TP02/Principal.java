import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;


class Principal {
    public static void main (String[] args) throws FileNotFoundException{
        File file = new File("disneyplus.csv");

        Scanner scan = new Scanner(file);

        Show shows[] = new Show[1369];
        int i = 0;

        while (scan.hasNext()) {            
            String linha = scan.nextLine();
            shows[i] = Show.ler(linha);
            i++;
        }

        for (int j = 0; j < i; j++) {
            System.out.println(shows[j]);
        }

    }

        // ler arquivo csv, e adicionar o show de cada linha no array
}