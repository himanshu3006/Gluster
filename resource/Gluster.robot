*** Settings ***
Documentation    A test suite with multiple test for Gluster install, Trigger fio and uninstall gluster
...
...              Installing gluster and verify it by gluster status
...              Triggering fio commands and after completion deleting or uninstalling gluster

Library          OperatingSystem
Library          ../lib/create_gluster.py
Library          ../lib/Test.py

*** Variables ***
#Here dont use any variables
*** Test Cases ***
TC-58: Gluster_Cre_Status
    [Tags]    Validate the create gluster and validate the status
    Execute cammand to install gluster
    Get the status of gluster
    
TC-59: Gluster_Trigger_fio
    [Tags]    Validate the create gluster and trigger fio command
    Execute cammand to install gluster
    Trigger fio comands
    

TC-60: Gluster_project Verified and Rechecked for import and export data
    [Tags]    Validate project is Verified and Rechecked
    Get the status of gluster
    Rechecking project from system
    Exporting project from system
    Importing project from system    

TC-61: Gluster_project Insert and Collect data
    [Tags]    Validate project is Insert and Collect data
    Execute cammand to install gluster
    Inserting data from system
    Add new project in the Gluster
    Pushing new job in the Project

TC-62: Gluster_project Removed and Update
    [Tags]    Validate project is Removed and Update
    Removing project from system
    Updating project from Gluster
    Changing job from project
    Upgrading project from system
    

TC-63: Gluster_project Download and Edit
    [Tags]    Validate project is Download and edit is done
    Download project from Gluster
    Copying project from system
    Editing data from system
    Refreshing data from Gluster
    
*** Keywords ***
Execute cammand to install gluster
    [Documentation]  Installing Gluster please wait...
    install__gluster
    
Get the status of gluster
    [Documentation]  Getting Gluster current status
    getting__status
    
Trigger fio comands
    [Documentation]  Triggering IO commands
    trigger__fio
    
Verified project from system
    [Documentation]  Verified project please wait...
    verified__project
    
Rechecking project from system
    [Documentation]  Rechecking project please wait...
    rechecked__cli 
    
Inserting data from system
    [Documentation]  Inserting data please wait...
    insert__data
    
Collecting data from system
    [Documentation]  Collecting data please wait...
    collecting__data

Removing project from system
    [Documentation]  Removing project  please wait...
    remove__project

Download project from Gluster
    [Documentation]  Download  project  please wait...
    download__cli

Updating project from Gluster
    [Documentation]  Update project please wait...
    update__cli

Editing data from system
    [Documentation]  Editing data  please wait...
    editing__data

Add new project in the Gluster
    [Documentation]  Adding project please wait...
    add__newproject

Pushing new job in the Project
    [Documentation]  Pushing job please wait...
    push__newjob

Generating request from system
    [Documentation]  Generating request please wait...
    generate__req

Customizing project from system
    [Documentation]  Customizing please wait...
    customized__project

Pulling Request from Project
    [Documentation]  Pulling req please wait...
    pull__req

Exporting project from system
    [Documentation]  Exporting project please wait...
    export__project

Importing project from system
    [Documentation]  Importing project please wait...
    import__project

Unchecked data  from project
    [Documentation]  Unchecking data please wait...
    unchecked__data

Upgrading project from system
    [Documentation]  Upgrading project please wait...
    upgrade__project

Copying project from system
    [Documentation]  Copying project please wait...
    copy__project

Releasing project from system
    [Documentation]  Releasing project please wait...
    release__project

Changing job from project
    [Documentation]  Changing job from the project please wait...
    change__project

Refreshing data from Gluster
    [Documentation]  Refreshing data  please wait...
    refresh__data



