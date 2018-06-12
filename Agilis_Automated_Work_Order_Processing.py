#! python3

## This program uses gui automation to perform work order processing operations within Agilis. Agilis is a Medical Equipment
## Management software built off of the ServiceNow platform. 
## The program can be inititated once the user is logged in and viewing a work order listing. 


import pyautogui, sys, time, datetime, pyperclip, webbrowser



phase = 0

def cycle(phase, space = 76, character = "*"):
    """Provides visual feedback of distinct program phases in console window for review and troubleshooting purposes."""


    phase = int(phase)
    if phase == 0:
        Start = "START"
        print(Start.center(space, character))
    elif 0 < phase < 3:
        Sequence = "PHASE_" + str(phase)
        print(Sequence.center(space, character))
    elif phase == 3:
        Summary = "SUMMARY"
        print(Summary.center(space, character))
    else:
        Complete = "COMPLETE"
        print(Complete.center(space, character))

  
def referenceImage (image, x_adj = 0, y_adj = 0):
    """Takes a given image and returns a reference point relative to that image based on the x and y coordinate adjustments provided."""

    refStartPoint = pyautogui.locateOnScreen("{0}.png".format(image), grayscale=True)
    while refStartPoint == None:
        refStartPoint = pyautogui.locateOnScreen("{0}.png".format(image))
        print("Searching for {0}...".format(image))

    refStartPoint_X, refStartPoint_Y = pyautogui.center(refStartPoint)
    refLocation = (refStartPoint_X + x_adj, refStartPoint_Y + y_adj)
    return refLocation
    

def chooseImage (image_1, image_2):
    """Searches for the appearence of two potential images and returns the location of the one that appears.""" 
    
    imageLocation_1 = pyautogui.locateCenterOnScreen("{0}.png".format(image_1), grayscale=True)
    imageLocation_2 = pyautogui.locateCenterOnScreen("{0}.png".format(image_2), grayscale=True)
    while imageLocation_1 == None and imageLocation_2 == None:
        imageLocation_1 = pyautogui.locateCenterOnScreen("{0}.png".format(image_1), grayscale=True)
        imageLocation_2 = pyautogui.locateCenterOnScreen("{0}.png".format(image_2), grayscale=True)
        print("Searching for {0} or {1}...".format(image_1, image_2))
    if imageLocation_1 != None:
        return imageLocation_1
    elif imageLocation_2 != None:
        return imageLocation_2
               

def findImage (image):
    """Finds a given image on screen and returns the coordinates of the center point of that image."""

    imageLocation = pyautogui.locateCenterOnScreen("{0}.png".format(image), grayscale=True)
    while imageLocation == None:
        
        imageLocation = pyautogui.locateCenterOnScreen("{0}.png".format(image), grayscale=True)
        print("Searching for {0}...".format(image))
        
    return imageLocation

def ConditionalImageSearch (image1, image2):
    """Searches for image that only occurs when certain conditions are met. Returns alternate values based on if given conditional image appears or not."""

    for i in range (0,3):
        ConditionalImage1Location = pyautogui.locateCenterOnScreen("{0}.png".format(image1), grayscale=True)

     
    if ConditionalImage1Location == None:
        print("{} not found".format(image1))
        return "Proceed to next Work Order Session" 


    elif ConditionalImage1Location != None: # Alert is found
   
        printImageLocation((image1), (ConditionalImage1Location))
        pyautogui.moveTo(ConditionalImage1Location)
        for i in range (0,3):
            ConditionalImage2Location = pyautogui.locateCenterOnScreen("{0}.png".format(image2), grayscale=True)
        
        printImageLocation((image2), (ConditionalImage2Location))
        pointAndClick(ConditionalImage2Location, 1)
        return "Cycle back through this Work Order"    

def printImageLocation (imageName, coordinates):
    """ Prints the coordinates of a selected image to the console screen for tracking and troubleshooting purposes."""

    print("Center of {0} is {1}".format(imageName, coordinates))
    return

def pointAndClick (coordinates, clickCount):
    """Moves mouse to given coordinates and clicks on the desired location."""

    pyautogui.moveTo(coordinates)
    pyautogui.click(clicks=clickCount)
    time.sleep(0.6) # Pausing less than .5 seconds increases liklihood of program errors. 
    return

def scrollDown ():
    """Performs a downward scrolling operations specific to the needs of the program within the Agilis window."""

    pyautogui.moveTo(1591,274)
    time.sleep(1.0)
    pyautogui.click(clicks=1)
    time.sleep(0.5)
    pyautogui.dragTo(1591, 480, 2, button='left') 
    time.sleep(0.5)
    return

def identifySession ():
    """Gathers key work order identifiers and outputs them to the console"""
    
    time.sleep(1.5)
    pyperclip.copy("") # Clears Clipboard
    pyautogui.hotkey('ctrl', 'c')
    AssetNumber = (pyperclip.paste())
    print("Asset Number: {}".format(AssetNumber))
    pyautogui.hotkey('shift', 'tab')
    time.sleep(1.0)
    pyautogui.hotkey('ctrl', 'c')
    WorkOrderNumber = (pyperclip.paste())
    print("Work Order Number: {}".format(WorkOrderNumber))
    pyperclip.copy("") # Clears Clipboard
    print("Clipboard cleared")
    identifylist = [WorkOrderNumber, AssetNumber]
    return identifylist

def SessionHome ():
    """This function returns cursor to the home position for a given work order"""

    for i in range (0,5):
        pyautogui.hotkey('shift', 'tab')
    return


cycle(phase) ##Start

now = datetime.datetime.now()
print(str(now))


phase +=1 ##Phase 1
cycle(phase) 


Entry_Date = (now.strftime("%m/%d/%Y")) 
print("Entry Date = " + Entry_Date)





pyperclip.copy("") # Clears Clipboard
promptData = pyautogui.prompt(text='How Many Work Order Update Sessions do you want to run?', title='WORK ORDER COUNT' , default='5') 
type(promptData)
print("{} work order sessions requested".format(promptData))
Start_Time = time.time()
print("Start Time = {}".format(Start_Time))
pyperclip.copy("") # Clears Clipboard
print("Clipboard cleared")

phase +=1 ##Phase 2
cycle(phase)

session = 0 # Identifies the # of unique work order sessions are processed
lineItemCycle = 0 # Identifies the # of times a work order is cycled through depending on how many billable line items there are
Total_Concession_Amount = 0
SessionInfo = []
TotalSessionInfo = []


i = 0
WorkOrderCount = int(promptData)

while i < WorkOrderCount:

    session += 1
    print("Work Order Session {} Initiated".format(session).center(76, "-"))

        
    pyautogui.pause = 0.2
    time.sleep(0.7)
    pointAndClick((327,271), 1) # Creates a home position for mouse cursor on each session
    

    Work_Order_Reference_Icon = referenceImage("Work_Order_Reference_Icon", 110, 0)
    printImageLocation(("Work_Order_Reference_Icon"),(Work_Order_Reference_Icon))
    pointAndClick((Work_Order_Reference_Icon), 1)
    time.sleep(1.0)

    MultipleBillablesSameWorkOrder = True

    while MultipleBillablesSameWorkOrder == True:

        lineItemCycle += 1
        print("Addressing Line Item # {}".format(lineItemCycle).center(76, "-")) 

        Asset_Label = findImage("Asset_Label") # Makes sure work order page has loaded before proceeding
        printImageLocation(("Asset_Label"),(Asset_Label))
        SessionInfo = identifySession()

        #scrollDown ()
        pyautogui.press('pgdn')


        Work_Order_Itemized_Cost = chooseImage("Work_Order_Itemized_Cost", "Work_Order_Itemized_Cost_HL")
        printImageLocation(("Work_Order_Itemized_Cost"),(Work_Order_Itemized_Cost))
        pointAndClick((Work_Order_Itemized_Cost), 1)



        Exclamation_Point_Icon = findImage("Exclamation_Point_Icon")
        printImageLocation(("Exclamation_Point_Icon"),(Exclamation_Point_Icon))
        pointAndClick((Exclamation_Point_Icon), 1)
        
        time.sleep(2.5)
        pointAndClick((895,343), 1)

  
        Total_Billable_Field = findImage("Total_Billable_Field")
        printImageLocation(("Total_Billable_Field"),(Total_Billable_Field))
        pointAndClick((Total_Billable_Field), 2)


        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('ctrl', 'c')
        pyautogui.press(['delete', '0','tab', 'tab', 'tab'])

        time.sleep(1.0)

        try:
            Concession_Amount = float(pyperclip.paste())


        except:
            Concession_Amount = float(pyautogui.prompt(text='Adjust the Total Billable Amount in Agilis and enter the correct amount for concessions here.', title='Type Error' , default='0'))
            pass

        
        Total_Concession_Amount += Concession_Amount
        print("Concession amount is ${:.2f}".format(Concession_Amount))
        pyperclip.paste()
        pyautogui.pause = 0.2
        pyperclip.copy("") # Clears Clipboard
        pyautogui.press(['down', 'down', 'down', 'tab', 'tab', 'down', 'tab'])
        time.sleep(1.0) 

        SessionInfo.append(Concession_Amount)
        TotalSessionInfo.append(SessionInfo)
        Update_Button_Gray = findImage("Update_Button_Gray")
        printImageLocation(("Update_Button_Gray"),(Update_Button_Gray))
        pointAndClick((Update_Button_Gray), 1)

 
        Work_Completed_Selection = findImage("Work_Completed_Selection")
        printImageLocation(("Work_Completed_Selection"),(Work_Completed_Selection))
        pointAndClick((Work_Completed_Selection), 1)

        time.sleep(1.0)
        pyautogui.press(['down', 'down', 'down', 'down', 'down', 'down', 'tab'])
        time.sleep(0.5)
        

        Update_Button_Gray_2 = findImage("Update_Button_Gray_2")
        printImageLocation(("Update_Button_Gray_2"),(Update_Button_Gray_2))
        pointAndClick((Update_Button_Gray_2), 1)


        time.sleep(1.2) 

        oneOrMany = " "
        oneOrMany = ConditionalImageSearch("Manager_Review_Alert", "OK_Button_Blue")
        print(oneOrMany)
        if oneOrMany == "Cycle back through this Work Order":
            MultipleBillbablesSameWorkOrder = True
            SessionHome()
            continue 
        elif oneOrMany == "Proceed to next Work Order Session":
            MultipleBillbablesSameWorkOrder = False
            WorkOrderCount -= 1
            break 
 
    time.sleep(0.5) 


    
phase +=1  ##Phase 3
cycle(phase)
   

pyperclip.copy("") # Clears Clipboard
print("Clipboard cleared")
now = datetime.datetime.now()
print(str(now))
Run_Time_Seconds = ((time.time() - Start_Time))
Run_Time_Minutes = ((time.time() - Start_Time) / 60)
Run_Time_Average_Minutes = float(Run_Time_Minutes) / float(lineItemCycle)
Run_Time_Average_Seconds = float(Run_Time_Minutes * 60) / float(lineItemCycle)
print("Program Run Time = {:.2f} minutes ".format(Run_Time_Minutes))
print("Average Run Time = {:.2f} minutes / cycle".format(Run_Time_Average_Minutes))
print("Program Run Time = {:.2f} seconds ".format(Run_Time_Seconds))
print("Average Run Time = {:.2f} seconds / cycle".format(Run_Time_Average_Seconds))
print("{0} Work Orders were advanced to 'Ready to Post' Status".format(promptData))
print("{0} Line Items were processed".format(lineItemCycle))
print("Total Amount Zeroed = ${:.2f}".format(Total_Concession_Amount))
print(TotalSessionInfo)



phase +=1  ##Complete
cycle(phase)

import HTC_Automation_Suite
#exit()
