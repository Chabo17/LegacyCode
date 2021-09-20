import java.io.File;
import java.util.Scanner;


public class Problem4 {
	public static void main(String[] args) throws Exception {
		Scanner fs = new Scanner(new File("Problem4.in.txt")),ls;
		
		int T = Integer.parseInt(fs.nextLine());
		
		while(T-->0){
			String line =fs.nextLine();
			line=line.replace("|", " ");
			ls = new Scanner(line);
			String s1= ls.next();
			String s2 = ls.next();
			System.out.print(s1+ " | " +s2);
			for(int i =0;i<s2.length();i++){
				if(s2.contains(s1.substring(i,i+1))==false||s1.length()!=s2.length()||s1.equals(s2)){
					System.out.println(" NO ");
					return;
				}
			}
			for(int i =0;i<s2.length();i++){
				if(s1.contains(s2.substring(i,i+1))==false||s1.length()!=s2.length()||s1.equals(s2)){
					System.out.println(" NO ");
					return;
				}
			}
				System.out.println("    YES");
			
		}
		}
}
