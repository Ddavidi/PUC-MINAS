import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.net.HttpURLConnection;
import java.net.URL;

public class HTML {

    public static void main(String[] args) {
        // Scanner para ler as entradas
        java.util.Scanner scanner = new java.util.Scanner(System.in);

        // Entrada do nome da página
        System.out.print("Digite o nome da página: ");
        String nomePagina = scanner.nextLine();
        
        // Entrada da URL
        System.out.print("Digite a URL da página: ");
        String url = scanner.nextLine();

        // Chama o método para obter o código HTML da página
        String htmlContent = getHtmlContent(url);

        // Exibe o nome da página e o conteúdo HTML
        if (htmlContent != null) {
            System.out.println("\nNome da página: " + nomePagina);
            System.out.println("Código fonte HTML da página:\n");
            System.out.println(htmlContent);
        } else {
            System.out.println("Não foi possível acessar a página.");
        }
    }

    // Método para obter o conteúdo HTML da página
    public static String getHtmlContent(String urlString) {
        StringBuilder content = new StringBuilder();
        try {
            // Cria o objeto URL
            URL url = new URL(urlString);
            
            // Abre uma conexão HTTP com a URL
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            
            // Define o método de requisição como GET (padrão)
            connection.setRequestMethod("GET");
            
            // Obtém o código de resposta da requisição
            int responseCode = connection.getResponseCode();
            
            // Verifica se a resposta foi bem-sucedida (código 200)
            if (responseCode == HttpURLConnection.HTTP_OK) {
                // Cria um BufferedReader para ler a resposta da página
                BufferedReader in = new BufferedReader(new InputStreamReader(connection.getInputStream()));
                String inputLine;
                
                // Lê linha por linha e adiciona ao StringBuilder
                while ((inputLine = in.readLine()) != null) {
                    content.append(inputLine);
                }
                in.close(); // Fecha o BufferedReader
            } else {
                System.out.println("Erro na requisição. Código de resposta: " + responseCode);
                return null;
            }
        } catch (IOException e) {
            System.out.println("Erro ao acessar a página: " + e.getMessage());
            return null;
        }
        return content.toString();
    }
}
