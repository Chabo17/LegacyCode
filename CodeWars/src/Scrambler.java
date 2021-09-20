import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;


public class Scrambler {
	

	static String [] words;
	static char [][] ch;
	static int [][] dir={{1,0},{1,1},{0,1},{-1,0},{0,-1},{-1,-1},{-1,1},{1,-1}};
	
	public static void buildGrid() throws FileNotFoundException{
		Scanner fs = new Scanner(new File("src/Sram")),ss;
		int col=Integer.parseInt(fs.nextLine());//number of rows in the scramble 
		int n=Integer.parseInt(fs.nextLine());//number of lines in the input text
		String str="";
		while(n!=0){//gets all of the text lines in the input needed for the text
			String line=fs.nextLine();
			ss= new Scanner(line);
			while(ss.hasNext()){
				str+=ss.next();
			}				
			n--;
		}

		str=str.replaceAll("[\\W]", "");//gets rid of all of the non ascii characters
		str=str.toUpperCase(); 
		int ind=0;//keeps track of the index
		ch= new char [col][(str.length()/col)+1];
		for(int i =0;i<(str.length()/col)+1;i++){//builds the cols
			for (int j =0;j<col;j++){
				if(ind>=str.length())
					break;
				ch[j][i]=str.charAt(ind);//builds the grid
				ind++;
			}
		}
		for (int i =0;i<ch.length;i++){
			for(int j=0;j<(str.length()/col)+1;j++){
				System.out.print(ch[i][j]);//prints out the grid
			}
			System.out.println();
		}
		int w=Integer.parseInt(fs.nextLine());//finds out how many words there are
		words = new String[w];
		for (int q=0;q<w;q++){//gets all of the words
			words[q]=fs.nextLine();
		}
	}
	
	public static void find(String word){
		String fin =word;
		int num=0;
		int needc=0;
		for (int r=0;r<ch.length;r++){//looks through the array for the first letter
			for (int c=0;c<ch[0].length;c++){
				if(ch[r][c]==word.charAt(0)){
					for (int i=0;i<dir.length;i++){
						int row=r;
						int col=c;
						while(valid(row,col)&&num<word.length()&&ch[row][col]==word.charAt(num)){//while it is the word and in bounds it counts the length
							num+=1;
							row+=dir[i][0];
							col+=dir[i][1];
						}
						if(num==word.length()){
							if(needc>0)//checks if it needs a comma 
								fin+=", "+r+" "+c;
							else
								fin+=" "+r+" "+c;
							needc++;
						}
						num=0;
						}
					}
				}
			}
		if(needc==0)
			System.out.println(word+" NOT FOUND");
		else
			System.out.println(fin);
		
	}
	
	public static boolean valid(int r, int c){//checks if the row col combo is in bounds 
		if(r>=ch.length||r<0){
			return false;
		}else if(c>=ch[0].length||c<0){
			return false;
		}
		return true;
	}
	

	public static void main(String[] args) throws FileNotFoundException {
		buildGrid();
		for(int i=0;i<words.length;i++){
			find(words[i]);
		}
	}
	}