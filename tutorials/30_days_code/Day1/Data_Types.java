/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package data_types;

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;


/**
 *
 * @author michal.freygant
 */
public class Data_Types {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        int i = 4;
        double d = 4.0;
        String s = "HackerRank ";
        
        int i2 = 0;
        double d2 = 0.0;
        String s2 = "";
		
        Scanner scan = new Scanner(System.in);
        while(scan.hasNext()){
            i2 = scan.nextInt();
            d2 = scan.nextDouble();
            scan.nextLine();
            s2 = scan.nextLine();
            break;
        }
        
        System.out.println(i + i2);
        System.out.println(d + d2);
        System.out.println(s  +  s2);
        scan.close();
        
    }
    
}
