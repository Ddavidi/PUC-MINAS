public class Fila {
    private int[] array;
    private int n;

    public Fila(){
        this(10);
    }

    public Fila(int tamanho){
        array = new int[tamanho];
        n = 0;
    }

    public void inserir(int x) throws Exception {
        if(n>=array.length){
            throw new Exception("Erro ao inserir");
        }

        for(int i=n;i>0; i--){
            array[i] = array[i-1];
        }

        array[0] = x;
        n++;
    }

    public int remover() throws Exception {
        if(n==0){
            throw new Exception("Erro ao remover");
        }

        int resp = array[0];
        n--;

        for(int i=0;i<n; i++){
            array[i] = array[i+1];
        }

        return resp;
    }

    public void mostrar(){
        System.out.print("[ ");
        for(int i=0; i<n;i++){
            System.out.print(array[i] + " ");
        }
        System.out.println("]");
    }

    public boolean pesquisar(int x){
        boolean resp = false;
        for(int i=0;i<n;i++){
            if(array[i] == x){
                resp = true;
                i = n;
            }
        }

        return resp;

    }
}