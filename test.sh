for file in `ls`
do
	if [ ${file:0:5} == 'input' ]; then
		python3 msp.py $file > output
		stdout="output${file:5}"
		if diff output $stdout > "diff${file:5}"; then
			echo "success $file"
		else
			echo "failed $file"
		fi
	fi
done