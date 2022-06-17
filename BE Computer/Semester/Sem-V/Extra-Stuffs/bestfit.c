// IMPLEMENTATION BEST FIT MEMORY ALLOCATION ALGORITHM
#include <stdio.h>
int main(){
   int nop,nom;  
   printf("\n=======================================================\n");
   printf("Demonstration of BEST FIT memory allocation ALGORITHM");
   printf("\n=======================================================\n");

   printf("Enter number of processes:");
   scanf("%d",&nop);
   printf("Enter number of Memory blocks:");
   scanf("%d",&nom);
   
   int process_arr[nop];
   struct mem{
          int id;
          int size;
   }memory_arr[nom];
   int i;
   for(i=0;i<nop;i++)
   {
     printf("Enter size of process %d:",i+1);
     scanf("%d",&process_arr[i]);      
   }
   for(i=0;i<nom;i++)
   {
     printf("Enter size of memory %d:",i+1);
     scanf("%d",&memory_arr[i].size);   
     memory_arr[i].id=i+1;   
   }
   //sorting of memory in increasing order
   int j;
   for(i=0;i<nom;i++)
      for(j=i+1;j<nom;j++)
        if(memory_arr[i].size > memory_arr[j].size)
        {
          struct mem t=memory_arr[i];
          memory_arr[i]=memory_arr[j];
          memory_arr[j]=t;                               
        }
   /* printf("Memory hole in order\n");
    for(i=0;i<m;i++){
      printf("ID memory_arr[%d]=%d\n",i,memory_arr[i].id);
      printf("Size memory_arr[%d]=%d\n",i,memory_arr[i].size);
    }
  */

  //Best Fit algorithm
    for(i=0;i<nop;i++){
       for(j=0;j<nom;j++){
         if(memory_arr[j].size>=process_arr[i]){
              printf("\nAllocating process %d (%dK) to memory: %d (%dK)\n" 
                     "New memory hole after allocation: %dK\n\n",
                     i+1,process_arr[i],memory_arr[j].id,memory_arr[j].size,(memory_arr[j].size-process_arr[i])); 
              memory_arr[j].size-=process_arr[i];
              break;            
         }   //end of if
    }   //end of j loop
     //if not enough memory hole is present 
    if(j==nom)
    {
        printf("Not enough memory for process: %d(%dK)",i,process_arr[i]);
        break;
    }        
   } //end of i loop
  return 0;  
}
