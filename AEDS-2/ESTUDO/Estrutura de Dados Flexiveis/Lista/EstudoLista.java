public class EstudoLista{
    public static class Celula{
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

    public static class Lista{
        public Celula primeiro;
        public Celula ultimo;

        Lista(){
            primeiro = new Celula();
            ultimo = primeiro;
        }

        public void inserirInicio(int elemento){
            Celula tmp = new Celula(elemento);
            tmp.prox = primeiro.prox;
            primeiro.prox = tmp;

            if(primeiro == ultimo){
                ultimo = tmp;
            }

            tmp = null;
        }

        public void inserirFim(int elemento){
            ultimo.prox = new Celula(elemento);
            ultimo = ultimo.prox;
        }

        public void inserir(int elemento, int pos){
            int tamanho = tamanho();
            
            if(primeiro == ){

            }
        }
    }

    public static void main(String[] args){

    }
}