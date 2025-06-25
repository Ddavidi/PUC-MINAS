

public class ArvoreBinaria {
    private No raiz;

    public ArvoreBinaria() {
        raiz = null;
    }

    public boolean pesquisar(int x){
        return pesquisar(x, raiz);
    }

    /*
    PESQUISAR
    */
    private boolean pesquisar(int x, No i){
        boolean resp;

        if(i == null){
            resp = false;
        }

        else if(i.elemento == x){
            resp = true;
        }

        else if(i.elemento > x){
            resp = pesquisar(x, i.esq);
        }

        else {
            resp = pesquisar(x, i.dir);
        }

        return resp;
    }


    /*
    CAMINHAR CENTRAL
    */
    public void caminharCentral() {
        System.out.print("[ ");
        caminharCentral(raiz);
        System.out.print("]");
    }

    private void caminharCentral(No i){
        if(i != null){
            caminharCentral(i.esq);
            System.out.print(i.elemento + " ");
            caminharCentral(i.dir);
        }
    }

    /*
    CAMINHAR POS ORDEM
    */
    public void caminharPos() {
        System.out.print("[ ");
        caminharPos(raiz);
        System.out.print("]");
    }

    private void caminharPos(No i){
        caminharPos(i.esq);
        caminharPos(i.dir);
        System.out.print(i.elemento + " ");
    }


    /*
    CAMINHAR PRE ORDEM
    */
    public void caminharPre(){
        System.out.print("[ ");
        caminharPre(raiz);
        System.out.print("]");
    }

    private void caminharPre(No i){
        System.out.print(i.elemento);
        caminharPre(i.esq);
        caminharPre(i.dir);
    }


    /*
    INSERIR
    */
    public void inserir(int x) throws Exception {
        raiz = inserir(x, raiz);
    }

    private No inserir(int x, No i) throws Exception {
        if (i == null){
            i = new No(x);
        }

        else if(x < i.elemento) {
            i.esq = inserir(x, i.esq);
        }

        else if(x > i.elemento) {
            i.dir = inserir(x, i.dir);
        }

        else {
            throw new Exception("Erro ao inserir");
        }

        return i;
    }


    /*
    REMOVER
    */
    public void remover(int x) throws Exception {
        raiz = remover(x, raiz);
    }

    public No remover(int x, No i) throws Exception {
        if(i == null) {
            throw new Exception("Erro ao remover!");
        }

        else if(x < i.elemento) {
            i.esq = remover(x, i.esq);
        }

        else if(x > i.elemento) {
            i.dir = remover(x, i);
        }

        else if(i.esq == null) {
            i = i.dir;
        }

        else if(i.dir == null){
            i = i.esq;
        }

        else {
            i.esq = maiorEsq(i, i.esq);
        }

        return i;
    }

    private No maiorEsq(No i, No j) {

      // Encontrou o maximo da subarvore esquerda.
		if (j.dir == null) {
			i.elemento = j.elemento; // Substitui i por j.
			j = j.esq; // Substitui j por j.ESQ.

      // Existe no a direita.
		} else {
         // Caminha para direita.
			j.dir = maiorEsq(i, j.dir);
		}
		return j;
	}

}