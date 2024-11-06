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

Once all your data files are accounted for, select the files you want to import into MAWA. Click the button that says Load selected NIDAP input data, which is the upper of the two middle buttons. You will know what the data is being loaded, because the widgets will grey out slightly and there is text in the top right corner that says running with a running figure. This goes for any action in MAWA. You know there are underlying processes being performed when you see this icon in the top right.


### Introduction to Neighborhood Profiles

When we were in the early stage of developing MAWA, we worked with Will Heinz of the OMAL group about how we might implement methods from a recent publication.

### MAWA Demo of Neighborhood Profiles

So, everything I recapped in the beginning are necessary steps to start using Neighborhood Profiles