# Session 1: Introduction to NIDAP. MAWA fundamentals. Supervised phenotyping

## Session information

* **Date**: Tue 10/15/24, 1-2 PM
* **Speaker**: Andrew Weisman, Ph.D.
* **[Link](https://bioinformatics.ccr.cancer.gov/btep/classes/spatial-omics-data-analysis-introduction-to-nidap-and-mawa-fundamentals)**

## Introduction

MAWA (Multiplex Analysis Web Apps) is new, open-source software capable of performing file handling, phenotyping, and spatial analysis on segmented spatial transcriptomics/proteomics data. Implementing multiple published and novel methodologies, it is extremely performant and user-friendly, aiming to be accessible to users of all skill levels.

MAWA can be run either locally, requiring [installation](https://github.com/ncats/multiplex-analysis-web-apps/tree/develop), or on the cloud. Cloud options include the [NIH Integrated Data Analysis Platform (NIDAP)](https://nidap.nih.gov), which provides a secure, powerful environment for NIH researchers, and [Streamlit Community Cloud](https://nci-mawa.streamlit.app), which is open to the general public on a shared computing environment. Deployment on NIDAP will be the focus of this workshop. Deployment on Streamlit Community Cloud is brand new and requires a few more tweaks. All three deployment options share the same [codebase](https://github.com/ncats/multiplex-analysis-web-apps/tree/develop), so MAWA's features are consistent across all platforms.

## NIH Integrated Data Analysis Platform (NIDAP)

NIDAP's filesystem is organized into Projects, which usually corresponds to research groups. Each Project can contain both user data and instances of NIDAP applications. MAWA is an instance of the Code Workspaces application.

You can [explore MAWA in a public project](https://nidap.nih.gov/workspace/compass/view/ri.compass.main.folder.a50782c9-f612-4476-9633-49eb266dbaed), which will be used during this workshop. To create a secure deployment for your group, [contact us](mailto:andrew.weisman@nih.gov) to have MAWA set up in your project. Once set up, you will be given a URL to access your instance of MAWA, bringing you to a page that looks like this:

![mawa_on_nidap](full/mawa_on_nidap.png)

(Note it is recommended to use the Chrome web browser for NIDAP.)

Here you will generally see four items:

* `input` is a folder where you place your datafiles, which can be `.csv`, `.tsv`, or `.txt`.
* `output` is a folder where MAWA will save its results.
* `MAWA App` is what you click on to start the app.
* `MAWA developer workspace` is reserved for admins and developers.

When you click into the `input` folder (generally, it helps to do this in a new tab by `Ctrl`-clicking it), you will see something like this:

![input_folder](full/input_folder.png)

To upload your data into NIDAP, click on the Import button in the top right or drag and drop your datafile(s) into the window, resulting in a pop-up like this:

![import_data](reduced/import_data.png)

Make sure that "Add file(s)" is selected before you press the blue Next button to import your data into NIDAP.

Note that zipping of files is supported. E.g., you can optionally zip `myfile.csv` into `myfile.csv.zip` before uploading an individual file. Also note that datafiles are never modified by MAWA unless you explicitly overwrite a file, which is rare.

Other than the `input` folder, the only other item in the MAWA workspace that you will generally interact with is the `MAWA App`:

![mawa_app](reduced/mawa_app.png)

After clicking on it (again, it generally helps to do this in a new tab by `Ctrl`-clicking it), the app will open in 2-6 minutes.

As the app opens, if you see a glowing "Warnings" message in the top right, as below, do not worry about it (unless the adjacent number is greater than 1). In addition, if you do not see "Latest" as highlighted in the top left, you will see a prominent banner to restart the app to pick up the latest changes; if so, click on the restart link in the banner to do so:

![warnings](full/warnings.png)

## File handling

### Overview

Once the app is open, you will see a page like this:

![mawa_app_open](full/mawa_app_open.png)

Note the above screenshot has the NIDAP sidepanel on the left collapsed, which is done by clicking on the three horizontal lines in the top left. This is generally recommended to maximize the app's screen real estate.

If you click on "View 14 more" in the left sidebar, you will see a list of all the functionalities available in MAWA:

![mawa_functionalities](reduced/mawa_functionalities.png)

Clicking on each "page" will bring up a new page with a different set of functionalities. Today we will cover what is in green ("Week 1"), and we will cover the other pages in subsequent sessions.

Below the page listing are a few more items:

![additional_sidebar_items](reduced/additional_sidebar_items.png)

You will see three buttons and a dropdown menu in the App Session Management section. It is a good practice to occassionally press the Save button to save your work, particularly after performing a time-consuming operation. This will save the entire state of the app. When there are sessions that have been saved, they will be available in the dropdown menu "Session to load:". To load a session, select it from the dropdown and press the Load button. To reset the state of the entire app, press the Reset button.

Next, you will see a link for the MAWA documentation. Please keep in mind that the documentation is a work in progress.

Finally, you will see an "Advanced:" dropdown menu, reserved for developers and admins.

In the main part of the app, you will see the contents of the first page in the sidebar, which is the "Welcome" or "Home" page. Like the documentation, this page is a work in progress and is meant to provide a brief overview of the app.

### Data Import and Export

Now we want to load the data that we previously uploaded into the `input` folder. To do this, click on the "Data Import and Export" page in the sidebar:

![data_import_and_export](full/data_import_and_export.png)

You will see all available datafiles from the `input` folder listed in the "Available input data on NIDAP" table in the top left. To load datafiles for analysis from NIDAP to MAWA, select the datafiles you want to load by clicking on the checkboxes in the "Selected" column and "Load selected NIDAP input data" button.

While the data are being transferred (typically takes a few seconds), you will see the app partially grayed out and "RUNNING..." message in the top right. This is typical behavior while an operation is running in the app. Generally, you should not interrupt the process by pressing the Stop button in the top right:

![app_running](full/app_running.png)

After the data have been transferred, you will see the datafiles listed in the "Input data in MAWA" table in the top right:

![input_data_in_mawa](reduced/input_data_in_mawa.png)

We will return to this Data Import and Export page multiple times during this workshop.

### Datafile Unification

Next, we want to combine multiple datafiles into a single dataset, after which we want to perform some basic preprocessing to ensure the resulting dataset is compatible with the rest of the functionalities in MAWA. To do this, click on the "Datafile Unification" page in the sidebar:

![datafile_unification](full/datafile_unification.png)

Steps to perform on this page, in sequence, will be identified by bright blue numbers. In section "1: Select datafile(s)", we will select the datafiles we want to combine by clicking on the checkboxes in the "Selected" column and then pressing the "Combine selected files into single dataframe" button:

![combine_selected_files](reduced/combine_selected_files.png)

Note that if the selected datafiles do not have exactly the same columns, only the common set of columns will be used in the combined dataset. The excluded columns will be listed; if you don't see such a listing, then you know all selected datafiles have the same columns.

Upon pressing the button, you will see the rest of the sections on the page populate,

![datafile_unification_populated](full/datafile_unification_populated.png)

including a sample of the unified dataset at the bottom:

![unified_dataset](full/unified_dataset.png)

This preview (and the number of rows/columns above it) has two main purposes: (1) to serve as a sanity check that everything looks reasonable, and (2) to display the column names that will be needed for further processing on this Datafile Unification page. Note that this (and any) table of data are interactive and can be maximized by hovering over it and clicking on the maximize button in the top right:

![maximize_table](reduced/maximize_table.png)

In section "2: Delete null rows", press the "Detect null rows in each column" button to display the number of null rows in each column containing null values. If null data are detected in columns that you expect would be used in downstream analyses, you should delete the null values by expanding the "Click to expand:" dropdown and selecting one or more column names containing null values. (If you suspect all relevant columns contain the same null rows, you only need to select one of these columns.) Then press the "Delete rows from dataframe" button to delete the rows having null values in the selected columns. If rows were deleted, a message will display saying how many were deleted. You can confirm that the rows have been deleted by clicking again on the "Detect null rows in each column" button.

If no null rows are detected, you will see something like this:

![no_null_rows](reduced/no_null_rows.png)

Use the sample of the unified dataset at the bottom to identify a column(s) whose values uniquely identify the slides/images in the dataset. In section "3: Identify images", select the column name(s) from the dropdown menu and press the "Assign images" button. This will add a new column to the dataset containing the unique image IDs, as can be confirmed in the sample of the unified dataset at the bottom:

![assign_images](reduced/assign_images.png)

![assigned_images_sample](reduced/assigned_images_sample.png)

If your dataset contains a column that specifies regions of interest (ROIs) within the images, step "4: Identify regions of interest (ROIs)" allows you to select that column name by turning on the "Identify dataframe column that identifies ROIs" toggle. Most groups do not have such a column. In either case, the "Assign ROIs" button must be pressed:

![assign_rois](reduced/assign_rois.png)

Section "5: Identify coordinates" allows you to select the columns that contain the x and y coordinates of the cells/objects. If the dataset has already calculated the their locations using a single coordinate, then the "One column (centroid)" radio button should be selected. On the other hand, if the centroid has not already been calculated, and instead only the coordinates of the x and y bounding boxes for the cells are specified, then "Two columns (min and max)" should be selected. Regardless, the corresponding column names (which again can be determined from the dataset sample at the bottom) should be selected from the dropdown menus.

In addition, this is the place to specify the units of the coordinates in the dataset. In particular, a value should be entered identifying the number of microns per coordinate unit. E.g., if dataset units are in pixels, then the number of microns per pixel should be entered. If the coordinate units are already in microns, then this value should remain the default of 1.0.

After the coordinate columns and unit conversions have been specified, press the "Assign coordinates" button. This will add new columns to the dataset containing the x and y coordinates of the cells/objects, as can be confirmed in the sample of the unified dataset at the bottom:

![assign_coordinates](reduced/assign_coordinates.png)

![assigned_coordinates_sample](reduced/assigned_coordinates_sample.png)
