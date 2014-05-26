#include <iostream>
#include <iterator>
#include <list>
using namespace std;

// calculates (n!)/(d!)
int fact_over_fact(int numerator, int denominator) {
	int total = 1;
	while (numerator > denominator) {
		total *= numerator;
		numerator--;
	}
	return total;
}

// returns start of the next level down one
// use: total number of tiles, level number
int start_level_value(int numberOfTiles, int currentLevel){
	int total = 0;
	for (int j = 1; j<=currentLevel; j++) {
		total += fact_over_fact(numberOfTiles, (numberOfTiles-j));
	}
	return total;
}

// returns what level of the tree the value occurs on
// use: total number of tiles, value 
int generate_level(int numberOfTiles, int currentValue) {
	int currentLevel = numberOfTiles;
	while (currentValue < start_level_value(numberOfTiles, currentLevel)) {
		currentLevel--;
	}
	return currentLevel;
}

// calculates width of "packet"
// use: total number of tiles, level number
int get_width(int numberOfTiles, int currentLevel) {
	return numberOfTiles-currentLevel;
}

// use: number of tiles, current level, number of current location
// start_level_value(n,i-1) gives first value in the i-1 level
// (value-start_level_value(n,i)) gives number in the current level
// get_width(n,i) gives the number of tiles placed under each tile above (number of tiles in a "packet")
// (value-start_level_value(n,i))/(get_width(n,i)) give witch "packet" the tile is in
int up_one_level(int numberOfTiles, int currentLevel, int currentValue) {
	return start_level_value(numberOfTiles, currentLevel-1) + (currentValue-start_level_value(numberOfTiles, currentLevel))/(get_width(numberOfTiles, currentLevel));
}

// use: number of tiles, number of current location
int up_one_level(int numberOfTiles, int currentValue) {
	int currentLevel = generate_level(numberOfTiles, currentValue);
	return start_level_value(numberOfTiles, currentLevel-1) + (currentValue-start_level_value(numberOfTiles, currentLevel))/(get_width(numberOfTiles, currentLevel));
}

// use: number of tiles, number of current location, number of levels down
// start_level_value(n,i+1) gives first value in the i+1 level
// (value - start_level_value(n,i))*w gives location of the value in the i+1 level
int down_level_first(int numberOfTiles, int currentValue, int numberOfLevelsDown = 1) {
	int currentLevel = generate_level(numberOfTiles, currentValue);
	int width = get_width(numberOfTiles, currentLevel+1);
	for (int j = 0; j < numberOfLevelsDown; j++) {
		currentValue = start_level_value(numberOfTiles, currentLevel+1) + (currentValue - start_level_value(numberOfTiles, currentLevel))*width;
		width--; currentLevel++;
	}
	return currentValue;
}


// use: number of tiles, number of current location, number of levels down
// same idea as down_level_first()
// just adds the width-1 to down_level_first()
int down_level_last(int numberOfTiles, int currentValue, int numberOfLevelsDown = 1) {
	int currentLevel = generate_level(numberOfTiles, currentValue);
	int width = get_width(numberOfTiles, currentLevel+1);
	for (int j = 0; j < numberOfLevelsDown; j++) {
		currentValue = start_level_value(numberOfTiles, currentLevel+1) + (currentValue - start_level_value(numberOfTiles, currentLevel)+1)*width - 1;
		width--; currentLevel++;
	}
	return currentValue;
}


// use: number of tiles, current level, number of current location
// returns the path to get to the current location from the start
int* generate_path(int numberOfTiles, int currentLevel, int currentValue){
	int *path = new int[currentLevel+1];
	path[currentLevel] = currentValue;
	while (currentLevel>0) {
		path[currentLevel-1] = up_one_level(numberOfTiles, currentLevel, path[currentLevel]); 
		currentLevel--;
	}
	return path;
}

// use: number of tiles, number of current location
int* generate_path(int numberOfTiles, int currentValue){
	int currentLevel = generate_level(numberOfTiles, currentValue);
	int *path = new int[currentLevel+1];
	path[currentLevel] = currentValue;
	while (currentLevel>0) {
		path[currentLevel-1] = up_one_level(numberOfTiles, currentLevel, path[currentLevel]); 
		currentLevel--;
	}
	return path;
}

// use: number of tiles, current level, number of current location
// returns the indexes of the tile being along the path to the current location
// basically generates the old placed tiles array
int* generate_index(int numberOfTiles, int currentLevel, int currentValue) {
	int temp;
	int *placedTiles = generate_path(numberOfTiles, currentLevel, currentValue);
	list<int> unplacedTiles;
	list<int>::iterator it;

	// fill list with possible tile indexes
	for (int j = 0; j < numberOfTiles; ++j)
	{
		unplacedTiles.push_back(j);
	}
	for (int j = 0; j<currentLevel+1; j++) {
		// set it to the being of the list
		it = unplacedTiles.begin();

		// find the index of remaining tiles
		temp = (placedTiles[j]-start_level_value(numberOfTiles, j)) % get_width(numberOfTiles, j);

		// move through list
		advance(it, temp);

		// place tile and remove from unplaced tiles
		placedTiles[j] = *it;
		unplacedTiles.erase(it);
	}
	return placedTiles;
}

// use: number of tiles, number of current location
int* generate_index(int numberOfTiles, int currentValue) {
	int currentLevel = generate_level(numberOfTiles, currentValue), temp;
	int *placedTiles = generate_path(numberOfTiles, currentLevel, currentValue);
	list<int> unplacedTiles;
	list<int>::iterator it;

	// fill list with possible tile indexes
	for (int j = 0; j < numberOfTiles; ++j)
	{
		unplacedTiles.push_back(j);
	}
	for (int j = 0; j<currentLevel+1; j++) {
		// set it to the being of the list
		it = unplacedTiles.begin();

		// find the index of remaining tiles
		temp = (placedTiles[j]-start_level_value(numberOfTiles, j)) % get_width(numberOfTiles, j);

		// move through list
		advance(it, temp);

		// place tile and remove from unplaced tiles
		placedTiles[j] = *it;
		unplacedTiles.erase(it);
	}
	return placedTiles;
}

int main(int argc, char const *argv[])
{
	cout << down_level_first(6,0,5) << '\n';
	int *path = generate_index(6,1240);
	for (int i = 0; i<6; i++) {
		cout << path[i] << '\t';
	}
	delete path;
	return 0;
}