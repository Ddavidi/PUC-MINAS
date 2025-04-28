class EstudoFila {

    // classe celula
    public static class Celula {
        public int elemento;
        public Celula prox;

        public Celula(){
            this(0);
        }

        public Celula(int elemento){
            this.elemento = elemento;
            this.prox = null;
        }
    }


    // classe lista
    public static class Fila {
        public Celula primeiro;
        public Celula ultimo;

        public Fila(){
            primeiro = new Celula();
            ultimo = primeiro;
        }

        public void inserir(int elemento){
            ultimo.prox = new Celula(elemento);
            ultimo = ultimo.prox;
        }

        public int remover() throws Exception{
            if(primeiro == ultimo){
                throw new Exception("Fila vazia - impossivel remover");
            }

            Celula tmp = primeiro;
            primeiro = primeiro.prox;
            int resp = primeiro.elemento;
            tmp.prox = null;
            tmp = null;

            return resp;
        }

        public void mostrar(){
            System.out.print("[ ");
            for(Celula i = primeiro.prox; i!=null; i = i.prox){
                System.out.print(i.elemento + " ");
            }

            System.out.println("]");
        }
    }

    public static void main(String[] args) throws Exception{

        Fila fila = new Fila();

        fila.inserir(2);
        fila.inserir(4);
        fila.mostrar();
        fila.inserir(5);
        fila.mostrar();
        fila.remover();
        fila.mostrar();

    }
}