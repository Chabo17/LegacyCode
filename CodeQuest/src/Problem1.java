import java.io.File;
import java.util.Scanner;


public class Problem1 {
	public static void main(String[] args) throws Exception {
		Scanner fs = new Scanner(new File("Problem1.in.txt"));
		
		int T = Integer.parseInt(fs.nextLine());
		
		while(T-->0){
			int N =Integer.parseInt(fs.nextLine());
			for(int i=0; i<N;i++){
				for(int j=0; j<N;j++){
					System.out.print("# ");
				}
				System.out.println();
			}
		}
	}
}
