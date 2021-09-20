import java.io.File;
import java.util.ArrayList;
import java.util.ArrayDeque;
import java.util.Scanner;

public class PortalMaze {
	static char [][] maze;
	static final char TRIED = '7';
	static BPoint start;
	static ArrayDeque<Path> q = new ArrayDeque<Path>();
	static ArrayList<Portal> portalList = new ArrayList<Portal>();
	
	public static void readMaze(String fname) throws Exception{
		Scanner scan = new Scanner(new File(fname));
		String data = scan.nextLine();
		int r=Integer.parseInt(data.substring(0,2));
		int c=Integer.parseInt(data.substring(3,5));
		boolean con=false;
		maze=new char[r][c];
		for(int i=0;i<r;i++){
			data=scan.nextLine();
			for(int j=0;j<c;j++){
				maze[i][j]=data.charAt(j);
				if(data.charAt(j)=='S')
					start=new BPoint(i,j);
				if(isPortal(i,j)){
					for(int k =0;k<portalList.size();k++){
						if(portalList.get(k).ch==data.charAt(j)){
							portalList.set(k, new Portal(portalList.get(k).ch,portalList.get(k).row,portalList.get(k).col,i,j));
							con=true;
						}
					}
					if(!con)
						portalList.add(new Portal(data.charAt(j),i,j,100,100));
					con=false;
				}
			}
		}
	}
	
	public static boolean valid(int row, int colum, char[][] maze){
		if(row>=0 && row<=maze.length-1 && colum>=0 && colum<=maze[0].length-1 && maze[row][colum]=='.')
			return true;
		return false;
		
	}
	
	public static void printMaze(char [][] m){
		for(int i =0;i<m.length;i++){
			for(int j=0;j<m[0].length;j++){
				System.out.print(m[i][j]);
			}
			System.out.println();
		}
	}
	
	public static boolean isPortal(int row, int col){
		if(maze[row][col]!='.'&&maze[row][col]!='#'&&maze[row][col]!='S'&&maze[row][col]!='F')
			return true;
		return false;
		
	}
	
	public static Portal getPortal(int r, int c){
		for(int i =0;i<portalList.size();i++){
			if(portalList.get(i).row==r&&portalList.get(i).col==c)
				return portalList.get(i);
		}
		return null;
	}
	
	public static ArrayList<BPoint> copyPath(ArrayList<BPoint> orig){
		ArrayList<BPoint> temp=new ArrayList<BPoint>();
		for(int i =0;i<orig.size();i++)
			temp.add(orig.get(i));
		return temp;
			
		
	}
	
	public static char[][] copyMaze(char[][] orig){
		char [][] temp=new char[orig.length][orig[0].length];
		for(int i=0;i<orig.length;i++){
			for(int j=0;j<orig[0].length;j++){
				temp[i][j]=orig[i][j];
			}
		}
		return temp;
	}
	
	public static void solveMaze() throws Exception{
		boolean isPath=false;
		ArrayList<BPoint> points = new ArrayList<BPoint>();
		points.add(start);
		q.add(new Path(maze,points));
		Path cur = null;
		while(!q.isEmpty()){
			cur=q.poll();
			if(maze[cur.p.get(cur.p.size()-1).row][cur.p.get(cur.p.size()-1).col]=='F'){
				isPath=true;
				break;
			}
			else if(isPortal(cur.p.get(cur.p.size()-1).row,cur.p.get(cur.p.size()-1).col)){
				Portal temp=getPortal(cur.p.get(cur.p.size()-1).row,cur.p.get(cur.p.size()-1).col);
				if(cur.p.get(cur.p.size()-1).row==temp.row && cur.p.get(cur.p.size()-1).col==temp.col){
					cur.p.add(new BPoint(temp.row,temp.col));
					cur.pused+=temp.ch;
					q.add(cur);
				}
				else{
					cur.p.add(new BPoint(temp.row2,temp.col2));
					cur.pused+=temp.ch;
					q.add(cur);
				}
			}
			else{
			if(valid(cur.p.get(cur.p.size()-1).row,cur.p.get(cur.p.size()-1).col+1,cur.m)){
				char [][] tem=copyMaze(cur.m);
				tem[cur.p.get(cur.p.size()-1).row][cur.p.get(cur.p.size()-1).col+1]=' ';
				ArrayList<BPoint> temp=copyPath(cur.p);
				temp.add(new BPoint(cur.p.get(cur.p.size()-1).row,(cur.p.get(cur.p.size()-1).col+1)));
				q.add(new Path(tem,temp));
			}
			if(valid(cur.p.get(cur.p.size()-1).row,cur.p.get(cur.p.size()-1).col-1,cur.m)){
				char [][] tem=copyMaze(cur.m);
				tem[cur.p.get(cur.p.size()-1).row][cur.p.get(cur.p.size()-1).col-1]=' ';
				ArrayList<BPoint> temp=copyPath(cur.p);
				temp.add(new BPoint(cur.p.get(cur.p.size()-1).row,(cur.p.get(cur.p.size()-1).col-1)));
				q.add(new Path(tem,temp));
			}
			if(valid(cur.p.get(cur.p.size()-1).row+1,cur.p.get(cur.p.size()-1).col,cur.m)){
				char [][] tem=copyMaze(cur.m);
				tem[cur.p.get(cur.p.size()-1).row+1][cur.p.get(cur.p.size()-1).col]=' ';
				ArrayList<BPoint> temp=copyPath(cur.p);
				temp.add(new BPoint(cur.p.get(cur.p.size()-1).row+1,(cur.p.get(cur.p.size()-1).col)));
				q.add(new Path(tem,temp));
			}
			if(valid(cur.p.get(cur.p.size()-1).row-1,cur.p.get(cur.p.size()-1).col,cur.m)){
				char [][] tem=copyMaze(cur.m);
				tem[cur.p.get(cur.p.size()-1).row-1][cur.p.get(cur.p.size()-1).col]=' ';
				ArrayList<BPoint> temp=copyPath(cur.p);
				temp.add(new BPoint(cur.p.get(cur.p.size()-1).row-1,(cur.p.get(cur.p.size()-1).col)));
				q.add(new Path(tem,temp));
			}
			}
		
		}
		printMaze(cur.m);
		if(!isPath)
			System.out.println("There is no path");
		else{
			System.out.println("Distance: "+cur.p.size()+" squares");
			System.out.println("Portals Used: "+cur.pused);
			printMaze(cur.m);			
		}
			
	}
	
	public static void main(String[] args) throws Exception{
		readMaze("prob18_1.in");
		solveMaze();
	}
	
	private static class BPoint{
		int row,col;
		
		BPoint(int r, int c){
			row=r;
			col=c;
		}
		
		public String toString(){
			return(row+" "+col);
		}
		
	}
	
	private static class Portal{
		int row,col,row2,col2;
		char ch;
		
		Portal(char ch,int r,int c,int r2,int c2){
			row=r;
			col=c;
			row2=r2;
			col2=c2;
			this.ch=ch;
			
		}
		
		public String toString(){
			return(ch+" "+row+" "+col+" "+row2+" "+col2);
		}
		
	}
	
	private static class Path{
		ArrayList<BPoint> p = new ArrayList<BPoint>();
		char[][] m;
		String pused="";
		
		Path(char [][]ma,ArrayList<BPoint> p){
			m=copyMaze(ma);
			this.p.addAll(p);
		}
		
		public String toString(){
			System.out.println(p.get(p.size()-1));
			return "portals used "+pused;
		}
		
	}	
}
