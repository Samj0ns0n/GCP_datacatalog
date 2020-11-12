# Datacatalog Util  

A Python package to manage Google Cloud Data Catalog helper commands and scripts.

**Disclaimer: This is not an officially supported Google product.**

-----

## Execute Tutorial in Cloud Shell


<!--
  ⚠️ DO NOT UPDATE THE TABLE OF CONTENTS MANUALLY ️️⚠️
  run `npx markdown-toc -i README.md`.

  Please stick to 80-character line wraps as much as you can.
-->

## Table of Contents

<!-- toc -->

- [4. Load Templates from CSV file](#4-load-templates-from-csv-file)
  * [4.1. Create a CSV file representing the Templates to be created](#41-create-a-csv-file-representing-the-templates-to-be-created)
    + [4.1.1 Execute Tutorial in Cloud Shell](#411-execute-tutorial-in-cloud-shell)
  * [4.2. Run the datacatalog-util script - Create the Tag Templates](#42-run-the-datacatalog-util-script---create-the-tag-templates)
  * [4.3. Run the datacatalog-util script - Delete the Tag Templates](#43-run-the-datacatalog-util-script---delete-the-tag-templates)
- [5. Export Templates to CSV file](#5-export-templates-to-csv-file)
  * [5.1. A CSV file representing the Templates will be created](#51-a-csv-file-representing-the-templates-will-be-created)
    + [5.1.1 Execute Tutorial in Cloud Shell](#511-execute-tutorial-in-cloud-shell)
  * [5.2. Run the datacatalog-util script](#52-run-the-datacatalog-util-script)

<!-- tocstop -->

-----

## 0. Executing in Cloud Shell from PyPi
If you want to execute this script directly in cloud shell, download it from PyPi:

````bash
# Set your SERVICE ACCOUNT, for instructions go to 1.3. Auth credentials
# This name is just a suggestion, feel free to name it following your naming conventions
export GOOGLE_APPLICATION_CREDENTIALS=~/credentials/datacatalog-util-sa.json

# Install datacatalog-util
pip3 install --upgrade datacatalog-util --user

# Add to your PATH
export PATH=~/.local/bin:$PATH

# Look for available commands
datacatalog-util --help
````

## 1. Environment setup for local build

### 1.1. Python + virtualenv

#### 1.1.1. Install Python 3.6+

#### 1.1.2. Get the source code
```bash
git clone https://github.com/mesmacosta/datacatalog-util
cd ./datacatalog-util
```

_All paths starting with `./` in the next steps are relative to the `datacatalog-util`
folder._

#### 1.1.3. Create and activate an isolated Python environment

```bash
pip install --upgrade virtualenv
python3 -m virtualenv --python python3 env
source ./env/bin/activate
```

#### 1.1.4. Install the package

```bash
pip install --upgrade .
```

## 4. Load Templates from CSV file

### 4.1. Create a CSV file representing the Templates to be created

Templates are composed of as many lines as required to represent all of their fields. The columns are
described as follows:

| Column                 | Description                                    | Mandatory |
| ---                    | ---                                            | ---       |
| **template_name**      | Resource name of the Tag Template for the Tag. | Y         |
| **display_name**       | Resource name of the Tag Template for the Tag. | Y         |
| **field_id**           | Id of the Tag Template field.                  | Y         |
| **field_display_name** | Display name of the Tag Template field.        | Y         |
| **field_type**         | Type of the Tag Template field.                | Y         |
| **enum_values**        | Values for the Enum field.                     | N         |

#### 4.1.1 Execute Tutorial in Cloud Shell

[![Open in Cloud Shell](http://gstatic.com/cloudssh/images/open-btn.svg)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/Samj0ns0n/datacatalog-util-master&tutorial=tutorials/tag-templates/TUTORIAL.LOAD.md)


### 4.2. Run the datacatalog-util script - Create the Tag Templates

- Python + virtualenv

```bash
datacatalog-util tag-templates create --csv-file CSV_FILE_PATH
```

### 4.3. Run the datacatalog-util script - Delete the Tag Templates

- Python + virtualenv

```bash
datacatalog-util tag-templates delete --csv-file CSV_FILE_PATH
```

## 5. Export Templates to CSV file

### 5.1. A CSV file representing the Templates will be created

Templates are composed of as many lines as required to represent all of their fields. The columns are
described as follows:

| Column                 | Description                                    | 
| ---                    | ---                                            | 
| **template_name**      | Resource name of the Tag Template for the Tag. | 
| **display_name**       | Resource name of the Tag Template for the Tag. | 
| **field_id**           | Id of the Tag Template field.                  | 
| **field_display_name** | Display name of the Tag Template field.        | 
| **field_type**         | Type of the Tag Template field.                | 
| **enum_values**        | Values for the Enum field.                     | 

#### 5.1.1 Execute Tutorial in Cloud Shell

[![Open in Cloud Shell](http://gstatic.com/cloudssh/images/open-btn.svg)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/Samj0ns0n/datacatalog-util-master&tutorial=tutorials/tag-templates/TUTORIAL.EXPORT.md)


### 5.2. Run the datacatalog-util script

- Python + virtualenv

```bash
datacatalog-util tag-templates export --project-ids my-project --file-path CSV_FILE_PATH
```

# Original work  

Author : * Marcelo Miranda <mesmacosta@gmail.com>  
github : https://github.com/mesmacosta/datacatalog-util  


