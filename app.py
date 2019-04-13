from load import load_nvd
from load import loadingAnimation
from parser import cve_parse
import os 
import shutil






def logo():


    x=''' 
              
||||||||||||||||||||||||||||||||||||||||             ||||||||||||||||||||||||||||||||||||||||||||||||||
                          

     __     __           __                            __    __            __       
    /  |   /  |         /  |                          /  |  /  |          /  |      
    $$ |   $$ |__    __ $$ | _______    ______        $$ |  $$ | __    __ $$ |____  
    $$ |   $$ /  |  /  |$$ |/       \  /      \       $$ |__$$ |/  |  /  |$$      \ 
    $$  \ /$$/$$ |  $$ |$$ |$$$$$$$  | $$$$$$  |      $$    $$ |$$ |  $$ |$$$$$$$  |
     $$  /$$/ $$ |  $$ |$$ |$$ |  $$ | /    $$ |      $$$$$$$$ |$$ |  $$ |$$ |  $$ |
      $$ $$/  $$ \__$$ |$$ |$$ |  $$ |/$$$$$$$ |      $$ |  $$ |$$ \__$$ |$$ |__$$ |
       $$$/   $$    $$/ $$ |$$ |  $$ |$$    $$ |      $$ |  $$ |$$    $$/ $$    $$/ 
        $/     $$$$$$/  $$/ $$/   $$/  $$$$$$$/       $$/   $$/  $$$$$$/  $$$$$$$/  


                Company : 10XDS | Follow: http;//github.com/adhi1234                                                                
                                                                                
               |||||||||||||||||||||||    Created By R4ngtx   ||||||||||||||||||||||                                                               

      '''



    print(x)
                                                                                
                                                                                











if __name__ == "__main__":
    logo()

    print("Choose your option \n" )
    print(" 1. Download the CVE data ")
    print(" 2. Run the Parser")

    print(" 3. Get the STIX format")
    print(" 4. Erase the output log ")
    print(" 5. Update the Repository\n\n")



option=int( input("Enter the option from above "))


if(option==1):
    print("Downloading Data")
    loadingAnimation()
    load_nvd()
    

if(option==2):
    print("Parsing the database....") 
    cve_parse()

if(option==3):
    print("Under processing") 

if(option==4):
    print("Output file erased")

    

    f=open('parsed_file.json','r+')
    f.truncate(0)

if(option==5):
    cmd='cd nvd && rm -r *'
    os.system(cmd)  

        


    

