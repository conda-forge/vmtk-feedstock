cd build
python -m pip list
git clone https://github.com/vmtk/vmtk-test-data.git tests/vmtk-test-data
pytest --timeout=1200 tests
