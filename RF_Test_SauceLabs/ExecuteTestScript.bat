set SOURCE=%~dp0

SET today=%Date:~10,4%%Date:~4,2%%Date:~7,2%
set t=%time:~0,8%
set t=%t::=%
set t="010000"


echo "drive change"
cd C:
echo "drive path"
cd C:\RF_Test_SauceLabs\

echo ********** Executing MM Scripts on Firefox and Chrome *****************


#call pybot --variable SausLabs_Connect:Yes --outputdir results\Firefox_%today%_%t% tests
call pybot --variable SausLabs_Connect:Yes --outputdir results\Firefox_%today%_%t% tests




