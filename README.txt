To use with latex diff,

use the following command line with two self constained latex files 
(condensed into a single one using merge_tex.py) and the pre-diff.tex file
from the repo

latexdiff -p diff-pre.tex --type=CCHANGEBAR --append-safecmd="nu.*,v.*,such.*{,}" --exclude-safecmd="in" old.tex new.tex > diff.tex
