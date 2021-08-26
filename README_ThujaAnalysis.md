## README for all Analysis with Thuja plicata

1. IpyradThuja/
	1.1 DESCRIPTION: Assembly of ddRADseq data using ipyrad
	1.2 FILES
		ThujaAssemblyNov12.ipynb  ## Main Jupyter notebook has walk through of all assembly steps and parameters used
		## sequence (fastq.gz) files available only on dryad @ doi link tbd
		thuja_R1_lib1.fastq.gz	  ## Raw Sequence file for first ddRADseq library, 50 bp SR reads from Illumina HiSeq 2500 (Sept 2017)
		thuja_R1_lib2.fastq.gz    ## Raw Sequence file for first ddRADseq library, 50 bp SR reads from Illumina HiSeq 2500 (April 2019)
		barcodes_lib1.txt         ## barcodes paired with Accession IDS for library 1
		barcodes_lib2.txt         ## barcodes paired with Accession IDS for library 2
		Assembly_Noc12_part2_concurrent.ipynb  ## Jupyter notebook of demultiplex for library 2
		mergedThuja_minsamp4.json ## json file of this assembly
		mergedThuja_minsamp10.json ## json file of this assembly
		mergedThuja_minsamp25.json ## json file of this assembly
		OutputFiles.tar.gz        ## tar directories of output files
			mergedThuja_minsamp4/*    ## output files from ipyrad for assembly with loci present at least 4 samples
			mergedThuja_minsamp10/*    ## output files from ipyrad for assembly with loci present at least 10 samples
			mergedThuja_minsamp25/*    ## output files from ipyrad for assembly with loci present at least 25 samples
			## output format details here https://ipyrad.readthedocs.io/en/master/output_formats.html?highlight=output 	
	## All other intermediate assembly files (including .jsons) can be reproduced using the above files 

2. IpyradTsuga/
	1.1 DESCRIPTION: Assembly of ddRADseq data using ipyrad
	1.2 FILES
		ThujaAssemblyNov12.ipynb  ## Main Jupyter notebook has walk through of all assembly steps and parameters used
		## sequence (fastq.gz) files available only on dryad @ doi link tbd
		## All tsuga libraries were prepared at the same time
		tsuga_R1_lib1.fastq.gz  
		tsuga_R1_lib2.fastq.gz
		tsuga_R1_lib3.fastq.gz
		tsuga_R1_lib4.fastq.gz
		tsuga_R2_lib1.fastq.gz
		tsuga_R2_lib2.fastq.gz
		tsuga_R2_lib3.fastq.gz
		tsuga_R2_lib4.fastq.gz
		barcodes_lib1.txt 
		barcodes_lib2.txt 
		barcodes_lib3.txt 
		barcodes_lib4.txt 
		OutputFiles.tar.gz        ## tar directories of output files
			AllTsugaLibs_outfiles_minsamp4/*    ## output files from ipyrad for assembly with loci present at least 4 samples
	## All other intermediate assembly files (including .jsons) can be reproduced using the above files 

3. SubsamplingSFS
	subsampleSFS.py  ## This function is used to subsample SNPS from a VCF file repeatedly
	CheckSNPS_ParamEstsjAFS.ipynb
	PlottingPreviewForSubsamplingSFS.ipynb
	SubsamplingSFSscript.ipynb    ## main notebook to do subsampling and sfs construction

4. Structure
	ThujaStructure.ipynb   ## notebook to do entire Structure analysis
	TsugaStructure.ipynb   ## notebook to do entire Structure analysis

5. DelimitR
	## Thuja
		Models/    ## directory includes all demographic model files, .tpl and .est for fastsimcoal2 simulations
		DelimitR_Thuja_Anlaysis.ipynb   ## main jupyter notebook with walkthrough delimitR analysis
		editTPLscript.ipynb       ## short notebook to edit all tpl files when changing sample size
		plotting.ipynb     ## script for plotting SFS
		MakeSummarizedBinnedObserved.ipybn    ##script to summarize SFS for plotting
		
	## Tsuga
		TPLfiles/  ## directory includes .tpl files for demo models
		EstFiles/  ## directory includes .est files for demo models
		TsugaDelimitRAnlaysis.ipynb   ## main jupyter notebook with walkthrough delimitR analysis
		editTPLscript.ipynb       ## short notebook to edit all tpl files when changing sample size
		plotting.ipynb     ## script for plotting SFS

		
		
		
		
		