package day03;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySwing04 extends JFrame {

	private JPanel contentPane;
	private JTextField tfMine;
	private JTextField tfCom;
	private JTextField tfResult;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing04 frame = new MySwing04();
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
	public MySwing04() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 217, 284);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lblMine = new JLabel("나 : ");
		lblMine.setBounds(44, 26, 57, 15);
		contentPane.add(lblMine);
		
		JLabel lblCom = new JLabel("컴 : ");
		lblCom.setBounds(44, 77, 57, 15);
		contentPane.add(lblCom);
		
		JLabel lblResult = new JLabel("결과 : ");
		lblResult.setBounds(44, 133, 57, 15);
		contentPane.add(lblResult);
		
		tfMine = new JTextField();
		tfMine.setBounds(113, 23, 46, 21);
		contentPane.add(tfMine);
		tfMine.setColumns(10);
		
		tfCom = new JTextField();
		tfCom.setColumns(10);
		tfCom.setBounds(113, 74, 46, 21);
		contentPane.add(tfCom);
		
		tfResult = new JTextField();
		tfResult.setColumns(10);
		tfResult.setBounds(113, 130, 46, 21);
		contentPane.add(tfResult);
		
		
		JButton btn = new JButton("게임하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myclick();
			}
		});
		btn.setBounds(44, 193, 115, 23);
		contentPane.add(btn);
	}
	
	public void myclick() {
		String mine = tfMine.getText();
		String com="";
		String result = "";
		
		double rnd = Math.random();
		if(rnd>0.5) {
			com="홀";
		}else {
			com="짝";
		}
		if(mine.equals(com)) {
			result ="이김";
		}else {
			result="짐";
		}
		
		tfCom.setText(com);
		tfResult.setText(result);
	}
}
