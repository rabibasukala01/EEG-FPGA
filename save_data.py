# Function: record the data from the electrode 
# pynq-3.0.1
import os
import time
import numpy as np
from playsound import playsound
PATH_OF_SOUND=os.path.join(os.getcwd(),"assets","sounds", "beep.wav")


# PYNQ overlays and setup
# from pynq import overlay, allocate
# from pynq.overlays.xadc_scope import xadc_scopeOverlay
# overlay = xadc_scopeOverlay('xadc_scope.bit')
# dma = overlay.axi_dma
# input_buffer = allocate(shape=(128,), dtype=np.uint16)



ACQTIME = 2  # seconds

name=input('Please enter your name :  ')


# folders config
MAIN = os.path.join(os.getcwd(), "data")
os.makedirs(MAIN, exist_ok=True)
try:
    subdir = os.path.join(os.getcwd(), "data", name)
    os.makedirs(subdir)
    print(f"Directory {subdir} created")
except:
    print('The Name already exists,Try another name.')
    exit()



while True:            #continue taking data for number of times until user wants
    data=[]

    # Recording of data starts here
    print(f"Collecting data from XADC in 2 sec ...")
    time.sleep(2)
    print("Recording started ...")
    # Set the start time using perf_counter
    start_time = time.perf_counter()

    # Run the loop for ACQTIME seconds
    while time.perf_counter() - start_time < ACQTIME:

        # dma.recvchannel.transfer(input_buffer)
        # dma.recvchannel.wait()
        # data.append(list(input_buffer))
      pass
        
    playsound(PATH_OF_SOUND)

    # flattened the data
    flat_list = [item for sublist in data for item in sublist]
    print("\nflattening the data ... ")

    # enter the wavetype and number of last run
    while 1:
        wavetype=input("Enter the wavetype and number of last run :eg: Type(t1/n1) : ")   #thinking or not thinking
        if wavetype.lower().startswith('t') or wavetype.lower().startswith('n'):
            break
        print("Enter the correct format")



    # name of file to save recorded data
    filename_to_save=os.path.join(os.getcwd(),"data",name, f"{name}{wavetype.upper()}.npy")

    # Save the array 
    np.save(filename_to_save, data)
    print("Saving the data ... ")
    print(f"Done!,check {filename_to_save}")
    print()
    
    
    if  input("Press <Enter> to continue adding  and 'q' to terminate :").lower() == "q":
        print("BYE")
        break    
