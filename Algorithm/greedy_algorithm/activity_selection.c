/* Activity Selection Problem
 * Problem: get your money's worth out of a carnival!
 * Goal: ride as many rides as possible.
 * Input: start & end time of each rides
 * Output: the max number of rides who you ride.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define INPUT_SIZE 6
#define NUM_SIZE 100

typedef struct
{
	int numOfRides;
	int starttime[INPUT_SIZE];
	int endtime[INPUT_SIZE];
} Datas;
void initDatas(Datas *data)
{
	data->numOfRides = 0;
}
void printInput(char **input)
{
	printf("inputs: \n");
	for(int i = 0; i < INPUT_SIZE; i++)
		printf("\t%d: %s", i+1, input[i]);
}
void preprocessInput(char **input, Datas *data)
{
	int len = 0;
	for(int i = 0; i < data->numOfRides; i++)
	{
		int j = 0, k = 0;
		char tmp[NUM_SIZE] = {0, };
		while(input[i][k] != ' ')
			tmp[j++] = input[i][k++];
		data->starttime[i] = atoi(tmp);

		j = 0; k++;
		while(input[i][k] != '\n')
			tmp[j++] = input[i][k++];
		tmp[j] = '\0';
		data->endtime[i] = atoi(tmp);
	}
}
void swap(int *num1, int *num2)
{
	*num1 ^= *num2;
	*num2 ^= *num1;
	*num1 ^= *num2;
}
int partition(Datas *data, int left, int right)
{
	int pivot = left;

	return pivot;
}
void quickSort(Datas *data, int left, int right)
{
	if(left < right)
	{
		int pivot = partition(data, left, right);
		quickSort(data, left, pivot);
		quickSort(data, pivot+1, right);
	}	
}
void printOutput(Datas *data)
{

}
int main(void)
{
	char *input[INPUT_SIZE]	= 
	{
		"1 4\n",
		"0 1\n",
		"2 6\n",
		"3 5\n",
		"7 13\n",
		"4 9\n",
	};
	Datas data; initDatas(&data);
	printInput(input);
	data.numOfRides = 6; // This is only for example.
	preprocessInput(input, &data);
	quickSort(&data, 0, data.numOfRides);
	printOutput(&data);
	return 0;
}
