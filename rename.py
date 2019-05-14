# Pythono3 code to rename multiple
# files in a directory or folder

# importing os module
import os

# Function to rename multiple files
def main():
    i = 0
    filedir = "/Users/rayd/Downloads/Downtown Gainesville 1950-1960/1965_s/"
    for filename in os.listdir(filedir):
        dst ="1021753940 FL_GAI_PlantSale" + str(i) + ".jpg"
        src = filedir + filename
        dst = filedir + dst

        # rename() function will
        # rename all the files
        os.rename(src, dst)
        i += 1

# Driver Code
if __name__ == '__main__':

    # Calling main() function
    main()
