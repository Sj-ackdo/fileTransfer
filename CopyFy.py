#!/usr/bin/env python3
import os


def start():
    usbPy = os.popen("ls /dev/disk/by-id | grep '^usb.*part1$'")
    usbPy = usbPy.read().strip("\n")
    amountUsb = len(usbPy.split())
    
    usb_dict = {}
    for i, x in enumerate(usbPy.split()):
        usb_dict[i] = x
    
    if amountUsb >= 1:
        print( "**", amountUsb, "Storage USB('s) found**")
        print("-----------------------------------------------------")
        for b in range(amountUsb):
            print(str(b + 1) + ".", usb_dict.get(b))
        print("-----------------------------------------------------")    
    elif amountUsb == 0:
        print("*!* No USB's found! *!*")
        exit()

    usbChoice = input("Enter the number of the USB you want to use: ")
    usbChoice = int(usbChoice) - 1
    usbChoice = usb_dict.get(usbChoice)
    if not os.path.exists("/media/usb"):
        os.mkdir("/media/usb")

    if os.path.ismount("/media/usb"):
        os.system("umount /media/usb")
    os.system("mount /dev/disk/by-id/" + usbChoice + " /media/usb")
    
    print("Which directory would you like to transfer to the USB?")
    inputDir = input("Enter the directory: ").rstrip()
    if os.path.exists(inputDir):
        os.system("cp -rv " + inputDir+ " /media/usb")
        print("Transfer completed...")
    else:
        print("Directory does not exist!")
        exit()



start()

#Error count = 2
