
import java.io.*; 

public class prueba1 {
    public static void main(String[] args) {
        try{
            File file = new File("input.txt"); 
  
            BufferedReader br = new BufferedReader(new FileReader(file)); 
  
            long res=0;
            long fuels=0;
            long fuel=0;
            for(int i = 0; i< 100; i++) {
                fuels = Integer.parseInt(br.readLine());
                while(fuels>0) {
                	fuels=(Math.floorDiv(fuels,3)-2);
                	if(fuels>0)
                	fuel+=fuels;
                }
                res+=fuel;
                fuel=0;
            }
            System.out.println(res);
        }
        catch(IOException E){
            System.out.println("caca");
        }
    }
}


