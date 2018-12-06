file=$1
sed -i '/^$/{n;/^$/d}' $file
