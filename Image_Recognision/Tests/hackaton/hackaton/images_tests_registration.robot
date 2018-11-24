*** Settings ***
Library          SeleniumLibrary

Resource         ../../../Settings/images/images_tests.txt
Library          ../../../Libraries/LoadCSV.py
Suite setup      SeleniumLibrary.Set Screenshot Directory    ${SCREENSHOT_DIR}
Test setup       Open Browser and Go to URL    ${BROWSER}    ${URL}
Test Teardown    Close Browser

*** Test Cases ***
Take screenshot
    [Tags]    recognision
    

