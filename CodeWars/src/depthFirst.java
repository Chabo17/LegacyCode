import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class depthFirst {

	public static void main(String[] args) throws FileNotFoundException {
		Scanner fs = new Scanner(new File("src/tree"));
		int n = fs.nextInt();
		String temp = "";
		node root = null;
		node[] tree = new node[n];
		String[] val = new String[n * 3];
		for (int i = 0; i < n * 3; i++) {// finding all the values
			val[i] = fs.next();
		}
		for (int i = 0, j = 0; i < val.length; i += 3) {// making all of the mini trees
			tree[j] = new node(val[i], new node(val[i + 1], null, null),new node(val[i + 2], null, null));
			j++;
		}
		for (int i = 0; i < n * 3; i++) {// finding root value
			for (int k = i + 1; k < val.length; k++) {
				if ((val[i] != null && val[k] != null) && val[i].equals(val[k])) {
					val[i] = null;
					val[k] = null;
				}
			}
		}
		for (int i = 0; i < val.length; i += 3) {// getting the root value
			if (val[i] != null) {
				temp = val[i];
			}
		}
		for (int i = 0; i < tree.length; i++) {// making the root
			if (tree[i] != null) {
				if (temp.equals(tree[i].value))
					root = tree[i];
			}
		}
		for (node node : tree) {// making the final tree
			for (node child : tree) {
				if (node != null && child != null) {
					if (node.left.value.equals(child.value)) {
						node.left = child;
					} else if (node.right.value.equals(child.value)) {
						node.right = child;
					}
				}
			}
		}
		root.postOrder(root);
	}

	public static class node {
		public String value;
		node left, right, parent;

		public node(String value, node left, node right) {
			this.value = value;
			this.left = left;
			this.right = right;
		}

		public static void postOrder(node n) {
			if (n == null || n.value.equals("."))
				return;
			postOrder(n.left);
			postOrder(n.right);
			System.out.print(n);
			// if( this.left ) text += this.left.traverse();
			// if( this.right ) text += this.right.traverse();
		}

		public String toString() {
			return value.toString();
		}
	}
}