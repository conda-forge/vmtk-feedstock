set -e
git clone --quiet https://github.com/vmtk/vmtk-test-data.git ./build/tests/vmtk-test-data
if [ "$(uname)" == "Darwin" ]; then
    pytest ./build/tests/   
elif [ "$(uname)"  = "Linux" ]; then
    xvfb-run --auto-servernum pytest ./build/tests/
else
	exit 1
fi
