import java.io.*;

public class Example3 {
    public static void main(String[] args) throws Exception {
        BufferedReader string = new BufferedReader(new InputStreamReader(System.in));
        String J = string.readLine();
        String S = string.readLine();
        char[] temp = S.toCharArray();
        int sum = 0;

        for (int i =0; i < temp.length;i++) {
            if (J.contains(Character.toString(temp[i]))) {
                   sum ++;
            } 
        }  
        System.out.println(sum);
    }
}