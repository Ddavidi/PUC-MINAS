public class EstudoPilha {
    // classe Celula
    public static class Celula {
        public int elemento;
        public Celula prox;
        
        Celula(){
            this(0);
        }

        Celula(int elemento){
            this.elemento = elemento;
            this.prox = null;
        }
    }

    // classe Pilha
    public static class Pilha{
        public Celula topo;

        public Pilha(){
            topo = null;
        }

        public void inserir(int elemento){
            Celula tmp = new Celula(elemento);
            tmp.prox = topo;
            topo = tmp;
            tmp = null;
        }

        public int remover() throws Exception{
            if(topo == null)
                throw new Exception("Pilha vazia");

            int resp = topo.elemento;
            Celula tmp = topo;
            topo = topo.prox;
            tmp.prox = null;
            tmp = null;

            return resp;

        }

        public void mostrar(){
            System.out.print("[ ");

            for(Celula i=topo; i!=null; i=i.prox){
                System.out.print(i.elemento + " ");
            }

            System.out.println("]");
        }
    }


    public static void main(String[] args) throws Exception{
        Pilha pilha = new Pilha();

        pilha.inserir(7);
        pilha.inserir(5);
        pilha.inserir(3);
        pilha.mostrar();

        pilha.remover();

        pilha.mostrar();

        pilha.inserir(9);

        pilha.mostrar();

    }    
}
