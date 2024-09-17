package Eternity;
/*
 * Project by Silent Rider
 **/
public class toHex_toBin {

    public static void main(String[] args) {
        String binaryNumber = "100111010000";
        String hexNumber = "9d0";
        System.out.println("Двоичное число " + binaryNumber + " равно шестнадцатеричному числу " + toHex(binaryNumber));
        System.out.println("Шестнадцатеричное число " + hexNumber + " равно двоичному числу " + toBinary(hexNumber));
    }

    public static String toHex(String binaryNumber) {
        if (binaryNumber == null){
            return "";}
        StringBuilder hex = new StringBuilder(binaryNumber);
        while (hex.length()%4 != 0) {
            hex.reverse();
            hex.append("0");
            hex.reverse();
        }
        for (int i = 0; i < hex.length()-1; i++){
            if (hex.substring(i, i+4).equals("0000")) {
                hex.replace(i, i+4, "0");
            }
            else if (hex.substring(i, i+4).equals("0001")) {
                hex.replace(i, i+4, "1");
            }
            else if (hex.substring(i, i+4).equals("0010")) {
                hex.replace(i, i+4, "2");
            }
            else if (hex.substring(i, i+4).equals("0011")) {
                hex.replace(i, i+4, "3");
            }
            else if (hex.substring(i, i+4).equals("0100")) {
                hex.replace(i, i+4, "4");
            }
            else if (hex.substring(i, i+4).equals("0101")) {
                hex.replace(i, i+4, "5");
            }
            else if (hex.substring(i, i+4).equals("0110")) {
                hex.replace(i, i+4, "6");
            }
            else if (hex.substring(i, i+4).equals("0111")) {
                hex.replace(i, i+4, "7");
            }
            else if (hex.substring(i, i+4).equals("1000")) {
                hex.replace(i, i+4, "8");
            }
            else if (hex.substring(i, i+4).equals("1001")) {
                hex.replace(i, i+4, "9");
            }
            else if (hex.substring(i, i+4).equals("1010")) {
                hex.replace(i, i+4, "a");
            }
            else if (hex.substring(i, i+4).equals("1011")) {
                hex.replace(i, i+4, "b");
            }
            else if (hex.substring(i, i+4).equals("1100")) {
                hex.replace(i, i+4, "c");
            }
            else if (hex.substring(i, i+4).equals("1101")) {
                hex.replace(i, i+4, "d");
            }
            else if (hex.substring(i, i+4).equals("1110")) {
                hex.replace(i, i+4, "e");
            }
            else if (hex.substring(i, i+4).equals("1111")) {
                hex.replace(i, i+4, "f");
            }
            else {
                return "";
            }
        }
        String hexi = hex.toString();
        return hexi;
    }

    public static String toBinary(String hexNumber) {
        if (hexNumber == null){
            return "";
        }
        StringBuilder bin = new StringBuilder(hexNumber);
        for (int i = 0; i < bin.length(); i+=4){
            if (bin.charAt(i) == '0') {
                bin.replace(i, i+1, "0000");
            }
            else if (bin.charAt(i) == '1') {
                bin.replace(i, i+1, "0001");
            }
            else if (bin.charAt(i) == '2') {
                bin.replace(i, i+1, "0010");
            }
            else if (bin.charAt(i) == '3') {
                bin.replace(i, i+1, "0011");
            }
            else if (bin.charAt(i) == '4') {
                bin.replace(i, i+1, "0100");
            }
            else if (bin.charAt(i) == '5') {
                bin.replace(i, i+1, "0101");
            }
            else if (bin.charAt(i) == '6') {
                bin.replace(i, i+1, "0110");
            }
            else if (bin.charAt(i) == '7') {
                bin.replace(i, i+1, "0111");
            }
            else if (bin.charAt(i) == '8') {
                bin.replace(i, i+1, "1000");
            }
            else if (bin.charAt(i) == '9') {
                bin.replace(i, i+1, "1001");
            }
            else if (bin.charAt(i) == 'a') {
                bin.replace(i, i+1, "1010");
            }
            else if (bin.charAt(i) == 'b') {
                bin.replace(i, i+1, "1011");
            }
            else if (bin.charAt(i) == 'c') {
                bin.replace(i, i+1, "1100");
            }
            else if (bin.charAt(i) == 'd') {
                bin.replace(i, i+1, "1101");
            }
            else if (bin.charAt(i) == 'e') {
                bin.replace(i, i+1, "1110");
            }
            else if (bin.charAt(i) == 'f') {
                bin.replace(i, i+1, "1111");
            }
            else {
                return "";
            }
        }
        String bina = bin.toString();
        return bina;
    }
}
