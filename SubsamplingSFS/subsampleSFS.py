#!/usr/bin/env python

import os
import easySFS

## This function is used to subsample SNPS from a VCF file repeatedly
##     for a set number of individuals from each popoulation; only works with 2 populations

def subsampleSFS(infile, popfile, sumfile, reps=1, pop1size=10, pop2size=10):
            
        summaryOutputfile = open(sumfile, "w+")
        summaryOutputfile.write(str(reps)+" observations\n2\t"+str(pop1size)+"\t"+str(pop2size)+"\n")
        
        for i in range(1, reps+1, 1):
            
            #print("Subsampling the SFS number "+str(i))
            out = "output_"+str(i)
            ## create the easySFS.py command to run in the terminal
            cmd = "./easySFS.py -i "+ infile+ " -p "+popfile+" --proj="+str(pop1size)+","+str(pop2size)+" -o "+out
            print(cmd)
            os.system(cmd)
        
        print("Finished subsampling...now compiling results")
        
        for i in range(1, reps+1, 1):
            print("compiling SFS "+str(i))
            
            ## locate the output file, open, combine all of the lines and add it to the output file
            jSFSfileName = infile.split(".")[0]+"_jointMAFpop1_0.obs"
            outFolder = "./output_"+str(i)
            pathtojSFS_File = os.path.join(outFolder, "fastsimcoal2", jSFSfileName)
            print(pathtojSFS_File)
            jSFSfile = open(pathtojSFS_File, "r")

            ##get ride of first two lines
            allLines = jSFSfile.readlines()
            allLines = allLines[2:]
            #print(allLines)

            for line in allLines:
                rows = line.split("\t")[1].strip()
                #print(rows)
                sites = rows.split(" ")
                for singleSiteFreq in sites:
                    #print(singleSiteFreq+"\t")
                    summaryOutputfile.write(singleSiteFreq+"\t")
 
            ## add return for each SFS flattened
            summaryOutputfile.write("\n")
        
        ## at the very end, delete the output directories
        rmcmd = "rm -rf output_*"
        os.system(rmcmd)
  
def main(): 
    subsampleSFS("AllTsugaLibs.vcf","popFile.txt", "jSFS_dataset6.obs", reps=100, pop1size=16, pop2size=27)

if __name__ == "__main__":
    main()