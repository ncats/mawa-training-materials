# Spatial Omics Data Analysis with MAWA

## Session 4: Neighborhood Analysis using Spatial UMAP

- [Spatial Omics Data Analysis with MAWA](#spatial-omics-data-analysis-with-mawa)
  - [Session 4: Neighborhood Analysis using Spatial UMAP](#session-4-neighborhood-analysis-using-spatial-umap)
  - [Session information](#session-information)
  - [Concepts](#concepts)
    - [Review Data Ingestion/Unification](#review-data-ingestionunification)
    - [Introduction to Neighborhood Profiles](#introduction-to-neighborhood-profiles)
    - [MAWA Demo of Neighborhood Profiles](#mawa-demo-of-neighborhood-profiles)

## Session information

- **Date**: Wed 11/06/24, 11 AM - 12 PM
- **Speaker**: Dante J Smith, Ph.D.
- **[Session information](https://bioinformatics.ccr.cancer.gov/btep/classes/spatial-omics-data-analysis-neighborhood-analysis-using-spatial-umap-mawa-4)**
- **[Main training page](https://github.com/ncats/mawa-training-materials/tree/develop)**
- **[Session slides](../session_4/Spatial%20Omics%20Data%20Analysis%20with%20MAWA%204.pdf)**
- **[Recording of session](https://cbiit.webex.com/cbiit/ldr.php?RCID=12b75c9528dfc122df185d93b9281af5)**
- All data generously provided by the David Wink lab

## Concepts

### Review Data Ingestion/Unification

![MAWA Welcome Screen](../session_4/images/MAWA_welcome.jpg)

When you first open MAWA, you are going to see a Welcome Screen that looks like this. To start your data ingestion journey, you will click on the button labeled *Data Import and Export*

![MAWA Import and Export](../session_4/images/MAWA_import.jpg)

At the top of the page, you will see two tables, one labeled as Available Input on NIDAP, and another labeled as Input Data in MAWA. There will be two buttons positioned between these tables. The table on the left displays all data available on NIDAP that could be imported in MAWA. Verify that you can find all your necessary files in this left-hand table. Recall that this table is displaying the csv files listed in this the input folder in the top-level folder on NIDAP.

![NIDAP input folder](../session_4/images/NIDAP_input.jpg)

This is what that folder looks like. You can see the app itself (red crown), the developer environment (white card), and then two data folders-the input folder and the output folder. If we look at the inside of the input folder, we can see several different files that have already been uploaded. Any time you want to add new data to this folder, you will do so in the input folder. You can drag and drop new files here. Once you do, you should be able to see them displayed in this left-hand table in the input MAWA page.

![MAWA Selected Input](../session_4/images/MAWA_input_select.jpg)

Once all your data files are accounted for, select the files you want to import into MAWA. Click the button that says Load selected NIDAP input data, which is the upper of the two middle buttons. You will know what the data is being loaded, because the widgets will grey out slightly and there is text in the top right corner that says running with a running figure. This goes for any action in MAWA. You know there are underlying processes being performed when you see this icon in the top right. Once the load step has been completed, verify that all your expected files appear in the right-hand table. With this step done, we can unify and preprocess our files.

![MAWA Datafile Unification](../session_4/images/MAWA_Datafile_Unification.jpg)

Select the page in the menu on the left titled *Datafile Unification*. You will see a table on the left with the files you want to use in your analysis. Select all or some of those files and click the button ‘Combine selected files into single dataframe’ to combine them.

![MAWA Datafile Unification2](../session_4/images/MAWA_Datafile_Unification2.jpg)

Follow the rest of the instructions on this page to fully clean and process your dataset. This includes:

- Step 2: Identifying rows with NA entries and removing them
- Step 3: Identifying a column that can be used to label the images in your dataset
- Step 4: Identifying a column which labels ROIs (if any)
- Step 5: Identifying the columns which describe the Cell coordinates
- Step 6: Identifying the column or columns which describe any pre-assigned phenotypes (if any)
- Step 7: Save a copy of the mawa_unified_datafile which is being created throughout this process. If you ever pause your analysis activities for the day and want to return to working on the same dataset, this unified_datafile will retain all the changes you made in this unification step. Make sure to upload back to NIDAP in the Data Import and Export Step

![MAWA Open File](../session_4/images/MAWA_openfile.jpg)

Once the unification step is done, and any unified files are done being saved, move to the next page from the menu on the left titled *Open File*. If you have just finished the datafile unification step, make sure the toggle is on to load the data that is still loaded on that page. If you are returning to analysis and are loading a unified_datafile, make sure the toggle is off and select your unified_datafile from the drop-down menu. In either case, click the load button to load your data into memory, and review your data in the preview at the bottom of the screen.

![MAWA Open File](../session_4/images/MAWA_Threshold_Intensity.jpg)

The final important step to perform before considering Neighborhood Profiles is the phenotyping step. MAWA offers a variety of different ways to apply phenotypes to the cells in your dataset. Because the dataset we are using already has Thresholded intensities, we can use the phenotyping method called Thresholded Intensities. In the left-hand menu, in the category called Phenotyping, select the page titled Using Thresholded Intensities. At the start, nothing should be loaded in the widgets and windows in the lower part of the page. Click the button in the top left titled Load Data. This will load the unified_dataset into this phenotyping page. You should see the tables and figures in the lower part of the page populate. There is a scatterplot on the left of one of your images. There is also a table on the right which describes the different species of cell that are present in this dataset. In the top right corner is a set of radio buttons to assign different types of phenotypes. For simplicity, I will not go into much detail about each, but for demo purposes, I will select the Species option. The species option will simply assign a phenotype name that is identical to the species of the cell. When this option is selected and applied, the tables and figure will be updated with the phenotype names. At this stage, we are ready to consider Neighborhood Profiles

### Introduction to Neighborhood Profiles

When we were in the early stage of developing MAWA, we worked with Will Heinz of the OMAL group about how we might implement methods from a recent publication.

### MAWA Demo of Neighborhood Profiles

So, everything I recapped in the beginning are necessary steps to start using Neighborhood Profiles. You need to have your data loaded into NIDAP, preprocessed using the Data Unifier, and phenotyped using at one of the many methods that MAWA has to offer. It is especially important that we are using spatial data (they x and y centroid locations), and a phenotype assigned to each cell.

![Neighborhood Profiles](../session_4/images/MAWA_NeighborhoodProfiles.jpg)

Once all that is completed, you will click on the tab on the left-hand side labeled as Neighborhood Profiles, under Neighborhood Profiles Workflow. From here, you will see a page that three buttons on the left hand side of the screen, and a message saying Step 1 please Perform Cell Density Analysis. If instead you see a message that says Step 0 please complete phenotyping, it might mean your dataset is not properly setup to perform Neighborhood Profiles. Above the message is a collapsable widget which holds settings for performing the Neighborhood Profiles. I am going to use the default values for now, but if anyone has questions about how these affect the analysis, and when they should be changed, we can talk about it after the talk.

![Neighborhood Profiles 2](../session_4/images/MAWA_NeighborhoodProfiles2.jpg)

We are going to start by hitting button #1 which is running the Cell Density Analysis. Once clicked, you will see a spinning wheel to indicate that this process is happening. For this demo dataset today, this should be completed in under 30s. The amount of time this takes will vary depending on the number of cells you have, the number of images in your sample, and the number of phenotypes selected on the previous step. When the cell density measure is complete, we will see a new message pop up telling us to complete Step 2, Complete UMAP analysis. All you need to do is click the button that says Perform UMAP analysis. Again, we are going to maintain the default values for this demo. This should take about 30-40s to complete. Again this amount of time will depend on the number of cells in your sample, the number of images, and the number of phenotypes.

![Neighborhood Profiles 3](../session_4/images/MAWA_NeighborhoodProfiles3.jpg)

When the UMAP is done, you will see a new message appear, and a new set of widgets and figures. The figure is a scatterplot of the 2D UMAP that has been created as a result of step 2. In reality its actually closer to a 2D histogram in which cells are placed into bins for common x and y values assigned during the spatial UMAP step. The intensity of the colors shows more cells aassigned to that bin. A settings window now appears on the left along with a message that says Step 3: Perform Clustering Analysis. Additionally, you will see a scatterplot of one of your images that is colored white for a No Cluster condition.

![Neighborhood Profiles 4](../session_4/images/MAWA_NeighborhoodProfiles4.jpg)

![Neighborhood Profiles 4b](../session_4/images/MAWA_NeighborhoodProfiles4b.jpg)

There are two ways to perform the clustering. The first one is very straight forward. Based on the UMAP figure you see on this page; it will perform k-means clustering on the non-empty bins for a given k that you set in the settings box below. This clustering step should take roughly 1min to complete. When it is done, you will see your scatterplot figure at the bottom of the screen colored by the clusters that were created by kNN. To the right you will also see the actual Neighborhood Profiles line plot. Here you can further investigate the make of your individual clusters, or even compare clusters. 

![Neighborhood Profiles 5](../session_4/images/MAWA_NeighborhoodProfiles5.jpg)
![Neighborhood Profiles 5b](../session_4/images/MAWA_NeighborhoodProfiles5b.jpg)
![Neighborhood Profiles 5c](../session_4/images/MAWA_NeighborhoodProfiles5c.jpg)

The second method is a bit nuanced, but it can lead to some interesting scientific discourse. If instead of performing K-mean clustering on the UMAP, instead, you can first split the UMAP figure, and its data, into two parts. By flipping the toggle here, you can select a feature by which to split the UMAP. The feature comes from your dataset and can be anything from survival after 5 years, to Cell area, to patient zip code. In the case of a binary feature like survival, you will see the values box default to 0 and 1. In the case of a numerical feature like Cell area, you will see the values split at the median by default. And for non-continuous numerical or string values, you are able to choose any two values to compare. This clustering method does not work if you have one or few unique values in the chosen feature. When this clustering step is selected, the following analyses are performed:

- The Full UMAP dataset is filtered by the feature at each of the two selected values. This creates a UMAP for a value 1 (False) and a UMAP for a value 2 (True).
- Next a difference is taken between the UMAP of value 2 subtracted from the UMAP of value 1. This creates a new 2D histogram as seen in the middle here where dark regions of red represent high cell counts of value 1, and dark regions of blue represent high cell counts of value 2. Lighter and white colors represent parts of the UMAP where there is not a strong preference towards value1 or value 2, and it’s more of a mix of the two values. This is called the Difference UMAP
- A mask is created of the Difference UMAP and only the most strong (dark) blue regions and the most strong (dark) red regions are selected out of the mask. Any lighter blue/red or white regions are masked out.
- From this mask, two separate kNN clustering analyses are performed; one on the red region (Left hand False condition), and on the blue region (Right hand True condition) of the masked difference UMAP. From each of these clustering steps, the algorithm returns separate clusters (False clusters & True clusters). You can tune the number of clusters produced for each set of False/True clusters.

