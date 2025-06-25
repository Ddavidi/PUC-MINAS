class No {
    public char letra;
    public No dir;
    public No esq;
    public Celula primeiro, ultimo;

    public No(char letra){
        this.letra = letra;
        this.dir = this.esq = null;
        primeiro = ultimo = new Celula();

    }
}