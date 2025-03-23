import java.util.Scanner;

public class Principal {
    public static void main(String[] args) throws Exception {
        Scanner scan = new Scanner(System.in);  
        
        String acao;
        int valor;

        Pilha pilha = new Pilha(10);
        
        while(scan.hasNext()) {
            acao = scan.next();

            try {
                if(acao.equals("E")) {
                    valor = scan.nextInt();
                    pilha.inserir(valor);
                }
                else if(acao.equals("D")) {
                    System.out.println(pilha.remover());
                }
                else if(acao.equals("M")) {
                    pilha.mostrar();
                }
                else if(acao.equals("P")) {
                    valor = scan.nextInt();
                    System.out.println(pilha.pesquisar(valor) ? "S" : "N");
                }
            } catch (Exception e) {
                System.out.println(e.getMessage());
            }
        }
        
        scan.close();
    }
}