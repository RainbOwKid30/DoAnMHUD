import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Arrays;

public class ChuyenDichDongUI {
    private JFrame frame;
    private JTextField textBeforeField;
    private JTextField keyField;
    private JButton encryptButton;
    private JTextArea resultArea;

    public ChuyenDichDongUI() {
        frame = new JFrame("ChuyenDichDong UI");
        frame.setLayout(new FlowLayout());

        JLabel textBeforeLabel = new JLabel("Text Before:");
        textBeforeField = new JTextField(15);
        frame.add(textBeforeLabel);
        frame.add(textBeforeField);

        JLabel keyLabel = new JLabel("Key:");
        keyField = new JTextField(5);
        frame.add(keyLabel);
        frame.add(keyField);

        encryptButton = new JButton("Encrypt/Decrypt");
        frame.add(encryptButton);

        resultArea = new JTextArea(10, 30);
        frame.add(resultArea);

        encryptButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String textBefore = textBeforeField.getText();
                String key = keyField.getText();
                String result = "";
                
                if (e.getActionCommand().equals("Encrypt/Decrypt")) {
                    if (textBefore.contains("z")) {
                        result = decrypt(textBefore, key);
                    } else {
                        result = encrypt(textBefore, key);
                    }
                }

                resultArea.setText("Result: " + result);
            }
        });

        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.pack();
        frame.setVisible(true);
    }

    private String encrypt(String text, String key) {
        //Tính số cột dựa trên độ dài của chìa khóa
        int numColumns = key.length();
        //Tính số hàng trong mảng

        int numRows = (int) Math.ceil((double) text.length() / numColumns);
        //Tạo mảng 2 chiều
        char[][] array = new char[numRows][numColumns];
        int a = 0;//Khai báo biến đếm = 0
        for (int i = 0; i < numRows; i++) {
            //Nếu biến đếm > độ dài của mảng thì thêm ‘z’ và tăng biến đếm
            for (int j = 0; j < numColumns; j++) {
                if (a < text.length()) {
                    array[i][j] = text.charAt(a++);
                } else {//Ngược lại gán ký tự tại index vào mảng và tăng biến đếm
                    array[i][j] = 'z';
                }
            }
        }//Chuyển đổi key thành mảng ký tự
        
        char[] keyChars = key.toCharArray();
        Arrays.sort(keyChars);//Sắp xếp key
         //Tạo biến để lưu trữ kết quả
        StringBuilder stringBuilder = new StringBuilder();
        for (char keyChar : keyChars) {//Duyệt các phần tử trong mảng keyChars
            int numkey = key.indexOf(keyChar);//Tạo biến gán bằng vị trí của ký tự ch
            for (int i = 0; i < numRows; i++) {
                stringBuilder.append(array[i][numkey]);//Nối các ký tự sau khi được mã hóa
            }
        }
        return stringBuilder.toString();//Xuất ra chuỗi được mã hóa
    }

    private String decrypt(String text, String key) {
        int numColumns = key.length();//Tính số cột dựa trên độ dài của chìa khóa
        int numRows = (int) Math.ceil((double) text.length() / numColumns);//Tính số hàng trong mảng
        char[][] array = new char[numRows][numColumns];//Tạo mảng 2 chiều
        char[] keyChars = key.toCharArray();//Chuyển đổi key thành mảng ký tự
        int[] keyOrder = new int[numColumns];
        Arrays.sort(keyChars);//Sắp xếp key
        for (int i = 0; i < numColumns; i++) {
            keyOrder[i] = key.indexOf(keyChars[i]);
        }

        int a = 0;//Khai báo biến đếm = 0
        for (int keyIndex : keyOrder) {
            for (int i = 0; i < numRows; i++) {
                array[i][keyIndex] = text.charAt(a++);
            }
        }

        StringBuilder stringBuilder = new StringBuilder();
        for (int i = 0; i < numRows; i++) {
            for (int j = 0; j < numColumns; j++) {
                stringBuilder.append(array[i][j]);
            }
        }
        return stringBuilder.toString();
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                new ChuyenDichDongUI();
            }
        });
    }
}
