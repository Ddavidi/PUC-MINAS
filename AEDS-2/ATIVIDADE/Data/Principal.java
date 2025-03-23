import java.util.Scanner;

public class Principal {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);

        
    }
}

class Data {
    private int dia;
    private int mes;
    private int ano;

    public Data(){
    }
    public Data(int dia){
        this.dia = dia;
    }
    public int getDia(){
        return dia;
    }
    public void setDia(int dia){
        this.dia = dia;
    }
}

