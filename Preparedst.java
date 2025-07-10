
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package preparedst;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.Scanner;

/**
 *
 * @author COMP 76
 */
public class Preparedst {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        try
        {
            Class.forName("com.mysql.cj.jdbc.Driver");
            Connection con=DriverManager.getConnection("jdbc:mysql://localhost:3306/vk","root","");
           // String stq="insert into prepadstud values(?,?,?)"; 
            String stq="update prepadstud set name=?,city=? where id=?";
            PreparedStatement pst=con.prepareStatement(stq);
            Scanner sc=new Scanner(System.in);
            System.out.print("enter your name=");
            String n=sc.next();
            System.out.println("");
            System.out.print("enter your city=");
            String c=sc.next();
            System.out.print("enter your id=");
            int i=sc.nextInt();
             System.out.println(""); 
             pst.setString(1,n);
             pst.setString(2,c);
             pst.setInt(3,i);
             pst.executeUpdate();
           // String stq="update prepadstud set name='rohit' where id=3";
           // String stq="delete from prepadstud where id=2";
            /*String stq="select *from stud";
            //String stq="select *from prepadstud where id=1";
            //String stq="select name from prepadstud";
           
           
            
            while(rs.next())
            {
                System.out.println("id :"+rs.getInt(1));
                System.out.println("name :"+rs.getString("name"));
                System.out.println("city :"+rs.getString(3));
            }*/
            
        }
        catch(Exception e)
        {
            System.out.println("soory"+e);
        }
    }
    
}
