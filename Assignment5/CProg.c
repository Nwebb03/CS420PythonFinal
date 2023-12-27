#include <stdio.h>
#include <stdlib.h>
int main(int argc, char *argv[]) {
    int *arr;
    int numEntries;

    //For each entry allocate memory
    numEntries = argc - 1;
    arr = (int *)malloc((numEntries) * sizeof(int));
    
    //Iterate through array and threshold
    for (int i = 0; i < numEntries; i++) {
        arr[i] = atoi(argv[i + 1]);
    }

    for (int i = 0; i < numEntries; i++) {
        if(arr[i] > 170){
            printf("%d ", 255);
        }
        else{
            printf("%d ", 0);
        }
    }
    printf("\n");
    //Deallocate memory
    free(arr);

    return 0;
}