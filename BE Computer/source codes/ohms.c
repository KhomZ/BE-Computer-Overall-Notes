#include <stdio.h>
#include <conio.h>

void main(){
FILE *fpt;

int i,r;
float v,ic;

fpt = fopen("Ohms.c","w");
printf("enter the values of v and r");
scanf("%f%d", &v,&r);
for(i=0;i<10;i++)
{
ic = v/r;
printf("v=%.2f\ti=%.2f\n",v,ic);
fprintf(fpt,"%.2f\t%.2f\n",v,ic);
v=v+5;
}
fclose(fpt);
getch();
}