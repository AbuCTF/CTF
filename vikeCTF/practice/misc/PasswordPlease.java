import java.util.Base64;
import java.util.Scanner;
import java.nio.charset.StandardCharsets;

class PasswordPlease{
	public static void main(String[] args){
		Scanner in = new Scanner(System.in);
		System.out.print("Password Please: ");
		String pw = in.nextLine();
		if(pw.equals("9CbJ3wDAuCG&")){
			Base64.Decoder d = Base64.getDecoder();
			System.out.println(new String(d.decode("Q1RGe3A0c3N3MHJkXzRjYzNwdDNkfQ=="), StandardCharsets.UTF_8));
		}
	}
}
