set SOURCE=%~dp0

SET today=%Date:~10,4%%Date:~4,2%%Date:~7,2%
set t=%time:~0,8%
set t=%t::=%
set t="010000"


echo "drive change"
cd C:
echo "drive path"
cd C:\Wizard_Latest\Wizard_Interface\

echo ********** Executing MM Scripts on Firefox and Chrome *****************


REM Execute test scripts in AWS system in Chrome browser
call pybot --variable SauceLabs_Connect:No --variable BROWSER:gc --outputdir Results\Chrome_%today%_%t% Automation_Testsuites\TestSuites\Demo.txt


REM Execute test scripts in Sauce Labs on Linux OS with Chrome browser
REM call pybot --variable SauceLabs_Connect:Yes --variable BROWSER:gc  --outputdir Results\Chrome_%today%_%t% Automation_Testsuites/TestSuites/Demo.txt

REM pause





