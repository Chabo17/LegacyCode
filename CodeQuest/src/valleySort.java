import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;


public class valleySort {
	
	public static void main(String[] args) throws FileNotFoundException {
		ArrayList<Integer>num=new ArrayList<>();
		ArrayList<Integer>fin=new ArrayList<>();
		Scanner fs = new Scanner(new File("problem1.in.txt"));
		int i=0;
		while(fs.hasNextInt()){
			num.add(fs.nextInt());
		}
		while(!num.isEmpty()){
			int k=0;
			for(int j=1;j<num.size();j++){
				if(num.get(k)<num.get(j))
					k=j;
			}
			if(fin.size()%2==0){
				fin.add(num.remove(k));
			}else
				fin.add(num.remove(k),fin.size());
		}
		System.out.println(fin);
		
		
	}
}
