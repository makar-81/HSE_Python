import java.io.*;

public class Example2 {
        public static void main(String[] args) {
            try {
                BufferedReader br;
                BufferedWriter bw;
    
                FileReader fr;
                //BufferedInputStream fr;
                //OutputStream bw;
                FileWriter wr;
                
                fr = new FileReader("input.txt");
                wr = new FileWriter("output.txt");
                
                br = new BufferedReader(fr);
                bw = new BufferedWriter(wr);
                
                //br = new BufferedReader(new InputStreamReader(System.in));
                //bw = new BufferedWriter(new OutputStreamWriter(System.out));

                String start_line = br.readLine();
                int A = Integer.parseInt(start_line.substring(0, start_line.indexOf(" ")));
                int B = Integer.parseInt(start_line.substring(start_line.indexOf(" ")+1));
    
                String sum = Integer.toString(A+B);
                bw.write(sum);
                bw.flush();
                bw.close();
                br.close();

            } catch (FileNotFoundException e) {
                
                e.printStackTrace();
            }
            catch (IOException e) {
                e.printStackTrace();
            }
      
    }    
}
