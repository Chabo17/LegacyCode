import java.io.File;
import java.util.Scanner;


public class Problem3 {
	public static void main(String[] args) throws Exception {
		Scanner fs = new Scanner(new File("Problem3.in.txt")),ls;
		
		int T = Integer.parseInt(fs.nextLine());
		
		while(T-->0){
			String line =fs.nextLine();
			line=line.replace(",", " ");
			ls = new Scanner(line);
			int s1=ls.nextInt();
			int s2=ls.nextInt();
			int s3=ls.nextInt();
			System.out.println(s1 + " " + s2 +" " + s3);
			if(s1+s2<=s3)
				System.out.println("it is not a triangle");
			else if(s1==s2&&s2==s3)
				System.out.println("It is an Equilateral Triangle");
			else if(s1==s2||s2==s3||s3==s1)
				System.out.println("It is an Isosceles Triangle");
			else 
				System.out.println("It is a Scalene Triangle");
		}
		}
}
