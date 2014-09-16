#include <iostream>
#include <string>
#include <list>
#include "node.cu"
#include "nmr_data.cu"
using namespace std;

struct protein
{
	float cAlpha1; // c alpha for i
	float cBeta1; // c beta for i
	int group;
};


// take in abbreviation, generates chemical shift data
protein letters_to_numbers(char acid[4]){

	// TODO: Create data base file for values
	// TODO: Make it easer to update 
	// TODO: python script for runtime?
	switch (acid) {
		case ala: 
	}
}

// read in all data from file
void read_In_File(string &fileName, protein &p, nmrData &n) {
	
	// float value = atof(myString.c_str());
}


void start_search(string fileName){
	// Initialize variables

	// Read in file, Store NRM Data and protein chain in array

	// Generate root node

	// Create frontier linked list

	// Loop till solution is found
	// while (keepRunning) {
		// Find best node to expand

		// Remove best node from list

		// Check state of node

		// Expand Node

		// Check if the solution has been found
	// }

	// Print results

	// TODO: save results to output file
}