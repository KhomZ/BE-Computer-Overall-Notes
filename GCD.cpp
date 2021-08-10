// Program to find GCD or HCF of two numbers

// GCD (Greatest Common Divisor) or HCF (Highest Common Factor) of two numbers is the largest number that divides both of them. 
// For example GCD of 20 and 28 is 4 and GCD of 98 and 56 is 14.



// C++ program to find GCD of two numbers

#include <iostream>

using namespace std; 

// Recursive function to return gcd of a and b

int gcd(int a, int b) 

{

    // Everything divides 0 

    if (a == 0) 

       return b; 

    if (b == 0) 

       return a; 

  

    // base case 

    if (a == b) 

        return a; 

  

    // a is greater 

    if (a > b) 

        return gcd(a-b, b); 

    return gcd(a, b-a); 

}

  

// Driver program to test above function

int main() 

{

    int a = 98, b = 56; 

    cout<<"GCD of "<<a<<" and "<<b<<" is "<<gcd(a, b); 

    return 0; 

}

