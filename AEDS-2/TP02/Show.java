import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Show {
    private String SHOW_ID;
    private String TYPE;
    private String TITLE;
    private String DIRECTOR;
    private String CAST; //tem q ser lista de String
    private String COUNTRY;
    private String DATE_ADDED; //criar a classe Date
    private String RELEASE_YEAR;
    private String RATING;
    private String DURATION;
    private String LISTED_IN; //tem q ser lista de String


    public static Show ler(String linha){
        String partes[] = new String[11];

        String campo = "";
        int i = 0;
        int j = 0;

        while(i < linha.length()){
            if(linha.charAt(i) == ','){
                partes[j] = campo;
                j++;
                campo = "";
            }

            campo += linha.charAt(i);
            i++;
        }

        String SHOW_ID = partes[0];
        String TYPE = partes[1];
        String TITLE = partes[2];
        String DIRECTOR = partes[3];
        String CAST = partes[4];
        String COUNTRY = partes[5];
        String DATE_ADDED = partes[6];
        String RELEASE_YEAR = partes[7];
        String RATING = partes[8];
        String DURATION = partes[9];
        String LISTED_IN = partes[10];

        Show show = Show(SHOW_ID, TYPE, TITLE, DIRECTOR, CAST, COUNTRY, DATE_ADDED, RELEASE_YEAR, RATING, DURATION, LISTED_IN);
        
        return show;
    }

    Show(){

    }

    Show(String SHOW_ID, ){

    }


}
