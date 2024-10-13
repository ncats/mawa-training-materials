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

Here you will generally see four items:

* `input` is a folder where you place your datafiles, which can be `.csv`, `.tsv`, or `.txt`.
* `output` is a folder where MAWA will save its results.
* `MAWA App` is what you click on to start the app.
* `MAWA developer workspace` is reserved for admins and developers.

When you click into the `input` folder (generally, it helps to do this in a new tab by ctrl-clicking it), you will see something like this:

![input_folder](full/input_folder.png)

To upload your data into NIDAP, click on the Import button in the top right or drag and drop your datafile(s) into the window, resulting in a pop-up like this:

![import_data](reduced/import_data.png)

Make sure that "Add file(s)" is selected before you press the blue Next button to import your data into NIDAP.

Note that zipping of files is supported. E.g., you can optionally zip `myfile.csv` into `myfile.csv.zip` before uploading an individual file. Also note that datafiles are never modified by MAWA unless you explicitly overwrite a file, which is rare.

Other than the `input` folder, the only other item in the MAWA workspace that you will generally interact with is the `MAWA App`:

![mawa_app](reduced/mawa_app.png)

After clicking on it (again, it generally helps to do this in a new tab by ctrl-clicking it), the app will open in 2-6 minutes.
