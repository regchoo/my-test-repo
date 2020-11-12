#!/bin/bash

# delete index.htm if it exists
indexfile="index.htm"
if [ -f "$indexfile" ]
then
    rm -f $indexfile
fi

####file_extensions="avi,AVI,jpg,JPG,jpeg,JPEG,png,PNG,mpg,MPG"

echo "<!DOCTYPE=html>" >> $indexfile
echo "<html><head><style type=\"text/css\">a {text-decoration: none}</style>" >> $indexfile
echo "<meta charset=\"UTF-8\">" >> $indexfile
echo "<title>PIX</title></head><body>" >> $indexfile
echo "<ol><br>" >> $indexfile

shopt -s nullglob

for filename in *.{avi,AVI,jpg,JPG,jpeg,JPEG,mpg,MPG,mpeg,MPEG,png,PNG}
do
    echo "<li><a href=\"$filename\">$filename</a><br></li>" >> $indexfile
done

echo "</ol>" >> $indexfile
echo "</body></html>" >> $indexfile
echo
echo "HTML INDEX FILE DONE!"
echo
