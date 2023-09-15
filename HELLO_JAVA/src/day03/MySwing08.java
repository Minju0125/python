package day03;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextField;
import javax.swing.JLabel;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySwing08 extends JFrame {

	private JPanel contentPane;
	private JTextField tf1;
	private JTextField tf2;
	private JTextField tf3;
	private JTextField tf4;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing08 frame = new MySwing08();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	
	
	public MySwing08() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 635, 151);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		tf1 = new JTextField();
		tf1.setBounds(50, 43, 74, 21);
		contentPane.add(tf1);
		tf1.setColumns(10);
		
		JLabel lbl1 = new JLabel("에서");
		lbl1.setBounds(136, 46, 33, 15);
		contentPane.add(lbl1);
		
		tf2 = new JTextField();
		tf2.setColumns(10);
		tf2.setBounds(181, 43, 74, 21);
		contentPane.add(tf2);
		
		JLabel lbl2 = new JLabel("까지");
		lbl2.setBounds(267, 46, 33, 15);
		contentPane.add(lbl2);
		
		tf3 = new JTextField();
		tf3.setColumns(10);
		tf3.setBounds(326, 43, 74, 21);
		contentPane.add(tf3);
		
		JButton btn = new JButton("배수의 합은");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myclick();
			}
		});
		btn.setBounds(412, 41, 97, 23);
		contentPane.add(btn);
		
		tf4 = new JTextField();
		tf4.setColumns(10);
		tf4.setBounds(521, 42, 74, 21);
		contentPane.add(tf4);
	}
	
	public void myclick() {
		String num1 = tf1.getText();
		String num2 = tf2.getText();
		String num3 = tf3.getText();
		
		int intNum1 = Integer.parseInt(num1);
		int intNum2 = Integer.parseInt(num2);
		int intNum3 = Integer.parseInt(num3);
		
		int sum = 0;
		for(int i=intNum1; i<=intNum2; i++) {
			if(i % intNum3 ==0) {
				sum+=i;
			}
		}
		tf4.setText(String.valueOf(sum));
	}
}
