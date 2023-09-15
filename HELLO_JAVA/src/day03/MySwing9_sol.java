package day03;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JTextField;
import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import javax.swing.JTextArea;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.text.MessageFormat;

public class MySwing9_sol extends JFrame {

	private JPanel contentPane;
	private JTextField tf;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing9_sol frame = new MySwing9_sol();
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
	JTextArea ta;
	int strike;
	String message ="";
	private String com;
	public MySwing9_sol() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 306, 452);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lbl = new JLabel("맞출 수 : ");
		lbl.setBounds(54, 31, 57, 15);
		contentPane.add(lbl);
		
		tf = new JTextField();
		tf.setBounds(126, 28, 95, 21);
		contentPane.add(tf);
		tf.setColumns(10);
		
		JButton btn = new JButton("맞춰보기");
		
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myclick();
			}
		});
		
		
		btn.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
			}
		});
		btn.setBounds(54, 61, 167, 23);
		contentPane.add(btn);
		
		ta = new JTextArea();
		ta.setBounds(54, 106, 167, 250);
		contentPane.add(ta);
		randCom();
	}
	
	public void randCom() {
		int arr[]= {0,1,2,3,4,5,6,7,8,9};
		for (int i=0; i<100000; i++) {
			int rnd = (int)(Math.random()*9);
			int a = arr[0];
			arr[0]=arr[rnd];
			arr[rnd]=a;
		}
		com = arr[0] + "" + arr[1] + "" + arr[2];
		System.out.println(com);
		}
	
	public void myclick() {
		String mine = tf.getText();
		int s = getS(com, mine);
		int b = getB(com, mine);
		
		String str_old = ta.getText();
		String str_new = mine + "  " + s + "S  " + b + "B\n";
		ta.setText(str_old + str_new); 
		tf.setText("");
		
		if(s==3) {
			JOptionPane.showMessageDialog(null, mine + "맞췄습니다.");
		}
	}
	
	public int getS(String com, String mine) {
		int cnt=0;
		String m1 = mine.substring(0,1);
		String m2 = mine.substring(1,2);
		String m3 = mine.substring(2,3);
		
		String c1 = com.substring(0,1);
		String c2 = com.substring(1,2);
		String c3 = com.substring(2,3);
		
		if(c1.equals(m1)) cnt++;
		if(c2.equals(m2)) cnt++;
		if(c3.equals(m3)) cnt++;
		
		return cnt;
	}
	public int getB(String com, String mine) {
		int cnt=0;
		String m1 = mine.substring(0,1);
		String m2 = mine.substring(1,2);
		String m3 = mine.substring(2,3);
		
		String c1 = com.substring(0,1);
		String c2 = com.substring(1,2);
		String c3 = com.substring(2,3);
		
		if(c1.equals(m2) || c1.equals(m3)) cnt++;
		if(c2.equals(m1) || c2.equals(m3)) cnt++;
		if(c3.equals(m1) || c3.equals(m2)) cnt++;
		
		return cnt;
	}
}
