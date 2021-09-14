import javax.swing.JOptionPane;

public class principal{
	public static void main(String[] args) {
		
		String v1 = JOptionPane.showInputDialog("Qual eh o valor 1?");
		int i = Interger.parseInt(v1);
		String v2 = JOptionPane.showInputDialog("Qual eh o valor 2");
		int n = Interger.parseInt(v2);
		
		int resultadoSoma;
		resultadoSoma = i + n;
		int resultadoSubtracao;
		resultadoSubtracao = i - n;
		int resultadoMultiplicacao;
		resultadoMultiplicacao = i * n;
		float resultadoDivisao;
		resultadoDivisao = i/n;
	
		JOptionPane.showMessageDialog(null, resultadoSoma + "" + resultadoSubtracao + "" + resultadoMultiplicacao + "" + String.format("%.2f", resultadoDivisao));
	} 
}
