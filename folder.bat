
@echo off
setlocal enabledelayedexpansion
 
echo Creating 100 day folders in this location...
echo.
 
for /L %%i in (1,1,100) do (
    set "num=00%%i"
    set "num=!num:~-3!"
    md "day!num!" 2>nul
)
 
echo.
echo Done. 100 folders created: day001 to day100
pause