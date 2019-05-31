#include <assert.h> 
#include <stdio.h>
#include <stdint.h>

int main(int argc, char **argv) {
	assert(argc == 3);
	int captcha = atoi(argv[1]);
	int time = atoi(argv[2]);

	int values[8];

	srand(time);
	for (int i = 0; i < 8; i++) {
		values[i] = rand();
	}

	int total = values[1] + values[2] - values[3] + values[4] + values[5] - values[6] + values[7];

	int canary = captcha - total;

	printf("0x%x\n", canary);
	return 0;
}
