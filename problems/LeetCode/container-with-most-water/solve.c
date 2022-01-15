#include <stdio.h>
#include <stdlib.h>
#include <stdarg.h>



int *getLargestArea(int count, int heights[count]){
	int left = 0;
	int right = count - 1;

	int *best = (int*) malloc(2 * sizeof(int));
	int bestArea = 0;

	while (left < right) {
		int lh = heights[left];
		int rh = heights[right];
		int area = (lh > rh ? rh : lh) * (right - left);
		if (area > bestArea) {
			best[0] = left;
			best[1] = right;
			bestArea = area;
		}

		if (lh < rh) left++;
		else right--;
	}

	return best;
}


int assertCase(int count, int heights[count], int expected[2]){
	int *result = getLargestArea(count, heights);
	int passed = result[0] == expected[0] && result[1] == expected[1];
	free(result);
	return passed;
}


int main(){
	if (!assertCase(9, (int[]) {1, 8, 6, 2, 5, 4, 8, 3, 7}, (int[]) {1, 8})) return 1;
	if (!assertCase(2, (int[]) {1, 1}, (int[]) {0, 1})) return 1;
	if (!assertCase(5, (int[]) {4, 3, 2, 1, 4}, (int[]) {0, 4})) return 1;
	if (!assertCase(3, (int[]) {1, 2, 1}, (int[]) {0, 2})) return 1;
	return 0;
}