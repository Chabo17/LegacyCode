import java.io.File;
import java.text.DecimalFormat;
import java.text.NumberFormat;
import java.util.Scanner;


public class Problem5 {
	public static void main(String[] args) throws Exception {
		Scanner fs = new Scanner(new File("Problem5.in.txt")),ls;
		int T = Integer.parseInt(fs.nextLine());
		NumberFormat fnt = NumberFormat.getCurrencyInstance();
		while(T-->0){
			String line =fs.nextLine();
			line=line.replace("$", " ");
			ls= new Scanner(line);
			double amt = Double.parseDouble(ls.nextLine().substring(1));
			System.out.println("Total of the bill: $"+amt);
			System.out.println("15% = " + fnt.format(amt*.15));
			System.out.println("18% = " + fnt.format(amt*.18));
			System.out.println("20% = " + fnt.format(amt*.2));
		}
	}

}
