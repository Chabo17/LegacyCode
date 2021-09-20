import java.io.File;
import java.text.NumberFormat;
import java.util.ArrayList;
import java.util.Scanner;


public class Problem6 {
	public static void main(String[] args) throws Exception {
		Scanner fs = new Scanner(new File("Problem6.in.txt")),ls;
		int T = Integer.parseInt(fs.nextLine());
		while(T-->0){
			String school =fs.nextLine();
			int n = Integer.parseInt(fs.nextLine());
			while(n-->0){
			int hrs=0;
			int pts=0;
			String data = fs.nextLine();
			String name =data.substring(0,data.indexOf(":"));
			System.out.println(name);
			String d = data.substring(data.indexOf(":")+1);
			d.replaceAll(","," ");
			while(){
				String drt=fs.next();
				int ptsd = Integer.parseInt(drt.charAt(1));
				double nrt = drt.charAt(0)*ptsd;
				
			}
			}
			}
			}
		}
	public static class Student implements Comparable<Student>{
		public String name;
		public double pts,gpa;
		public int hrs;
			public Student(String n, int h, double p){
				hrs=h;
				name=n;
				pts=p;
				gpa = p/h;
			}
			
			public int compareTo(Student other){
				if(Math.abs(gpa-other.gpa)<=.001){
					return hrs- other.hrs;
				} else {
					return (int) (1000000*(gpa-other.gpa));
				}
			}
	}
	
}

