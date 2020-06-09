# Transport-Management-System

A database architecture for SG Transport using pyQT for UI and SQLite for data management. We are using SQLite as being server-less it makes our app independent since it does not require any set-up to work, that is one can just install it and start working.

## Installing Dependencies

pip3 install PyQt5==5.14.2

## TODO List

The list below is in the order of decreasing priority therefore please focus on the first one for the time being.

1. Vehical-Repair-Management : A tool to track the repairing and maintenance cost of every vehical. This will help is calculating the cost effeciency of each vehical and help in making Important future decisions regarding the vehical. The back-end implementation of this can be done in 3 ways:
    1. Have different tables for every vehical.
    2. Have only one common table for every vehical.
    3. Have both 1 and 2.
Currently it's decided to implement the 2nd approach but instead of having just one table we'll have separate table for each years logs. That is each table will contain data of all the repairing and maintenance that happened that particular year.

1. Job-Management : A tool to track the jobs and movement of all the vehicals. Implementation needs further discussions

2. Bill-Generation-Tool : This will automate the Entries to Job-Management.

3. Maintenance-Suggester : A tool which uses Machine-Learning to suggest when a vehical should next go for maintenance using the jobs/movement and repairing/maintenance history of the vehical.

# TMS-Server
Backend system of Transport-Management-System


## Using Server SDK

first of all run the server from ```https://github.com/ShubhamPandey28/TMS-Server.git```
 by following the guidelines

You can find SDK(Software Development Kit) of this server in ```server/utils.py```