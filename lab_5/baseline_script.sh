#!/usr/bin/bash

echo $@

# name of the current tagger experiment
if [ -n "@1" ]; then
    EXP=$(echo "$@//[[:space:]]/")
else
    EXP=baseline
fi

# train tagger
hunpos-train $EXP\_tagger < ewt-train-wt.txt

# run tagger
hunpos-tag $EXP\_tagger < ewt-dev-w.txt > ewt-dev-$EXP.txt

# score tagger
python3 score.py tag ewt-dev-wt.txt ewt-dev-$EXP.txt > result_$EXP.txt

# Display the result
cat result_$EXP.txt
