import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;


public class prob10 {

	public static void main(String[] args) throws FileNotFoundException {
		Scanner fs = new Scanner(new File("src/Prob10-1-in.txt")),ls;
		while(fs.hasNextLine()){
			String s=fs.nextLine();
			ls=new Scanner(s);
			int size=Integer.parseInt(ls.next());
			if(size==0)
				break;
			char a[] = new char[size];
			for (int k=0;k<size; k++){
				a[k]=s.charAt(k+2);
			}
			 char arr[]=new char[size];
			 int index=0;
			 for (int i=0;i<size;i++){
				 int counter=0;
				 arr[i]=a[index];
				 char c=a[index];
				 if (c>='a' && c<='z'){
					 index+=1+c-'a';
				 }
				 else if (c>='A' && c<='Z')
					 index+=1+c-'A';
				 else{
					 index+=1;
				 }
				 while (index>size)
					 index=index-size;
			 }
			 for (int i=0; i<size;i++){
				 System.out.print( arr[i]);
			 }
			 System.out.println();
			 
			
		
		}
	}

}
