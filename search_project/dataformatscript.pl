#!/usr/bin/perl

# DataFormatScript.pl
# Author: David Mascharka
# Takes input formatted for reading as input into the assignment program and formats it for use in
# unit testing. 

use strict;

my $firstline = 1;
while (<>)
{
    if ($firstline) {
        $firstline = 0;
        next;
    }

    chomp $_;

    s/^\s+|\s+$//g;
        
    while ($_ =~ /0[^\d.]|0$/) {
        s/0$//g;
        s/0[^\d.]/ /g;
    }

    s/\.[^\d]/\.0 /g;

    s/na/-1.0/g;
    
    s/\s+/, /g;
    
    $_ =  "[$_]\n";
    print $_;
}

close FILE;