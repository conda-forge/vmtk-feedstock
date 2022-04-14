set -e
git clone --quiet https://github.com/vmtk/vmtk-test-data.git ./build/tests/vmtk-test-data
if [ "$(uname)" == "Darwin" ]; then
    pytest --timeout=1200 ./build/tests/   
elif [ "$(uname)"  = "Linux" ]; then
    xvfb-run --auto-servernum pytest --timeout=1200 ./build/tests/
else
	exit 1
fi
