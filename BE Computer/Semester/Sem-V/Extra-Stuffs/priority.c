#include <stdio.h>
#include <stdlib.h> 
struct process
{
	int pid;
	int wt,tt,bt,prior;
}p[100],temp; 
int main()
{
	int tottt,totwt;
	float avgtt,avgwt;
	int i,j,n; 
	printf("\nEnter Number of process:\t"); 
	scanf("\n%d",&n); 
	for(i=1;i<=n;i++)
	{
		p[i].pid=i;
		printf("\nEnter %d Burst Time:\t",i); 
		scanf("\n%d",&p[i].bt); 
		printf("\nEnter %d priority:\t",i); 
		scanf("\n%d",&p[i].prior);
	}
for(i=1;i<=n;i++)
{
	for(j=i+1;j<=n;j++)
	{
		if(p[i].prior > p[j].prior)
		{
			temp=p[j];
			p[j]=p[i];
			p[i]=temp;
		} 
	} 
}
p[1].wt=0;
p[1].tt=p[1].bt+p[1].wt;
i=2;
while(i<=n)
{
	p[i].wt=p[i-1].tt; 
	p[i].tt=p[i].bt+p[i].wt; 
	i++; 
}	
	totwt=tottt=0;
	i=1;
	printf("\n\t===============================");
	printf("\n\tPSSID\tBT\t Priority \t WT\tTT");
	printf("\n\t===============================");
	while(i<=n)
	{
		printf("\n\t%d\t%d\t%d\t%d\t%d\t",p[i].pid,p[i].bt,p[i].prior,p[i].wt,p[i].tt);
		totwt=p[i].wt+totwt;
		tottt=p[i].tt+tottt;
		i++;
	}
	avgwt=(float)totwt/n;
	avgtt=(float)tottt/n;
	printf("\n\n\n\tAVGWT\tAVGTT\n");
	printf("\n\t%.3f\t%.3f\n",avgwt,avgtt);
}
