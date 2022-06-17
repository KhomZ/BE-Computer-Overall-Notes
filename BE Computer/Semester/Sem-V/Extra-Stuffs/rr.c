#include<stdio.h>
int main()
{
int s[10],p[10],n,i,j,wi=0,w[10],t[10], st[10],tq,w1,tst=0;
int tt=0,tw=0;
float aw,at;
printf("enter no.of process");
scanf("%d",&n);
printf("\n enter time quanum");
scanf("%d",&tq);
printf("\n enter process&service time");
for(i=0;i<n;i++)
scanf("%d%d",&p[i],&s[i]);
for(i=0;i<n;i++)
st[i]=s[i];
tst=tst+s[i];
for(j=0;j<tst;j++)
for(i=0;i<n;i++)
{
if(s[i]>tq)
{
s[i]=s[i]-tq;
w1=w1+tq;
t[i]=w1;
w[i]=t[i]-st[i];
}
else if(s[i]!=0)
{
w1=w1+tq;
t[i]=w1;
w[i]=t[i]-st[i];
s[i]=s[i]-tq;
}
}
for(i=0;i<n;i++)
{
tw=tw+w[i];
tt=tt+t[i];
}
aw=tw/n;
at=tt/n;
printf("process\tst\twt\ttt");
for(i=0;i<n;i++)
printf("%d\t%d\t%d\t%d",p[i],st[i],w[i],t[i]);
printf("awt=%d",aw);
printf("att=%d",at);
}
