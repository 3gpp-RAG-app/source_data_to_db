
directory="/home/mufida/Documents/3GPP/38_series/markdown"


cd "$directory" || exit


for file in *; do

    if [ -f "$file" ]; then
 
        filename=$(basename -- "$file")
        filename_no_ext="${filename%.*}"
        mkdir -p "$filename_no_ext"
        mv "$file" "$filename_no_ext/"
        echo "Moved $file to $filename_no_ext/"
    fi
done
