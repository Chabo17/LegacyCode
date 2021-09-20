import java.io.File;
import java.util.Scanner;


public class Problem2 {
	public static void main(String[] args) throws Exception {
		Scanner fs = new Scanner(new File("Problem2.in.txt"));
		
		int T = Integer.parseInt(fs.nextLine());
		
		while(T-->0){
			double mon = Double.parseDouble(fs.nextLine().substring(1));
			System.out.println(mon);
			mon = mon * 100;
			mon = (int)mon;
			int tens = (int)mon/1000;
			int five = ((int)mon%1000)/500;
			int o = (((int)mon%1000)%500)/100;
			int qu = o/25;
			int di = (o%25)/10;
			int ni = ((o%25)%10)/5;
			int pe = (((o%25)%10)%5);
			System.out.println(tens + " tens");
			System.out.println(five + " fives");
			System.out.println(o + " ones");
			System.out.println(qu + " quarters");
			System.out.println(di + " dimes");
			System.out.println(ni + " nickles");
			System.out.println(pe + " pennies");
			System.out.println("");
		}
	}
}
