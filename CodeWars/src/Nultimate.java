import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.Stack;


public class Nultimate {

	public static void main(String[] args) throws FileNotFoundException {
		Scanner fs = new Scanner(new File("src/nu")),ss;
		String str = "";
		int i;
		Stack<String> s1 = new Stack<>();
		while (fs.hasNextLine()) {
			i=fs.nextInt();
			if(i==0)
				break;
			String l = fs.nextLine();
			l.substring(1,l.length()-1);
			ss=new Scanner(l.substring(1,l.length()-1));
			while(ss.hasNext()){
				s1.push(ss.next());
			}
			while(i>1){
				s1.pop();
				i--;
			}
			System.out.println(s1.pop());
		}

	}

}
