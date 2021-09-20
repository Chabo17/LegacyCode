import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;


public class counting_ones {

	public static void main(String[] args) throws FileNotFoundException {
		Scanner fs = new Scanner(new File("src/Prob10-1-in.txt"));
		while (fs.hasNext()){
		int num=fs.nextInt();
		//System.out.println(num);
		if (num==-1)
			break;
		int count=0;
		String s="";
		//System.out.println(count);
		for (int i=0; i<=num; i++){
			System.out.println("loop");
			Integer k= new Integer(i);
			System.out.print(k);
			
		  s+=k.toString();
			System.out.print(s);
			
		}
		}

	}

}
