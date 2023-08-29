package day03;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import javax.swing.JTextArea;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.text.MessageFormat;

public class MySwing09 extends JFrame {

	private JPanel contentPane;
	private JTextField tf;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing09 frame = new MySwing09();
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
	public MySwing09() {
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
		
		int arr[]= {0,1,2,3,4,5,6,7,8,9};
		for (int i=0; i<100000; i++) {
			int rnd = (int)(Math.random()*9);
			int a = arr[0];
			arr[0]=arr[rnd];
			arr[rnd]=a;
		}
		int comNum1 = arr[0];
		int comNum2 = arr[1];
		int comNum3 = arr[2];
		
		String comStrNum1 = String.valueOf(comNum1);
		String comStrNum2 = String.valueOf(comNum2);
		String comStrNum3 = String.valueOf(comNum3);
		String com = comStrNum1 + comStrNum2 + comStrNum3;
		
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myclick(com);
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
		
	}
	
	public void myclick(String com) {
		System.out.println(com);
		String numStr = tf.getText();
		tf.setText("");
		
		strike = getS(com, numStr);
		int ball = getB(com, numStr);
		
		message += MessageFormat.format("{0}\t{1}S{2}B", numStr, strike, ball);
		message +="\n";
		
		if(strike==3) {
			message+="정답입니다.";
		}
		
		ta.setText(message);
	}
	
	public int getS(String mine, String com) {
		int cnt = 0;
		
		String numStr1 = mine.substring(0,1);
		String numStr2 = mine.substring(1,2);
		String numStr3 = mine.substring(2,3);
		
		String numComStr1 = com.substring(0,1);
		String numComStr2 = com.substring(1,2);
		String numComStr3 = com.substring(2,3);
		
		if(numStr1.equals(numComStr1)) cnt += 1;
		if(numStr2.equals(numComStr2)) cnt += 1;
		if(numStr3.equals(numComStr3)) cnt += 1;
		
		return cnt;
	}
	public int getB(String mine, String com) {
		int cnt = 0;

		String numStr1 = mine.substring(0,1);
		String numStr2 = mine.substring(1,2);
		String numStr3 = mine.substring(2,3);
		
		String numComStr1 = com.substring(0,1);
		String numComStr2 = com.substring(1,2);
		String numComStr3 = com.substring(2,3);
		
		if(numStr1.equals(numComStr2) || numStr1.equals(numComStr3)) cnt += 1;
		if(numStr2.equals(numComStr3) || numStr2.equals(numComStr1)) cnt += 1;
		if(numStr3.equals(numComStr1) || numStr3.equals(numComStr2)) cnt += 1;
		
		return cnt;
	}
}
