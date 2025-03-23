public class PrincipalLista {
    public static void main(String[] args) throws Exception{
        Lista lista = new Lista();

        lista.inserirInicio(1);
        lista.inserirInicio(3);
        lista.inserir(4, 1);
        lista.inserirFim(5);

        lista.mostrar();

        lista.remover(1);

        lista.mostrar();
    }
}