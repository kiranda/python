import win32com.client 
import socket
import platform

strComputer = "." 
objWMIService = win32com.client.Dispatch("WbemScripting.SWbemLocator") 
objSWbemServices = objWMIService.ConnectServer(strComputer,"root\cimv2") 
colItems = objSWbemServices.ExecQuery("Select * from Win32_Product")

print (socket.gethostname())
print (platform.platform())

for objItem in colItems: 
    print (objItem.Name)
