public class Lista {
    private int[] array;
    private int n;

    public Lista(){
        this(10);
    }

    public Lista(int tamanho){
        array = new int[tamanho];
        n = 0;
    }

    public void inserirInicio(int x) throws Exception {
        if(n>=array.length){
            throw new Exception("Erro ao inserir");
        }

        for(int i=n; i>0; i--){
            array[i] = array[i-1];
        }

        array[0] = x;
        n++;
    }

    public void inserirFim(int x) throws Exception {
        if(n>=array.length){
            throw new Exception("Erro ao inserir");
        }

        array[n] = x;
        n++;
    }

    public void inserir(int x, int pos) throws Exception {
        if(n>=array.length){
            throw new Exception("Erro ao inserir");
        }

        for(int i=n;i>pos; i--){
            array[i] = array[i-1];
        }

        array[pos] = x;
        n++;
    }

    public int removerInicio() throws Exception {
        if(n==0){
            throw new Exception("Erro ao remover");
        }

        int resp = array[0];
        n--;

        for(int i=0; i<n; i++){
            array[i] = array[i+1];
        }

        return resp;
    }

    public int removerFim() throws Exception {
        if(n==0){
            throw new Exception("Erro ao remover");
        }

        int resp = array[n-1];
        n--;

        return resp;
    }

    public int remover(int pos) throws Exception {
        if(n==0){
            throw new Exception("Erro ao remover"); 
        }

        int resp = array[pos];
        n--;

        for(int i=pos; i<n;i++){
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