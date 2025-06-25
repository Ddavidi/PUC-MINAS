public class Agenda {
    private No raiz;

    public Agenda(){
        inserir();
    }

    public void inserir(){
        char letras[] = new char[] {'A', 'B', 'C', 'D'};
        for(char letra : letras){
            raiz = inserir(letra, raiz);
        }
    }

    No inserir(char letra, No i) {
        if(i == null){
            i = new No(letra);
        }

        else if(letra < i.letra){
            i.esq = inserir(letra, i.esq);
        }

        else if(letra > i.letra){
            i.dir = inserir(letra, i.dir);
        }

        else {
            // erro
        }

        return i;
    }
}