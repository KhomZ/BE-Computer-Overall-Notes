//NON PREEMPTIVE SHORTEST JOB FIRST SCHEDULING ALGORITHM
#include <stdio.h> 
struct process{ 
	int pid; 
	int bt; 
	int wt; 
	int tt; 
}p[10],temp; 

int main(){ 
	int i,j,n,totwt,tottt; 
	float avgwt,avgtat; 
	
	printf("\nEnter the number of process:\t"); 
	scanf("%d",&n); 
	for(i=1;i<=n;i++){ p[i].pid=i; 
		printf("\nEnter the burst time for process: %d \n",i); 
		scanf("%d",&p[i].bt); 
	} 
	for(i=1;i<n;i++){ 
		for(j=i+1;j<=n;j++){ 
			if(p[i].bt>p[j].bt){ 
				temp.pid=p[i].pid; 
				p[i].pid=p[j].pid; 
				p[j].pid=temp.pid; 
				temp.bt=p[i].bt; 
				p[i].bt=p[j].bt; 
				p[j].bt=temp.bt; 
			}
		}
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
	printf("\nProcess id \tBurst Time \t Waiting Time \t Turn around time"); 
	while(i<=n){ 
		printf("\n\t%d \t\t%d \t\t%d \t\t%d\n",p[i].pid,p[i].bt,p[i].wt,p[i].tt); 
		totwt=p[i].wt+totwt; 
		tottt=p[i].tt+tottt; 
		i++; 
	} 
	avgwt=(float)totwt/n; 
	avgtat=(float)tottt/n; 
	printf("\nAverage Waiting Time: %.3f\nAverage Turnaround Time:%.3f\n",avgwt,avgtat); 
	
	return 0; 
}
