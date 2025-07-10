/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package firstj2ee;
import java.sql.*;
/**
 *
 * @author COMP 76
 */
public class Firstj2ee {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        try
        {
            Class.forName("com.mysql.cj.jdbc.Driver");
            Connection con=DriverManager.getConnection("jdbc:mysql://localhost:3306/vk","root","");
           // String stq="insert into stud values(3,'pqr','babra')";
           // String stq="update stud set name='rohit' where id=3";
           // String stq="delete from stud where id=2";
            String stq="select *from stud";
            //String stq="select *from stud where id=1";
            //String stq="select name from stud";
            Statement st=con.createStatement();
            ResultSet rs=st.executeQuery(stq);
            
            while(rs.next())
            {
                System.out.println("id :"+rs.getInt(1));
                System.out.println("name :"+rs.getString("name"));
                System.out.println("city :"+rs.getString(3));
            }
            
        }
        catch(Exception e)
        {
            System.out.println("soory"+e);
        }
    }
    
}
