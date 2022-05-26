# _Google Big Query loader_

#### By _**Jarret Jeter**_

#### _A project showing an example of extracting a csv from a location, performing some transformations on it, and loading it into a Google Big Query table_

## Technologies Used

* _Python_
* _Pandas_
* _Big Query_
* _SQL_

## Description

_I've downloaded a csv containing data of the ancient Roman emperors from kaggle.com. I needed to do transformations such as drop certain columns from the csv and convert data types so that I could properly load it to google big query_

## Setup/Installation Requirements

* _Make sure you have a text editor such as Visual Studio Code installed.
* _Have a running version of Python3.7
* _Clone this repository (https://github.com/jarretjeter/Google-Big-Query-Loader.git) onto your local computer from github_
* _From the data folder, run the get_csv.sh script to download the the csv from google cloud storage_
* _If you haven't already, I would recommend reading the Google Cloud (https://console.cloud.google.com) documentation for setting up a project and your google credentials so that you can load the file to server_
* _In the main.py file you will want to change some variable values such as project_id to match the project on the google cloud storage that you own, dataset.location if you want to change what server location it will be downloaded to._
* _With Python run the main.py file to carry out the transformations and create and load into a google big query dataset_
* _You can check big query in you gcs and run some sql commands on the table. I've included some in the sql file you can try._

## Known Bugs

* _No bugs, but at this time it was too difficult for me to convert the Birth, Death, Reign_Start and Reign_End datetime values into more useable ones for querying_

## License

_If you have any questions, please email me at jarretjeter@gmail.com_

[MIT](https://github.com/jarretjeter/Google-Big-Query-Loader/blob/main/LICENSE.txt)

Copyright (c) _5/17/2022_ _Jarret Jeter_