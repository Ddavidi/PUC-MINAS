
public class Pilha{
    private int[] array;
    private int n;

    Pilha(){
        this(6);
    }

    Pilha(int tamanho){
        array = new int[tamanho];
        this.n = 0;
    }

    public void inserir(int elem) throws Exception{
        if(n>=array.length){
            throw new Exception("Pilha cheia");
        }

        array[n] = elem;
        n++;
    }

    public int remover() throws Exception{
        if(n==0){
            throw new Exception("Pilha vazia");
        }

        int resp = array[n-1];
        n--;

        return resp;
    }

    public void mostrar (){
        for(int i = n-1; i >= 0; i--){
           System.out.print(array[i] + " ");
        }
        System.out.println();
    }

    public boolean pesquisar (int elem){
        boolean flag = false;

        for(int i=0;i<n; i++){
            if(array[i] == elem){
                flag = true;
                i = n;
            }
        }

        return flag;
    }
}
