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

        public int tamanho(){
            int tamanho = 0;
            for(Celula i=primeiro.prox; i!=null; i=i.prox){
                tamanho++;
            }

            return tamanho;
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

        public void inserir(int elemento, int pos) throws Exception{
            int tamanho = tamanho();
            
            if(pos<0 || pos>tamanho){
                throw new Exception("Erro!");
            }

            else if(pos == 0){
                inserirInicio(elemento);
            }

            else if(pos == tamanho){
                inserirFim(elemento);
            }
                
            else {
                Celula i = primeiro;

                for(int j=0; j<pos; i=i.prox);

                Celula tmp = new Celula(elemento);
                tmp.prox = i.prox;
                i.prox = tmp;
                tmp = i = null;
            }
        }

        public int removerInicio(){
            int resp = primeiro.prox.elemento;
            primeiro.prox = primeiro.prox.prox;

            return resp;
        }

        public int removerFim(){
            int resp = ;
        }
    }

    public static void main(String[] args){

    }
}