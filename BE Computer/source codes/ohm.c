#include <stdio.h>
#include <conio.h>

void main(){
clrscr();
float I,R,V;
printf("Enter the value of current, I=");
scanf("%f",&I);

printf("Enter the value of Resistance, R=");
scanf("%f",&R);

V = I*R;
printf("The required voltage, V=");
printf("%f",V);
getch();
}