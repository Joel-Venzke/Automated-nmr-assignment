#!/usr/bin/perl

# DataFormatScript.pl
# Author: David Mascharka
# Takes input formatted for reading as input into the assignment program and formats it for use in
# unit testing. 

use strict;

open (FILE, '>', 'out.txt') or die;
my $firstline = 1;
while (<>)
{
    if ($firstline) {
        $firstline = 0;
        next;
    }

    chomp $_;
    $_ = "[$_";
    while ($_ =~ /\t+| {2,}/) {
        s/\t+|( {2,})/, /g;
    }
    
    while ($_ =~ /0[^\d.]|0$/) {
        s/0$//g;
        s/0[^\d.]/ /g;
    }

    while ($_ =~ /na/) {
        s/na/-1.0/g;
    }

    s/ /, /g;
    
    $_ =  "$_]\n";
    print FILE $_;
}

close FILE;