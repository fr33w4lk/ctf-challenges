#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>


int main(int argc, char* argv[]){

	unsigned char* submit;
	submit = "******";

	int match = 0;

	while (match != 6) {
			printf(".");

			int i;
			int j = 0;
			match = 0;

			// generate lotto numbers
			int fd = open("/dev/urandom", O_RDONLY);
			unsigned char lotto[6];
			unsigned char* lotto1 = "AA)AAA";

			//if(read(fd, lotto, 6) != 6){
			//	printf("error2. tell admin\n");
			//	exit(-1);
			//}
			for(i=0; i<6; i++){
				lotto[i] = (lotto1[i] % 45) + 1;		// 1 ~ 45
				//printf("%x", lotto[i]);
			}
			close(fd);
			//exit(0);
			// calculate lotto score
			for(i=0; i<6; i++){
				for(j=0; j<6; j++){
					if(lotto[i] == submit[j]){
						match++;
					}
				}
			}

	}
	printf("matched");
}

