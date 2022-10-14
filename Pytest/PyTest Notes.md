# Pytest

## What is pytest?

    A python framework which makes it easier to build simple and scalable tests.

    pros:
        1. Open source
        2. Detects Test and Test Type Automatically
        3. Has the ability to skip tests
        4. Allows Test Cases to Run in Parallel
        5. Allows user to run specific test cases
        6. Easy to use syntax 
        7. Simple to use
    
    Installation:
        To install python one should open up a terminal and run this command "pip install -U pytest"

## Test Case with Pytest

    Test cases in pytest are actually functions using assert keyword.
    which basically returns a boolean if the test case is meeting a certain criteria or not.

    Let say we have multiple test cases and we have to run them, how can we do that?
    We can run it by using following commands
    Module_name.py -k Name_of_TestCase_in_Substring -v

    -k is a tag for substring
    -v is a tag for verbosity

## Test Suite with Pytest

    Test Suite in Pytest is a module with multiple test cases.
    To run test suite in python you must first group the test cases with a marker.
    How to place markets:
        1. Import pytest
        2. use @pytest.mark.suitable_marker_name
        3. if you want to run it individually then when running call that marker like this test.py -m marker_name
        4. Otherwise Make a class and use these methods in it, that will act as a test suite for you.

## Pytest Fixtures

    Let say you have a some code which needs to be executed before running some tests.
    In such scenarios we use pytest fixtures.
    To create a fixture simply add this line of code before the code block or method:
        @pytest.fixture
    To execute the fixture based test suite/case you need to run following command:
    python -m pytest file_name.py (for windows)
    pytest file_name.py (for linux)

## Parameterized Tests

    Sometimes we need to parse in some parameters for the test cases.
    We can do that in a very simple way with pytest and that would be adding this line before the test case:
    @pytest.mark.parameterize("Comma Separated Parameters",["list of values for these comma separated parameters"])
    example:
        @pytest.marl.parametrize("Name,Roll_No,Course",["Asad",1210,"Computer Science Basic"])

## keywords

    We can skip cases with pytest with this simple command:
    @pytest.mark.skip
