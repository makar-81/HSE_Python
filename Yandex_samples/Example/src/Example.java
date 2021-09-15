import java.io.*;

public class Example {
    public static void main(String[] args) throws Exception {
        BufferedReader string = new BufferedReader(new InputStreamReader(System.in));
        String start_line = string.readLine();
        int space = start_line.indexOf(" ");
        int A = Integer.parseInt(start_line.substring(0, space));
        //System.out.println(start_line.length());
        //System.out.println(start_line.substring(1));
        //System.out.println(start_line.substring(space+1));
        int B = Integer.parseInt(start_line.substring(space+1));
        System.out.println(A + B);
    }
}
