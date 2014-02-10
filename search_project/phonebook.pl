print "This is your phonebook. What would you like to do?\n";
print "1: Add an entry\n2: Look up a number\n3: Delete an entry\n4: List phonebook\n";

$input = <STDIN>;

switch($input)
{
	case 1:
	addEntry();
	case 2:
	lookup();
	case 3:
	deleteNum();
	case 4: listphonebook();
}

addEntry()
{
	print "Add entry\n";
}

lookup()
{
	print "Lookup\n";
}