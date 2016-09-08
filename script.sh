if ! [ -x "$(command -v arq)" ]; then
	echo 'Error: arq was not found, please make sure Jena is installed and you have added it to your path'>&2
	exit 1
fi

if [ ! -f "FormatCSV.py" ]; then
	echo 'Error: The python formatter was not found, please make sure it is in your current directory'>&2
	exit 1
fi

if ! [ $# != 1 ]; then
	echo 'ts-observe <triple-store.owl> <Observe-query.rq> <output.csv>'
fi

echo "$#"
