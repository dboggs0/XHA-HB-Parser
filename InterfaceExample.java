import java.util.ArrayList;

public class InterfaceScratch{
   public static void main(String[] args){
      ArrayList<Vehicle> list = new ArrayList();
      Car buick = new Car("Buick", "Road Master", 1967);
      list.add(buick);
   
      Car toyota = new Car("Toyota","Land Cruiser",2008);
      list.add(toyota);
      
      Motorcycle honda = new Motorcycle("Honda", "Goldwing", 2016);
      list.add(honda);
      
      for (Vehicle v:list){
         System.out.println(v.getSpeed());
      }   
   }
}

abstract class Vehicle implements wheels{
   String make;
   String model;
   int year;
   
   public abstract int getNumberOfWheels();
   
   public abstract int getSpeed();
}

class Car extends Vehicle {

   Car(String make, String model, int year){
      this.make = make;
      this.model = model;
      this.year = year;
   }
   public int getNumberOfWheels(){
      return 4;
   }
   
   public int getSpeed(){
      return 110;
   }
}

class Motorcycle extends Vehicle {

   Motorcycle(String make, String model, int year){
      this.make = make;
      this.model = model;
      this.year = year;
   }
   public int getNumberOfWheels(){
      return 2;
   }
   
   public int getSpeed(){
      return 150;
   }
}

interface wheels{
   public int getNumberOfWheels();
   
   public int getSpeed();
}
