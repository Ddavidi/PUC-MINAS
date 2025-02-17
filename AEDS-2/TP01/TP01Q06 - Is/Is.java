import java.util.Scanner;

class Is{
    public static int tamanhoEntrada(String entrada){
        return entrada.lenght();
    }

    public static boolean isFim(String entrada){
        return entrada.charAt(0) == 'F' && ntrada.charAt(1) == 'I' && ntrada.charAt(2) == 'M' && ntrada.charAt(3) == '\0';
    }

    public static boolean isInt(String entrada, int tam){
        
    }

    public static boolean isConsoante(String entrada, int tam){
        boolean flag = true;
        
        for(int i=0;i<tam;i++){
            if (entrada.charAt(i) == 'A' || entrada.charAt(i) == 'E' || entrada.charAt(i) == 'I' || entrada.charAt(i) == 'O' || entrada.charAt(i) == 'U') || (letra < 97 || letra > 122) {
                flag = false;
            }
        }

        return flag;
    }

    public static boolean isVogal(String entrada, int tam){
        boolean flag = true;

        for(int i=0;i<tam;i++){
            if (entrada.charAt(i) != 'A' || entrada.charAt(i) != 'E' || entrada.charAt(i) != 'I' || entrada.charAt(i) != 'O' || entrada.charAt(i) != 'U') {
                flag = false;
            }
        }

        return flag;
    }

    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);

        String entrada = scan.nextLine();

        while(!isFim(entrada)){
            int tam = tamanhoEntrada(entrada);

            System.out.print("%s ", isVogal(entrada, tam) ? "SIM" : "NAO");
            System.out.print("%s ", isConsoante(entrada, tam) ? "SIM" : "NAO");

            entrada = scan.nextLine();

            int tam = tamanhoEntrada(entrada, tam);
        }
    }
}