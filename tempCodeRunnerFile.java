package com.masai;
public class A {
static{
System.out.println("inside static block of A class");
//we can write any type of code inside the static block
A a1= new A();
a1.funA();
}
public void funA() {
System.out.println("inside funA of A");
}
}
