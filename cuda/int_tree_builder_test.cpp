#include <iostream>
#include <vector> 
using namespace std;

// int factOverFact(int n, int d);
// int startLevelValue(int n, int i);
// int generateLevel(int n, int value);
// int width(int n, int i);
// int upOneLevel(int n, int i, int value);
// int upOneLevel(int n, int value);
// int downLevelFirst(int n, int i, int value, int num);
// int downLevelFirst(int n, int value, int num);
// int downLevelLast(int n, int i, int value, int num);
// int downLevelLast(int n, int value, int num);
// int* generatePath(int n, int i, int value);
// int* generatePath(int n, int value);
// int* generateIndex(int n, int i, int value);
// int* generateIndex(int n, int value);

// calculates (n!)/(d!)
int factOverFact(int n, int d) {
	int total = 1;
	while (n>d) {
		total *= n;
		n--;
	}
	return total;
}

// returns start of the next level down one
// total number of levels, level number
int startLevelValue(int n, int i){
	int total = 0;
	for (int j = 1; j<=i; j++) {
		total += factOverFact(n,(n-j));
	}
	return total;
}

int generateLevel(int n, int value) {
	int i=n;
	while (value < startLevelValue(n,i)) {
		i--;
	}
	return i;
}

// calculates width of "packet"
int width(int n, int i) {
	return n-i;
}

// give number of tiles, current level, number of current location
// startLevelValue(n,i-1) gives first value in the i-1 level
// (value-startLevelValue(n,i)) gives number in the current level
// width(n,i) gives the number of tiles placed under each tile above (number of tiles in a "packet")
// (value-startLevelValue(n,i))/(width(n,i)) give witch "packet" the tile is in
int upOneLevel(int n, int i, int value) {
	return startLevelValue(n,i-1) + (value-startLevelValue(n,i))/(width(n,i));
}

int upOneLevel(int n, int value) {
	int i = generateLevel(n,value);
	return startLevelValue(n,i-1) + (value-startLevelValue(n,i))/(width(n,i));
}

int downLevelFirst(int n, int i, int value, int num) {
	for (int j = 0; j<num; j++, i++) {
		value = startLevelValue(n,i+1) + (value - startLevelValue(n,i))*width(n,i+1);
	}
	return value;
}

int downLevelFirst(int n, int value, int num) {
	int i = generateLevel(n,value);
	return startLevelValue(n,i+1) + (value - startLevelValue(n,i))*width(n,i+1);
}

int downLevelLast(int n, int i, int value, int num) {
	int w = width(n,i+1);
	return startLevelValue(n,i+1) + (value - startLevelValue(n,i)+1)*w-1;
}

int downLevelLast(int n, int value, int num) {
	int i = generateLevel(n,value);
	int w = width(n,i+1);
	return startLevelValue(n,i+1) + (value - startLevelValue(n,i)+1)*w - 1;
}

int* generatePath(int n, int i, int value){
	int *path = new int[i+1];
	path[i] = value;
	while (i>0) {
		path[i-1] = upOneLevel(n,i,path[i]); 
		i--;
	}
	return path;
}

int* generatePath(int n, int value){
	int i = generateLevel(n,value);
	int *path = new int[i+1];
	path[i] = value;
	while (i>0) {
		path[i-1] = upOneLevel(n,i,path[i]); 
		i--;
	}
	return path;
}

int* generateIndex(int n, int i, int value) {
	int temp;
	int *index = generatePath(n,i,value);
	vector<int> tileIndex;
	for (int j = 0; j < n; ++j)
	{
		tileIndex.push_back(j);
	}
	for (int j = 0; j<i+1; j++) {
		temp = (index[j]-startLevelValue(n,j)) % width(n,j);
		index[j] = tileIndex[temp];
		tileIndex.erase(tileIndex.begin() + temp);
	}
	return index;
}

int* generateIndex(int n, int value) {
	int i = generateLevel(n,value), temp;
	int *index = generatePath(n,i,value);
	vector<int> tileIndex;
	for (int j = 0; j < n; ++j)
	{
		tileIndex.push_back(j);
	}
	for (int j = 0; j<i+1; j++) {
		temp = (index[j]-startLevelValue(n,j)) % width(n,j);
		index[j] = tileIndex[temp];
		tileIndex.erase(tileIndex.begin() + temp);
	}
	return index;
}

int main(int argc, char const *argv[])
{
	int *path = generateIndex(4,60);
	for (int i = 0; i<4; i++) {
		cout << path[i] << '\t';
	}
	delete path;
	return 0;
}