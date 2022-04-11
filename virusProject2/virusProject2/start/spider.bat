@echo on
cd /d E:\MyCode\MyPycharmFiles\virusProject\virusProject2\virusProject2
D:\ProgramData\Anaconda3\envs\virusProject\python.exe start_spider_bd.py
TASKKILL /F /IM msedgedriver.exe /T
TASKKILL /F /IM cmd.exe /T
pause