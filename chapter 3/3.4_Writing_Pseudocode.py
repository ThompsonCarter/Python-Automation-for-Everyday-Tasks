# Example of pseudocode:
START
CONNECT to email server
SEARCH inbox for subject "Weekly Sales"
IF email found THEN
    DOWNLOAD first .csv attachment to temp folder
    OPEN spreadsheet app
    IMPORT csv into new sheet
    SORT sheet by column "Region" descending
    SAVE as "Report_{today}.xlsx"
    COMPOSE email to team with attachment
    SEND email
ELSE
    LOG "No report found" with timestamp
END IF
END