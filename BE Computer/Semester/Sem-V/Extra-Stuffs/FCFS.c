//FIRST COME FIRST SERVE SCHEDULING ALGORITHM
#include <stdio.h> 
struct process{ 
	int pid; 
	int bt; 
	int wt,tt; 
}p[10]; 

int main(){ 
	int i,n,totwt,tottt;
	float avgwt,avgtat; 
	
	printf("Enter the no of process \n"); 
	scanf("%d",&n); 
	for(i=1;i<=n;i++){ 
		p[i].pid=i; 
		printf("Enter the burst time for process %d\n",i); 
		scanf("%d",&p[i].bt); 
	} 
	p[1].wt=0; 
	p[1].tt=p[1].bt+p[1].wt; 
	i=2; 
	while(i<=n){ 
		p[i].wt=p[i-1].bt+p[i-1].wt; 
		p[i].tt=p[i].bt+p[i].wt; 
		i++; 
	}
	i=1; 
	totwt=tottt=0; 
	printf("\n Processid \t Burst Time\t Waiting Time \t Turn Around Time\n"); 
	while(i<=n){ 
		printf("\n\t%d\t %d \t\t %d \t\t %d",p[i].pid,p[i].bt,p[i].wt,p[i].tt); 
		totwt=p[i].wt+totwt; 
		tottt=p[i].tt+tottt; 
		i++; 
	} 
	avgwt=(float)totwt/n; 
	avgtat=(float)tottt/n; 
	printf("\nAverage Waiting Time=%.3f \nAverage Turn Around Time=%.3f \n",avgwt,avgtat); 
	
	return 0; 
}