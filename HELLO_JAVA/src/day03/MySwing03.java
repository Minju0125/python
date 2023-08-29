package day03;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JButton;
import javax.swing.JTextArea;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySwing03 extends JFrame {

	private JPanel contentPane;
	private JTextField tf;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing03 frame = new MySwing03();
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
	
	JTextArea TA = new JTextArea();
	public MySwing03() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 373, 451);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lb = new JLabel("출력단수");
		lb.setBounds(71, 47, 71, 18);
		contentPane.add(lb);
		
		tf = new JTextField();
		tf.setBounds(154, 46, 116, 21);
		contentPane.add(tf);
		tf.setColumns(10);
		
		JButton btn = new JButton("출력하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myclick();
			}
		});
		btn.setBounds(71, 77, 211, 30);
		contentPane.add(btn);
		
		
		TA.setBounds(71, 129, 211, 230);
		contentPane.add(TA);
	}

	public void myclick() {
		String inputNum = tf.getText();
		int num = Integer.parseInt(inputNum); 
		String text="";
		for(int i=1; i<10; i++) {
			text += inputNum + "*" + i + "=" + num*i + "\n";
		}
		TA.setText(text);
	}
}
