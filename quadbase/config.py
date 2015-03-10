promoter_options = [("0", "No offset"), ("100", "100 bp"), ("500", "500 bp"), ("1000", "1 Kb"),
                    ("2000", "2 Kb"), ("5000", "5 Kb"), ("10000", "10 Kb")]

variable_stems = ("2-3", "2-5", "3-5")
quad_stem_options = [("2", "2"), ("3", "3"), ("4", "4"), ("5", "5"),
                     ("2-3", "2 - 3"), ("2-5", "2 - 5"), ("3-5", "3 - 5")]
#make sure quad_stem_options and variable stems have synchronized entries

quad_loop_options = [("1", "1"), ("3", "3"), ("5", "5"), ("7", "7"),
                     ("10", "10"), ("12", "12"), ("15", "15"), ("17", "17")]

databases = [("hg19", "Homo Sapiens (hg19)"), ("hg18", "Homo Sapiens (hg18)"),
             ("mm9", "Mus musculus (mm9)"), ("mm10", "Mus musculus (mm10)")]

quad_strand_options = [("both", "Both"), ("+", "Plus (+)"), ("-", "Minus (-)")]
#both option is custom tailored according to quadfinder function