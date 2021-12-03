# os is imported so that the file paths work.
import os
# Functuion that starts all of the python scritps.
def joblistmaster():
    try:
        os.system("C:\\Users\\short\\PycharmProjects\\ScrollerParser\\JobListScrollerMTP.py")
        print("MTP Scroller Script ran.")
        os.system("C:\\Users\\short\\PycharmProjects\\ScrollerParser\\JobListScrollerParis.py")
        print("Paris Scroller Script ran.")
        os.system("C:\\Users\\shortma1\\PycharmProjects\\ScrollerParser\\JobListScrollerSS.py")
        print("SS Scroller Script ran.")
        os.system("C:\\Users\\short\\PycharmProjects\\ScrollerParser\\JobListScrollerTXK.py")
        print("TXK Scroller Script ran.")
    except:
        print("An error occured creating Job Listing Page!")
    else:
        print("Success, all done!")
# Start Main 
if __name__ == '__main__':
    print("Call Job Scroller Scripts")
    joblistmaster()
    
