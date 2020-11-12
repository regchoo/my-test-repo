#!/bin/sh

# Creates a simple $INDEX file for the current directory 

# Create the $INDEX file
INDEX="index.php"

touch $INDEX

CURRDIR=`pwd`
echo "<?php \$HTML_ROOT=\"/var/www/html\"; include(\"\$HTML_ROOT/incl/header.inc\"); ?>" > $INDEX
echo "<html><head>" >> $INDEX
echo "<link rel=\"stylesheet\" href=\"/css/default.css\">" >> $INDEX
echo "<title>Files in $CURRDIR</title><head><body bgcolor="lightgrey">" >> $INDEX
#echo "<H2>Files in $CURRDIR</H2><HR>" >> $INDEX


# Create links for files in current directory
THIS_DIRECTORY=`ls -a`
# We create links only for these type of files
DISPLAY_THESE="Microsoft MICROSOFT html HTML pdf PDF macromedia Macromedia"

for files in $THIS_DIRECTORY; do
    {
	for display in $DISPLAY_THESE; do
	    	if [ `file $files | cut -d " " -f 2` == $display ]; then
		echo "<li><A HREF=$files>$files</A><BR>" >> $INDEX
    		fi
	done
    }
done

echo "<?php include(\"\$HTML_ROOT/incl/footer.inc\"); ?>" >> $INDEX

echo "</body></html>" >> $INDEX
chmod 644 $INDEX
