public class EstudoListaDupla {

    public static class CelulaDupla {
        public int elemento;
        public CelulaDupla prox, ant;


        public CelulaDupla(){
            this(0);
        }

        public CelulaDupla(int elemento){
            this.elemento = elemento;
            this.prox = null;
            this.ant = null;
        }
    }

    public static class ListaDupla {
        public CelulaDupla primeiro;
        public CelulaDupla ultimo;

        public ListaDupla(){
            primeiro = new CelulaDupla();
            ultimo = primeiro;
        }

        public void inserirInicio(int elemento){
            CelulaDupla tmp = new CelulaDupla(elemento);
            tmp.ant = primeiro;
            tmp.prox = primeiro.prox;
            primeiro.prox = tmp;

            if(primeiro == ultimo){
                ultimo = tmp;
            } else {
                tmp.prox.ant = tmp;
            }

            tmp = null;
        }

        public void inserirFim(int elemento){
            ultimo.prox = new CelulaDupla(elemento);
            ultimo.prox.ant = ultimo;
            ultimo = ultimo.prox;
        }

        public void inserir(int elemento, int pos) throws Exception{
            int tamanho = tamanho();

            if(pos<0 || pos>tamanho){
                throw new Exception("Posicao invalida");
            }

            else if(pos == 0){
                inserirInicio(elemento);
            }

            else if(pos==tamanho){
                inserirFim(elemento);
            }

            else {
                CelulaDupla i = primeiro.prox;

                for(int j=0; j<pos; j++,i=i.prox);

                CelulaDupla tmp = new CelulaDupla(elemento);
                tmp.ant = i;
                tmp.prox = i.prox;
                tmp.ant.prox = tmp;
                tmp.prox.ant = tmp;
                tmp = i = null;
            }

        }

        public int removerInicio() throws Exception{ 
            if(primeiro == ultimo){
                throw new Exception("Erro");
            }

            CelulaDupla tmp = primeiro;
            primeiro = primeiro.prox;
            int resp = primeiro.elemento;
            tmp.prox = null;
            tmp.ant = null;
            tmp = null;

            return resp;
        }

        public int removerFim() throws Exception{
            if(primeiro == ultimo){
                throw new Exception("Erro");
            }

            int resp = ultimo.elemento;
            ultimo = ultimo.ant;
            ultimo.prox.ant = null;
            ultimo.prox = null;

            return resp;

        }

        public int remover(int pos) throws Exception{
            int resp;
            int tamanho = tamanho();

            if(pos<0 || pos>tamanho){
                throw new Exception("Erro");
            }

            else if(primeiro == ultimo){
                throw new Exception("Erro");
            }

            else if(pos == 0){
                resp = removerInicio();
            }
            else if(pos == tamanho-1){
                resp = removerFim();
            }
            else{
                CelulaDupla i = primeiro.prox;

                for(int j=0; j<pos; j++, i=i.prox);

                i.ant.prox = i.prox;
                i.prox.ant = i.ant;
                resp = i.elemento;
                i.prox = null;
                i.ant = null;
                i=null;
            }
            
            return resp;
        }

        public void mostrar(){
            System.out.print("[ ");
            for(CelulaDupla i=primeiro.prox; i!=null; i=i.prox){
                System.out.print(i.elemento + " ");
            }
            System.out.println("] ");
        }

        public void mostrarInverso(){
            System.out.print("[ ");
            for(CelulaDupla i=ultimo; i!=primeiro; i=i.ant){
                System.out.print(i.elemento + " ");
            }
            System.out.println("] ");
        }

        public boolean pesquisar(int elemento){
            boolean resp = false;
            for(CelulaDupla i=primeiro.prox; i!=ultimo; i=i.prox){
                if(i.elemento == elemento){
                    resp = true;
                    i = ultimo;
                }
            }

            return resp;
        }

        public int tamanho(){
        int tamanho = 0;

        for(CelulaDupla i=primeiro; i!=ultimo; i=i.prox, tamanho++);

        return tamanho;
        }
    }

    public static void main(String[] args){

    }
}