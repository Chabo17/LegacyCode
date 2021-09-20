import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.Stack;

public class Reversi {

	public static void main(String[] args) throws FileNotFoundException {
		/*
		 * Scanner fs = new Scanner(new File("src/rev")); String str=""; int i
		 * =0; while(fs.hasNextLine()){ String l = fs.nextLine();
		 * if(l.equals("REVERSI")) i++; else if(i%2==0) str=l+" "+str; else
		 * str=str+" "+l; } System.out.println(str); }
		 */
		Scanner fs = new Scanner(new File("src/rev"));
		String str = "";
		Stack<String> s1 = new Stack<>();
		Stack<String> s2 = new Stack<>();
		int i = 0;
		while (fs.hasNextLine()) {
			String l = fs.nextLine();
			if (l.equals("REVERSI")) {
				if (i % 2 == 0) {
					while (!s1.isEmpty()) {
						s2.push(s1.pop());
					}
				} else {
					while (!s2.isEmpty()) {
						s1.push(s2.pop());
					}
				}

				i++;
			} else if (i % 2 == 0)
				s1.push(l);
			else
				s2.push(l);

		}
		if (i % 2 == 0)
			System.out.println(s1);
		else
			while(!s2.isEmpty()){
				s1.push(s2.pop());
			}
			while(!s1.isEmpty()){
				str+=s1.pop()+" "; 
			}
			System.out.println(str);
	}
}
