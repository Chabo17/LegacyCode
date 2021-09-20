import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;


public class LD {

	public static void main(String[] args) throws Exception {
		Scanner fs = new Scanner(new File("src/LD"));
		String At= "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
		int at =0;
		int [] counts = new int[26];
		while(fs.hasNextLine()){
			String line = fs.nextLine().toLowerCase();
			
			for(int i=0; i<line.length(); i++){
				char c = line.charAt(i);
				if(c>='a'&&c<='z')
				counts[c-'a']++;
			}
		}
		for(int c=0; c<counts.length;c++){
			System.out.print(At.charAt(c)+" ");
			for(int i=0; i<counts[c];i++){
				System.out.print("*");
			}
			at++;
			System.out.println();
		}
			
}
}
