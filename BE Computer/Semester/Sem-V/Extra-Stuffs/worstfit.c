// IMPLEMENTATION WORST FIT MEMORY ALLOCATION ALGORITHM
#include <stdio.h>
int main(){
   
   int nop,nom;  //no of process and memory
   printf("\n=======================================================\n");
   printf("Demonstration of WORST FIT memory allocation ALGORITHM");
   printf("\n=======================================================\n");
   printf("Enter number of processes:");
   scanf("%d",&nop);
   printf("Enter number of Memory blocks:");
   scanf("%d",&nom);
   
   int process_arr[10];
   struct mem{
          int id;
          int size;
   }memory_arr[10];
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
   //Sorting of memory in decending order
   int j;
   for(i=0;i<nom;i++)
      for(j=i+1;j<nom;j++)
        if(memory_arr[i].size < memory_arr[j].size)
        {
          struct mem t=memory_arr[i];
          memory_arr[i] = memory_arr[j];
          memory_arr[j] = t;                               
        }
   /* 
    printf("Memory hole in order\n");
    for(i=0;i<nom;i++){
     // printf("ID memory_arr[%d]=%d\n",i,memory_arr[i].id);
      printf("Size memory_arr[%d]=%d\n",i,memory_arr[i].size);
    }
    */

    //WORST FIT ALLOCATION ALGORITHM
   for(i=0;i<nop;i++){
       for(j=0;j<nom;j++){
         if(memory_arr[j].size>=process_arr[i]){
              printf("\nAllocating process %d (%dK) to memory: %d (%dK)\n"
                     "New memory hole after allocation: %dK\n\n",
                     i+1,process_arr[i],j+1,memory_arr[j].size,(memory_arr[j].size-process_arr[i]));
              memory_arr[j].size-=process_arr[i];
                 
              break;              
         }  //end of if
     }   //end of j loop
    if(j==nom)
    {
      printf("Not enough memory for process: %d(%dK)\n",i,process_arr[i]);
      break;
    }        
   } //end of i loop
  return 0;  
} //end of main