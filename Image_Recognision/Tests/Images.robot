*** Settings ***
Library    SeleniumLibrary
Library    Screenshot
Library    Collections
Library    ../Libraries/ImageComparison.py
Library    OperatingSystem
#Test Setup    Open Browser    https://www.seznam.cz/    chrome
#Test Teardown    Close Browser

*** Test Cases ***
Compare Picture
    ${template}=    Normalize Path     ${CURDIR}/../Resources/Template/logo.png    
    ${screenshot}=    Normalize Path    ${CURDIR}/../Resources/Output/screenshot.png
    Find In Template    ${template}    ${screenshot}
   
Compare Pictures    
    ${path}=    Normalize Path     ${CURDIR}/../Resources/Template/ 
    ${screenshot}=    Normalize Path    ${CURDIR}/../Resources/Output/screenshot.png
    @{templates}=    Set Variable    ${path}\\dog.jpg    ${path}\\find.jpg    ${path}\\logo.png
    Find Images    ${templates}    ${screenshot}    0.4
    