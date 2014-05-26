#include <iostream>
#include <iterator>
#include <list>
using namespace std;

// calculates (n!)/(d!)
int fact_over_fact(int numerator, int denominator) {
	int total = 1;

	// multiply all numbers in the set [n, n-1, ... , d]
	while (numerator > denominator) {
		total *= numerator;
		numerator--;
	}
	return total;
}

// returns start of the next level down one
int start_level_value(int numberOfTiles, int currentLevel){
	int total = 0;

	// sum the number of tiles on each level until you get to the current level
	for (int j = 1; j<=currentLevel; j++) {
		total += fact_over_fact(numberOfTiles, (numberOfTiles-j));
	}
	return total;
}

// returns what level of the tree the value occurs on
int generate_level(int numberOfTiles, int currentValue) {
	int currentLevel = numberOfTiles;

	// loop until the value is no longer less than the start of the level
	while (currentValue < start_level_value(numberOfTiles, currentLevel)) {
		currentLevel--;
	}
	return currentLevel;
}

// calculates width of a "packet" on a given level of a tree
int get_width(int numberOfTiles, int currentLevel) {
	return numberOfTiles-currentLevel;
}

// returns the location of the parent
// start_level_value(numberOfTiles, currentLevel-1) gives first value in the level above the current
// currentValue-start_level_value(numberOfTiles, currentLevel) gives number in the current level
// get_width(numberOfTiles, currentLevel) gives the number of tiles placed under each tile above (number of tiles in a "packet")
// (currentValue-start_level_value(numberOfTiles, currentLevel))/(get_width(numberOfTiles, currentLevel)) give which "packet" the tile is in on the current level
int up_one_level(int numberOfTiles, int currentLevel, int currentValue) {
	return start_level_value(numberOfTiles, currentLevel-1) + (currentValue-start_level_value(numberOfTiles, currentLevel))/(get_width(numberOfTiles, currentLevel));
}

// see overloaded function
int up_one_level(int numberOfTiles, int currentValue) {
	int currentLevel = generate_level(numberOfTiles, currentValue);
	return start_level_value(numberOfTiles, currentLevel-1) + (currentValue-start_level_value(numberOfTiles, currentLevel))/(get_width(numberOfTiles, currentLevel));
}

// start_level_value(numberOfTiles, currentLevel+1) gives first value in the level bellow the current
// (currentValue - start_level_value(numberOfTiles, currentLevel))*width gives location of the value in the level bellow the current
int down_level_first(int numberOfTiles, int currentValue, int numberOfLevelsDown = 1) {
	int currentLevel = generate_level(numberOfTiles, currentValue);

	// width of level one below the current level
	int width = get_width(numberOfTiles, currentLevel+1);
	for (int j = 0; j < numberOfLevelsDown; j++) {
		currentValue = start_level_value(numberOfTiles, currentLevel+1) + (currentValue - start_level_value(numberOfTiles, currentLevel))*width;
		
		// width of next level down is one less than current level
		width--;
		currentLevel++;
	}
	return currentValue;
}

// same idea as down_level_first()
// just adds the width-1 to down_level_first()
int down_level_last(int numberOfTiles, int currentValue, int numberOfLevelsDown = 1) {
	int currentLevel = generate_level(numberOfTiles, currentValue);

	// width of level one below the current level
	int width = get_width(numberOfTiles, currentLevel+1);
	for (int j = 0; j < numberOfLevelsDown; j++) {
		currentValue = start_level_value(numberOfTiles, currentLevel+1) + (currentValue - start_level_value(numberOfTiles, currentLevel)+1)*width - 1;
		
		// width of next level down is one less than current level
		width--; 
		currentLevel++;
	}
	return currentValue;
}


// returns the path to get to the current location from the zeroth level
int* generate_path(int numberOfTiles, int currentLevel, int currentValue){
	int *path = new int[currentLevel+1];

	// store the current value at the ending location of the path
	path[currentLevel] = currentValue;

	// genorates path from current level to root
	while (currentLevel>0) {
		path[currentLevel-1] = up_one_level(numberOfTiles, currentLevel, path[currentLevel]); 
		currentLevel--;
	}
	return path;
}

// see overloaded function
int* generate_path(int numberOfTiles, int currentValue){
	int currentLevel = generate_level(numberOfTiles, currentValue);
	int *path = new int[currentLevel+1];

	// store the current value at the ending location of the path
	path[currentLevel] = currentValue;

	// genorates path from current level to root
	while (currentLevel>0) {
		path[currentLevel-1] = up_one_level(numberOfTiles, currentLevel, path[currentLevel]); 
		currentLevel--;
	}
	return path;
}


// returns the index of the tile being placed at the that level of the tree
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

	// genorate placedTiles from root to current level
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

// see overloaded function
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

	// genorate placedTiles from root to current level
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