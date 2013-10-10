#include <stdio.h>

void fizzbuzz(int start=1, int end=100) {
     int i = start;
     for (i=start;i<=end; i++) {
          if ((i%5 == 0) && (i % 3 ==0)) {
               printf("fizzbuzz\n");
          }
          else if  (i % 5 == 0){
               printf("buzz\n");
          }
          else if (i%3==0) {
               printf("fizz\n");
          }
          else{
               printf("%d\n", i);
          }
}
}

int main() { 
     fizzbuzz(1,100);
     return 0;
}
 
