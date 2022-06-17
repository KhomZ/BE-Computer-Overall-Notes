// IMPLEMENTATION FIRST FIT MEMORY ALLOCATION ALGORITHM
#include <stdio.h>

int main(){
   
   int nop,nom;  //number of process and no of memory
   printf("\n=======================================================\n");
   printf("Demonstration of FIRST FIT memory allocation ALGORITHM");
   printf("\n=======================================================\n");

   printf("\nEnter number of processes:");
   scanf("%d",&nop);
   printf("\nEnter number of Memory blocks:");
   scanf("%d",&nom);
   
   int process_arr[nop],memory_arr[nom],i;
   for(i=0;i<nop;i++)
   {
     printf("Enter size of process %d:",i+1);
     scanf("%d",&process_arr[i]);      
   }
   for(i=0;i<nom;i++)
   {
     printf("Enter size of memory %d:",i+1);
     scanf("%d",&memory_arr[i]);      
   }
   int j;
   //FIRST FIT Allocation Algorithm
   for(i=0;i<nop;i++){
       for(j=0;j<nom;j++){
         if(memory_arr[j]>=process_arr[i]){
              printf("\nAllocating process %d (%dK) to memory: %dK\n"
                     "New memory hole after allocation: %dK\n\n",
                     i+1,process_arr[i],memory_arr[j],memory_arr[j]-process_arr[i]);
              memory_arr[j]-=process_arr[i];
                  break;            
         }
     }    
      if(j==nom)
         {
          printf("\nNot enough memory for process: %d(%dK)\n",i,process_arr[i]);
          break;
     }        
   }
  return 0;  
}