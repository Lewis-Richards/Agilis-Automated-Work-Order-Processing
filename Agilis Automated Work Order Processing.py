#! python3

## This program uses gui automation to automate the closure and resolution of work orders within a medical equipment management system

	
## Work Flow for recognizing the No Billable Dollars Alert
## 1) Find the billable alert  2) Click the OK button  3) Scroll down 4) Find the "Total Billable Amount" header
## 5) Click just below the header  6) Drag and highlight the text in the field 7)Copy to clip board and compare with $0.00
## 8) If not zero click on the exclamation point at the same Y axis  9) If zero, move slightly down under the "Total Billable Amount Header"
## 10) Click on the next available amount field and perform steps 6-8

import pyautogui, sys, time, datetime, pyperclip, webbrowser


phase = 0

def cycle(phase):  ## Provides visual feedback of distinct program phases in console window for review and troubleshooting purposes
    phase = int(phase)
    if phase == 0:
        Start = "START"
        print(Start.center(100, "-"))
    elif 0 < phase < 4:
        Sequence = "PHASE_" + str(phase)
        print(Sequence.center(100, "-"))
    else:
        Complete = "COMPLETE"
        print(Complete.center(100, "-"))

cycle(phase) ##Start

now = datetime.datetime.now()
print(str(now))
Start_Time = time.time()
print(Start_Time)

phase +=1 ##Phase 1
cycle(phase) 


Entry_Date = (now.strftime("%m/%d/%Y")) ## This selects a report period dating back to the beginning of the present month
print("Entry Date = " + Entry_Date)
File_Name = (now.strftime("%m%d%Y_Incomplete_PMs"))


phase +=1 ##Phase 2
cycle(phase)

session = 0

for i in range (1, 11):

    Increment_Session = session + 1
    print("Starting Session {}".format(Increment_Session))
    pyautogui.pause = 0.5
    time.sleep(2.0)
    pyautogui.moveTo(327,271)
    pyautogui.click(clicks=1)
    Work_Order_Reference_Icon = pyautogui.locateOnScreen("Work_Order_Reference_Icon.png", grayscale=True) 
    while Work_Order_Reference_Icon == None:
        Work_Order_Reference_Icon = pyautogui.locateOnScreen("Work_Order_Reference_Icon.png", grayscale=True)
        print("Still searching for Work_Order_Reference_Icon...")

#When program finds image, print the location
    print("Center of Work_Order_Reference_Icon is located at {0}".format(Work_Order_Reference_Icon))
    Work_Order_Reference_Icon_X, Work_Order_Reference_Icon_Y = pyautogui.center(Work_Order_Reference_Icon)
    pyautogui.moveTo(Work_Order_Reference_Icon_X + 110, Work_Order_Reference_Icon_Y)
    pyautogui.click(clicks=2)

       
    time.sleep(3.0)
    pyautogui.moveTo(1591,274)
    pyautogui.click(clicks=1)
    time.sleep(0.5)
    pyautogui.dragTo(1591, 505, 2, button='left')
    pyautogui.click(clicks=1)  # click in the Start Date Field
    time.sleep(3.0)

    Work_Order_Itemized_Cost = pyautogui.locateCenterOnScreen("Work_Order_Itemized_Cost.png", grayscale=True) 
    Work_Order_Itemized_Cost_HL = pyautogui.locateCenterOnScreen("Work_Order_Itemized_Cost_HL.png", grayscale=True) 

    while Work_Order_Itemized_Cost == None and Work_Order_Itemized_Cost_HL == None: 
        Work_Order_Itemized_Cost = pyautogui.locateCenterOnScreen("Work_Order_Itemized_Cost.png", grayscale=True)
        Work_Order_Itemized_Cost_HL = pyautogui.locateCenterOnScreen("Work_Order_Itemized_Cost_HL.png", grayscale=True)
        print("Still searching for Work_Order_Itemized_Cost Buttons...")

           
    if Work_Order_Itemized_Cost != None:
            time.sleep(0.5)
            print("Center of Work_Order_Itemized_Cost is located at {0}".format(Work_Order_Itemized_Cost))
            pyautogui.moveTo(Work_Order_Itemized_Cost)
            pyautogui.click(clicks=1)

    elif Work_Order_Itemized_Cost_HL != None:
            time.sleep(0.5)
            print("Center of Work_Order_Itemized_Cost_HL is located at {0}".format(Work_Order_Itemized_Cost_HL))
            pyautogui.moveTo(Work_Order_Itemized_Cost_HL)
            pyautogui.click(clicks=1)         
  

    else:
            print("This just is not working!")    
    

    Exclamation_Point_Icon = pyautogui.locateCenterOnScreen("Exclamation_Point_Icon.png", grayscale=True)
    while Exclamation_Point_Icon == None:
        Exclamation_Point_Icon = pyautogui.locateCenterOnScreen("Exclamation_Point_Icon.png", grayscale=True)
        print("Still searching for Exclamation_Point_Icon...")

#When program finds image, print the location
    print("Center of Exclamation_Point_Icon is located at {0}".format(Exclamation_Point_Icon))
    pyautogui.moveTo(Exclamation_Point_Icon)
    pyautogui.click(clicks=1)
    time.sleep(3.0) # changing from 4.0 to 3.0
    pyautogui.moveTo(895,343)
    pyautogui.click(clicks=1)
    Total_Billable_Field = pyautogui.locateCenterOnScreen("Total_Billable_Field.png", grayscale=True)
    while Exclamation_Point_Icon == None:
        Total_Billable_Field = pyautogui.locateCenterOnScreen("Total_Billable_Field.png", grayscale=True)
        print("Still searching for Total_Billable_Field...")

#When program finds image, print the location
    print("Center of Total_Billable_Field is located at {0}".format(Total_Billable_Field))
    pyautogui.moveTo(Total_Billable_Field)
    pyautogui.click(clicks=2) # 04172018 @ 2:50 PM Changed to 2 clicks.
    time.sleep(2.0)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.press(['delete', '0','tab', 'tab', 'tab'])

    time.sleep(1.5)

    Total_Concession_Amount = float(pyperclip.paste())
    time.sleep(1.5)
    print(Total_Concession_Amount)
    time.sleep(1.5)
    pyperclip.paste()
    pyautogui.pause = 0.5
    pyautogui.press(['down', 'down', 'down', 'tab', 'tab', 'down', 'tab'])
    time.sleep(3.0) # changing from 4.0 to 3.0

    if Total_Concession_Amount == 0.0:
        Update_Button_Gray = pyautogui.locateCenterOnScreen("Update_Button_Gray.png", grayscale=True)
        while Update_Button_Gray == None:
            Update_Button_Gray = pyautogui.locateCenterOnScreen("Update_Button_Gray.png", grayscale=True)
        print("Still searching for Update_Button_Gray...")
        pyautogui.moveTo(Update_Button_Gray)
        pyautogui.click(clicks=1)
        time.sleep(2.0)
        pass
        

    elif Total_Concession_Amount != 0.0:
        Save_Button_Gray = pyautogui.locateCenterOnScreen("Save_Button_Gray.png", grayscale=True)
        while Save_Button_Gray == None:
            Save_Button_Gray = pyautogui.locateCenterOnScreen("Save_Button_Gray.png", grayscale=True)
        print("Still searching for Save_Button_Gray...")
        pyautogui.moveTo(Save_Button_Gray)
        pyautogui.click(clicks=1) # 04172018 @ 2:50 PM Changed to 2 clicks.
        time.sleep(3.0) # changing from 4.0 to 3.0
        
        pyautogui.moveTo(895,343)
        pyautogui.click(clicks=2) # 04172018 @ 2:50 PM Changed to 2 clicks.
        Total_Billable_Field = pyautogui.locateCenterOnScreen("Total_Billable_Field.png", grayscale=True)
        while Total_Billable_Field == None:
            Total_Billable_Field = pyautogui.locateCenterOnScreen("Total_Billable_Field.png", grayscale=True)
        print("Still searching for Total_Billable_Field...")
        print("Center of Total_Billable_Field is located at {0}".format(Total_Billable_Field))
        time.sleep(1.5)
        pyautogui.moveTo(Total_Billable_Field)
        time.sleep(1.5)
        pyautogui.click(clicks=2)
        time.sleep(1.5)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('ctrl', 'c')

        
        try:
            Total_Concession_Amount_Validation = float(pyperclip.paste())
            time.sleep(2.0)
            print(Total_Concession_Amount_Validation)
        except:
            print("ValueError Alert!")
            #Error_Alert(text="Please correct, then press 'OK'", title="ValueError Alert:", button='OK')
            time.sleep(20)

        if Total_Concession_Amount == Total_Concession_Amount_Validation:
            pass #when I had break here a matching value exited the program...investigating

        else:
            pyautogui.press(['delete', '0','tab', 'tab', 'tab'])
            time.sleep(1.0)
            pyautogui.pause = 0.5
            pyautogui.press(['tab', 'tab', 'down', 'tab'])
            time.sleep(2)
            Update_Button_Gray = pyautogui.locateCenterOnScreen("Update_Button_Gray.png", grayscale=True)
            while Update_Button_Gray == None:
                Update_Button_Gray = pyautogui.locateCenterOnScreen("Update_Button_Gray.png", grayscale=True)
            print("Still searching for Update_Button_Gray...")
            pyautogui.moveTo(Update_Button_Gray)
            pyautogui.click(clicks=1)

    time.sleep(2.0)
    pyautogui.press(['tab', 'tab', 'tab', 'tab', 'tab', 'down', 'down', 'down', 'down', 'down', 'down', 'tab'])
    time.sleep(2.0)

    Update_Button_Gray_2 = pyautogui.locateCenterOnScreen("Update_Button_Gray_2.png", grayscale=True)
    while Update_Button_Gray_2 == None:
        Update_Button_Gray_2 = pyautogui.locateCenterOnScreen("Update_Button_Gray_2.png", grayscale=True)
        print("Still searching for Update_Button_Gray_2...")

    pyautogui.moveTo(Update_Button_Gray_2)
    pyautogui.click(clicks=1)
    time.sleep(3.0) # changing from 4.0 to 3.0

    for i in range (0,4):
        Resolution_Code_Alert = pyautogui.locateCenterOnScreen("Resolution_Code_Alert.png", grayscale=True)
        
    if Resolution_Code_Alert != None:
        Resolution_Code_Alert = pyautogui.locateCenterOnScreen("Resolution_Code_Alert.png", grayscale=True)
        print("Center of Resolution_Code_Alert is located at {0}".format(Resolution_Code_Alert))
        OK_Button_Blue = pyautogui.locateCenterOnScreen("OK_Button_Blue.png", grayscale=True)
        time.sleep(2.0)
        pyautogui.moveTo(OK_Button_Blue)
        pyautogui.click(clicks=1)
        
    else:
        continue

    time.sleep(3.0) # changing from 4.0 to 3.0
    pyautogui.moveTo(1591,274)
    pyautogui.click(clicks=1)
    time.sleep(0.5)
    pyautogui.dragTo(1591, 505, 2, button='left')
    time.sleep(1.5)
    Resolution_Button_Gray = pyautogui.locateCenterOnScreen("Resolution_Button_Gray.png", grayscale=True)
    while Resolution_Button_Gray == None:
        Resolution_Button_Gray = pyautogui.locateCenterOnScreen("Resolution_Button_Gray.png", grayscale=True)
        print("Still searching for Resolution_Button_Gray...")
            

    pyautogui.moveTo(Resolution_Button_Gray)
    pyautogui.click(clicks=1)
    time.sleep(3.0)
    Resolution_Code_Field = pyautogui.locateCenterOnScreen("Resolution_Code_Field.png", grayscale=True)
    time.sleep(2.0) # changing from 3.0 to 2.0
    pyautogui.moveTo(Resolution_Code_Field)
    pyautogui.click(clicks=2)
    time.sleep(2.0)
    pyautogui.pause = 0.5
    pyautogui.press(['down', 'down', 'down', 'tab'])
    Update_Button_White = pyautogui.locateCenterOnScreen("Update_Button_White.png", grayscale=True)
    time.sleep(2.0) # changing from 3.0 to 2.0
    pyautogui.moveTo(Update_Button_White)
    time.sleep(1.0)
    pyautogui.click(clicks=1)
    time.sleep(2.0)
    
phase +=1  ##Phase 3
cycle(phase)
   

pyperclip.copy("") # Clears Clipboard
print("Clipboard cleared")
now = datetime.datetime.now()
print(str(now))
Run_Time = ((time.time() - Start_Time) / 60)
print("Program Run Time = %s seconds " % (time.time() - Start_Time))
print("Program Run Time = {0} minutes ".format(Run_Time))



phase +=1  ##Complete
cycle(phase)

exit()
