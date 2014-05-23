#include <iostream>
#include <iterator>
#include <list>
using namespace std;

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
// use: total number of tiles, level number
int startLevelValue(int n, int i){
	int total = 0;
	for (int j = 1; j<=i; j++) {
		total += factOverFact(n,(n-j));
	}
	return total;
}

// returns what level of the tree the value occurs on
// use: total number of tiles, value 
int generateLevel(int n, int value) {
	int i=n;
	while (value < startLevelValue(n,i)) {
		i--;
	}
	return i;
}

// calculates width of "packet"
// use: total number of tiles, level number
int width(int n, int i) {
	return n-i;
}

// use: number of tiles, current level, number of current location
// startLevelValue(n,i-1) gives first value in the i-1 level
// (value-startLevelValue(n,i)) gives number in the current level
// width(n,i) gives the number of tiles placed under each tile above (number of tiles in a "packet")
// (value-startLevelValue(n,i))/(width(n,i)) give witch "packet" the tile is in
int upOneLevel(int n, int i, int value) {
	return startLevelValue(n,i-1) + (value-startLevelValue(n,i))/(width(n,i));
}

// use: number of tiles, number of current location
int upOneLevel(int n, int value) {
	int i = generateLevel(n,value);
	return startLevelValue(n,i-1) + (value-startLevelValue(n,i))/(width(n,i));
}

// use: number of tiles, number of current location, number of levels down
// startLevelValue(n,i+1) gives first value in the i+1 level
// (value - startLevelValue(n,i))*width(n,i+1) gives location of the value in the i+1 level
int downLevelFirst(int n, int value, int num = 1) {
	int i = generateLevel(n,value);
	// TODO make num work
	return startLevelValue(n,i+1) + (value - startLevelValue(n,i))*width(n,i+1);
}


// use: number of tiles, number of current location, number of levels down
// same idea as downLevelFirst()
// just adds the width-1 to downLevelFirst()
int downLevelLast(int n, int value, int num = 1) {
	int i = generateLevel(n,value);
	int w = width(n,i+1);
	// TODO make num work
	return startLevelValue(n,i+1) + (value - startLevelValue(n,i)+1)*w - 1;
}


// use: number of tiles, current level, number of current location
// returns the path to get to the current location from the start
int* generatePath(int n, int i, int value){
	int *path = new int[i+1];
	path[i] = value;
	while (i>0) {
		path[i-1] = upOneLevel(n,i,path[i]); 
		i--;
	}
	return path;
}

// use: number of tiles, number of current location
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

// use: number of tiles, current level, number of current location
// returns the indexes of the tile being along the path to the current location
// basically generates the old placed tiles array
int* generateIndex(int n, int i, int value) {
	int temp;
	int *placedTiles = generatePath(n,i,value);
	list<int> unplacedTiles;
	list<int>::iterator it;

	// fill list with possible tile indexes
	for (int j = 0; j < n; ++j)
	{
		unplacedTiles.push_back(j);
	}
	for (int j = 0; j<i+1; j++) {
		// set it to the being of the list
		it = unplacedTiles.begin();

		// find the index of remaining tiles
		temp = (placedTiles[j]-startLevelValue(n,j)) % width(n,j);

		// move through list
		advance(it,temp);

		// place tile and remove from unplaced tiles
		placedTiles[j] = *it;
		unplacedTiles.erase(it);
	}
	return placedTiles;
}

// use: number of tiles, number of current location
int* generateIndex(int n, int value) {
	int i = generateLevel(n,value), temp;
	int *placedTiles = generatePath(n,i,value);
	list<int> unplacedTiles;
	list<int>::iterator it;
	
	// fill list with possible tile indexes
	for (int j = 0; j < n; ++j)
	{
		unplacedTiles.push_back(j);
	}
	for (int j = 0; j<i+1; j++) {
		// set it to the being of the list
		it = unplacedTiles.begin();

		// find the index of remaining tiles
		temp = (placedTiles[j]-startLevelValue(n,j)) % width(n,j);

		// move through list
		advance(it,temp);

		// place tile and remove from unplaced tiles
		placedTiles[j] = *it;
		unplacedTiles.erase(it);
	}
	return placedTiles;
}

int main(int argc, char const *argv[])
{
	cout << downLevelFirst(6,1240);
	int *path = generateIndex(6,1240);
	// cout << startLevelValue(6,5);
	for (int i = 0; i<6; i++) {
		cout << path[i] << '\t';
	}
	delete path;
	return 0;
}