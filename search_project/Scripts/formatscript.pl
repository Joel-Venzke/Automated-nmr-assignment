#!/usr/bin/perl
#
# formatscript.pl
# Author: David Mascharka
#
# This format script loops through all .str files (star files from BMRB: http://www.bmrb.wisc.edu/), pulls out
# Carbon alpha and Carbon beta values for each amino acid inside a given number of standard deviations, and formats
# everything into an appropriate arff file
#
# Creates a file final.arff, which is the full output

use strict;
use warnings;

my $savefile = 'formatted.txt';
my $finalfile = 'final.arff';
my $finalfilehandle;

my $filehandle;
open $filehandle, '>', $savefile or die "Could not open $savefile: $!";

my $start = 0;

my $stdDeviations = 1;
my $deviation = 0;
my $average = 0;
my $number = 0;

my @files = <*.str>;
my $file;
my $line;
foreach $file (@files) {
	open my $fh, '<', $file or die "Cannot open $file: $!";

	foreach (<$fh>) {
		if (m/Atom_chem_shift\.Assigned_chem_shift_list_ID/) {
			$start = 1;
		}
		if ($start) {
			if (m/stop/) {
				$start = 0;
			}

			s/^\s*//;
			s/^\d*\s*\.(\s*\d*)*\s*//;
			s/\s+/\t/g;

			m/(\w{3}\t\w{2}).*?(\d+\.\d+).*/;
			if (defined $1 and defined $2) {
			    $line = "$1,$2\n";
			    $line =~ s/\t/,/g;
			}
			
			if (m/.*CA|CB.*/) {
				if ($line =~ m/^\w{3},\w{2},\d{3,}\./) {
					next;
				}
				if ($line =~ m/^\w{3},\w{2},\d{1}\./) {
					next;
				}

				if ($line =~ m/^ALA,CA/) {
				    $deviation = 1.95;
				    $average = 53.19;
				}
				if ($line =~ m/^ALA,CB/) {
				    $deviation = 1.78;
				    $average = 18.96;
				}
				if ($line =~ m/^ARG,CA/) {
				    $deviation = 2.31;
				    $average = 56.82;
				}
				if ($line =~ m/^ARG,CB/) {
				    $deviation = 1.82;
				    $average = 30.65;
				}
				if ($line =~ m/^ASN,CA/) {
				    $deviation = 1.88;
				    $average = 53.56;
				}
				if ($line =~ m/^ASN,CB/) {
				    $deviation = 1.67;
				    $average = 38.68;
				}
				if ($line =~ m/^ASP,CA/) {
				    $deviation = 2.04;
				    $average = 54.70;
				}
				if ($line =~ m/^ASP,CB/) {
				    $deviation = 1.61;
				    $average = 40.87;
				}
				if ($line =~ m/^CYS,CA/) {
				    $deviation = 3.38;
				    $average = 58.23;
				}
				if ($line =~ m/^CYS,CB/) {
				    $deviation = 6.24;
				    $average = 32.85;
				}
				if ($line =~ m/^GLN,CA/) {
				    $deviation = 2.12;
				    $average = 56.62;
				}
				if ($line =~ m/^GLN,CB/) {
				    $deviation = 1.81;
				    $average = 29.16;
				}
				if ($line =~ m/^GLU,CA/) {
				    $deviation = 2.07;
				    $average = 57.35;
				}
				if ($line =~ m/^GLU,CB/) {
				    $deviation = 1.70;
				    $average = 29.97;
				}
				if ($line =~ m/^GLY,CA/) {
				    $deviation = 1.27;
				    $average = 45.36;
				}
				if ($line =~ m/^HIS,CA/) {
				    $deviation = 2.32;
				    $average = 56.52;
				}
				if ($line =~ m/^HIS,CB/) {
				    $deviation = 2.09;
				    $average = 30.22;
				}
				if ($line =~ m/^ILE,CA/) {
				    $deviation = 2.69;
				    $average = 61.67;
				}
				if ($line =~ m/^ILE,CB/) {
				    $deviation = 1.99;
				    $average = 38.58;
				}
				if ($line =~ m/^LEU,CA/) {
				    $deviation = 2.12;
				    $average = 55.69;
				}
				if ($line =~ m/^LEU,CB/) {
				    $deviation = 1.85;
				    $average = 42.26;
				}
				if ($line =~ m/^LYS,CA/) {
				    $deviation = 2.18;
				    $average = 56.98;
				}
				if ($line =~ m/^LYS,CB/) {
				    $deviation = 1.77;
				    $average = 32.77;
				}
				if ($line =~ m/^MET,CA/) {
				    $deviation = 2.23;
				    $average = 56.13;
				}
				if ($line =~ m/^MET,CB/) {
				    $deviation = 2.20;
				    $average = 32.94;
				}
				if ($line =~ m/^PHE,CA/) {
				    $deviation = 2.59;
				    $average = 58.14;				   
				}
				if ($line =~ m/^PHE,CB/) {
				    $deviation = 1.07;
				    $average = 39.94;
				}
				if ($line =~ m/^PRO,CA/) {
				    $deviation = 1.51;
				    $average = 63.36;
				}
				if ($line =~ m/^PRO,CB/) {
				    $deviation = 1.18;
				    $average = 31.84;
				}
				if ($line =~ m/^SER,CA/) {
				    $deviation = 2.09;
				    $average = 58.75;
				}
				if ($line =~ m/^SER,CB/) {
				    $deviation = 1.52;
				    $average = 63.79;
				}
				if ($line =~ m/^THR,CA/) {
				    $deviation = 2.59;
				    $average = 62.26;
				}
				if ($line =~ m/^THR,CB/) {
				    $deviation = 1.75;
				    $average = 69.71;
				}
				if ($line =~ m/^TRP,CA/) {
				    $deviation = 2.58;
				    $average = 57.74;
				}
				if ($line =~ m/^TRP,CB/) {
				    $deviation = 2.00;
				    $average = 29.97;
				}
				if ($line =~ m/^TYR,CA/) {
				    $deviation = 2.52;
				    $average = 58.18;
				}
				if ($line =~ m/^TYR,CB/) {
				    $deviation = 2.14;
				    $average = 39.27;
				}
				if ($line =~ m/^VAL,CA/) {
				    $deviation = 2.86;
				    $average = 62.58;
				}
				if ($line =~ m/^VAL,CB/) {
				    $deviation = 1.78;
				    $average = 32.17;
				}
				
				$number = $1 if $line =~ m/C[AB],(\d+\.\d+)/;
			
				if (defined($number) && $number >= $average - $stdDeviations * $deviation &&
				    $number <= $average + $stdDeviations * $deviation) {
				    print $filehandle "$line";
				}
			}
		}
	}

	$start = 0;
	close $fh;
}

close $filehandle;
open $filehandle, '<', $savefile or die "Cannot open $savefile: $!";
open $finalfilehandle, '>', $finalfile or die "Cannot open $finalfile: $!";

print $finalfilehandle "\@relation AminoAcid\n\@attribute residue { ALA, CYS, ASP, GLU, PHE, GLY, HIS, ILE, LYS,";
print $finalfilehandle "LEU, MET, ASN, PRO, GLN, ARG, SER, THR, VAL, TRP, TYR }\n\@attribute c_alpha numeric\n";
print $finalfilehandle "\@attribute c_beta numeric\n\n\@data\n";

my $lastline;
my $firstline = 1;
foreach (<$filehandle>) {
	if ($firstline) {
		$lastline = $_;
		$firstline = 0;
		next;
	}

	my ($aminoAcid) = $lastline =~ /(\w{3}).*CA.*/;

	if (defined $aminoAcid && ($aminoAcid eq "ALA" || $aminoAcid eq "CYS" || $aminoAcid eq "ASP"
	|| $aminoAcid eq "GLU" || $aminoAcid eq "PHE" || $aminoAcid eq "GLY"
	|| $aminoAcid eq "HIS" || $aminoAcid eq "ILE" || $aminoAcid eq "LYS"
	|| $aminoAcid eq "LEU" || $aminoAcid eq "MET" || $aminoAcid eq "ASN"
	|| $aminoAcid eq "PRO" || $aminoAcid eq "GLN" || $aminoAcid eq "ARG"
	|| $aminoAcid eq "SER" || $aminoAcid eq "THR" || $aminoAcid eq "VAL"
	|| $aminoAcid eq "TYR" || $aminoAcid eq "TRP")) {
		if (m/$aminoAcid.*CB.*/) {
			chomp $lastline;
			$lastline =~ s/CA,//;
			chomp;
			s/\w{3},CB,//;
			print $finalfilehandle "$lastline,$_\n";
		} else {
			chomp $lastline;
			$lastline =~ s/CA,//;
			print $finalfilehandle "$lastline,?\n";
		}
	} else {
		my ($aminoAcid) = $lastline =~ /(\w{3}).*CB.*/;
		if (defined $aminoAcid && ($aminoAcid eq "ALA" || $aminoAcid eq "CYS" || $aminoAcid eq "ASP"
		|| $aminoAcid eq "GLU" || $aminoAcid eq "PHE" || $aminoAcid eq "GLY"
		|| $aminoAcid eq "HIS" || $aminoAcid eq "ILE" || $aminoAcid eq "LYS"
		|| $aminoAcid eq "LEU" || $aminoAcid eq "MET" || $aminoAcid eq "ASN"
		|| $aminoAcid eq "PRO" || $aminoAcid eq "GLN" || $aminoAcid eq "ARG"
		|| $aminoAcid eq "SER" || $aminoAcid eq "THR" || $aminoAcid eq "VAL"
		|| $aminoAcid eq "TYR" || $aminoAcid eq "TRP")) {
				chomp $lastline;
				$lastline =~ s/CB,//;
				$lastline =~ s/$aminoAcid,//;
				print $finalfilehandle "$aminoAcid,?,$lastline\n";
		}
	}
	$lastline = $_;
}

close $filehandle;
close $finalfilehandle;

unlink $savefile;

print "done\n";
