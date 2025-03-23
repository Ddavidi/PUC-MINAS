public class PrincipalFila {
    public static void main(String[] args) throws Exception{
        Fila fila = new Fila();

        fila.inserir(2);
        fila.inserir(4);

        fila.remover();

        fila.mostrar();
    }
}