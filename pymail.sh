created=$(ls ~ -lah | grep .pymail | wc -l)
if [ $created -gt 0 ]
	then
		echo ""
else 
	mkdir ~/.pymail
fi 
#mkdir ~/.pymail
while test $# -gt 0; do
        case "$1" in
                -h|--help)
                        echo "$package - attempt to capture frames"
                        echo " "
                        echo "$package [options] application [arguments]"
                        echo " "
                        echo "options:"
                        echo "-h, --help                show brief help"
                        echo "-l,		        Logs in/ Logs out current user "
                        echo "-o, --output-dir=DIR      specify a directory to store output in"
                        exit 0
                        ;;
                -a)
                        shift
                        if test $# -gt 0; then
                                export PROCESS=$1
                        else
                                echo ""
                                exit 1
                        fi
                        shift
                        ;;
                --action*)
                        export PROCESS=`echo $1 | sed -e 's/^[^=]*=//g'`
                        shift
                        ;;
                -o)
                        shift
                        if test $# -gt 0; then
                                export OUTPUT=$1
                        else
                                echo "no output dir specified"
                                exit 1
                        fi
                        shift
                        ;;
                --output-dir*)
                        export OUTPUT=`echo $1 | sed -e 's/^[^=]*=//g'`
                        shift
                        ;;
                *)
			echo "illegal flags"
                        break
                        ;;
        esac
done

