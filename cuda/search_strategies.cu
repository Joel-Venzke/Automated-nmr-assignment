#include <iostream>
#include <string>
#include <list>
using namespace std;

// take in abbreviation, generates chemical shift data
array lettersToNumbers(string acid){

	// TODO: Create data base file for values
	// TODO: Make it easer to update 
	// TODO: python script for runtime?

}

// read in protein from data file
Protein readInProtein(string &fileName){

}

// read in Chemical Shift Values from data file
NMR readInNMR(string &fileName) {

	//place holder tiles
}

// read in all data from file
void readInFile(string &fileName, Protein &p, NMR &n) {
	p = readInProtein(fileName);
	n = readInNMR(fileName);
}


void startSearch(string fileName){
	// Initialize variables

	// Read in file, Store NRM Data and protein chain in array

	// Generate root node

	// Create frontier linked list

	// Loop till solution is found
	while (keepRunning) {
		// Find best node to expand

		// Remove best node from list

		// Check state of node

		// Expand Node

		// Check if the solution has been found
	}

	// Print results

	// TODO: save results to output file
}