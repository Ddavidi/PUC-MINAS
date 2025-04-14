/*
   ==UserScript==
 @name         TP02Q01 - Classe em Java
 @namespace    https://github.com/Ddavidi/PUC-MINAS
 @description  VERDE PUC MINAS - TP02Q01 - Classe em Java
 @author       @ddavidi_
   ==/UserScript==
*/

class Show {
    private String SHOW_ID;
    private String TYPE;
    private String TITLE;
    private String DIRECTOR;
    private String[] CAST;
    private String COUNTRY;
    private String DATE_ADDED;
    private String RELEASE_YEAR;
    private String RATING;
    private String DURATION;
    private String[] LISTED_IN;
    private String DESCRIPTION;

    Show (String SHOW_ID, String TYPE, String TITLE, String DIRECTOR, String[] CAST, String COUNTRY, String DATE_ADDED, String RELEASE_YEAR, String RATING, String DURATION, String[] LISTED_IN, String DESCRIPTION){
        this.SHOW_ID = SHOW_ID;
        this.TYPE = TYPE;
        this.TITLE = TITLE;
        this.DIRECTOR = DIRECTOR;
        this.CAST = CAST;
        this.COUNTRY = COUNTRY;
        this.DATE_ADDED = DATE_ADDED;
        this.RELEASE_YEAR = RELEASE_YEAR;
        this.RATING = RATING;
        this.DURATION = DURATION;
        this.LISTED_IN = LISTED_IN;
        this.DESCRIPTION = DESCRIPTION;
    }

    public String getSHOW_ID() {
        return SHOW_ID;
    }

    public static Show ler(String linha){
        String partes[] = new String[100]; // atributos

        String campo = "";
        int i = 0;
        int j = 0;

        while(i < linha.length()){
            if(linha.charAt(i) == '"'){
                i++;
                while(linha.charAt(i) != '"'){
                    campo += linha.charAt(i);
                    i++;
                }
                i++;

                System.out.println(campo);

                partes[j] = campo;
                j++;
                campo = "";
                i++;
            }

            else if(linha.charAt(i) == ','){
                if(campo.isEmpty()){
                    partes[j] = "NaN";
                    j++;
                    i++;
                } else{
                    System.out.println(campo);
                    partes[j] = campo;
                    j++;
                    campo = "";
                    i++;
                }
            }
            
            else {
                campo += linha.charAt(i);
                i++;
            }
        }

        String SHOW_ID = partes[0];
        String TYPE = partes[1];
        String TITLE = partes[2];
        String DIRECTOR = partes[3];
        String CAST[] = partes[4].equals("NaN") ? new String[0] : partes[4].split(",\\s*");
        String COUNTRY = partes[5];
        String DATE_ADDED = partes[6];
        String RELEASE_YEAR = partes[7];
        String RATING = partes[8];
        String DURATION = partes[9];
        String LISTED_IN[] = partes[10].equals("NaN") ? new String[0] : partes[10].split(",\\s*");
        String DESCRIPTION = partes[11];

        System.out.println("ID:" + SHOW_ID);

        Show show = new Show(SHOW_ID, TYPE, TITLE, DIRECTOR, CAST, COUNTRY, DATE_ADDED, RELEASE_YEAR, RATING, DURATION, LISTED_IN, DESCRIPTION);
        
        return show;
    }

    public void mostreShow(String id) {
        if (SHOW_ID != null && SHOW_ID.equals(id)) {
            // Formata CAST manualmente
            String castStr = "NaN";
            if (CAST != null && CAST.length > 0) {
                castStr = "[";
                for (int i = 0; i < CAST.length; i++) {
                    castStr += CAST[i];
                    if (i < CAST.length - 1) {
                        castStr += ", ";
                    }
                }
                castStr += "]";
            }

            // Formata LISTED_IN manualmente
            String listedInStr = "NaN";
            if (LISTED_IN != null && LISTED_IN.length > 0) {
                listedInStr = "[";
                for (int i = 0; i < LISTED_IN.length; i++) {
                    listedInStr += LISTED_IN[i];
                    if (i < LISTED_IN.length - 1) {
                        listedInStr += ", ";
                    }
                }
                listedInStr += "]";
            }

            // Exibe a saída formatada
            System.out.printf("=> %s ## %s ## %s ## %s ## %s ## %s ## %s ## %s ## %s ## %s ## %s\n",
                SHOW_ID != null ? SHOW_ID : "NaN",
                TITLE != null ? TITLE : "NaN",
                TYPE != null ? TYPE : "NaN",
                DIRECTOR != null ? DIRECTOR : "NaN",
                castStr,
                COUNTRY != null ? COUNTRY : "NaN",
                DATE_ADDED != null ? DATE_ADDED : "NaN",
                RELEASE_YEAR != null ? RELEASE_YEAR : "NaN",
                RATING != null ? RATING : "NaN",
                DURATION != null ? DURATION : "NaN",
                listedInStr
            );
        }
    }
}
