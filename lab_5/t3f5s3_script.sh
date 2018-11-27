#!/usr/bin/bash

# name of the current tagger experiment
EXP=t3f5s3

# train tagger
hunpos-train $EXP\_tagger -t 3 -f 5 -s 3 < ewt-train-wt.txt

# run tagger
hunpos-tag $EXP\_tagger < ewt-dev-w.txt > ewt-dev-$EXP.txt

# score tagger
python3 score.py tag ewt-dev-wt.txt ewt-dev-$EXP.txt > result_$EXP.txt

# Display the result
cat result_$EXP.txt
