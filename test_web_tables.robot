*** Settings ***
Library    SeleniumLibrary
Library    check_tables.WebTables


*** Keywords ***
Open Browser Page
    Open Browser    ${url}    ${browser}
    Set Window Position   ${2000}    ${0} 
    Maximize Browser Window
    

*** Variables ***
${url}    https://demoqa.com/webtables
${browser}    chrome
&{values}    First Name=Razvan    Last Name=Alexandru    Email=razvanelul@yahoo.com    Age=23    Salary=9999    Department=IT
${rows_per_page}    ${50}

*** Test Cases ***
TestSearch
    Open Browser Page
    Search    Insurance
    Sleep     3
    Close Browser

TestChangeRows
    Open Browser Page
    Retrieve Rows Per Page
    Select Rows Per Page    ${rows_per_page}
    Sleep    3
    Close Browser
    

TestRetrieveData
    Open Browser Page
    Retrieve Data
    Sleep    5
    Close Browser
    

TestAddData
    Open Browser Page
    Click Add
    Insert Data    ${values}
    Retrieve Data
    Sleep    7
    Close Browser
    