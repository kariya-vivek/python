/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package callablestatmentvk;

/**
 *
 * @author COMP 76
 */
public class Callablestatmentvk {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        try
        {
          Class.forName("com.mysql.cj.jdbc.Driver");
        }
        catch(Exception e)
        {
            System.err.println("error"+e);
        }
        
    }
    
}
