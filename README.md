# Stop Trigger Stop AWS Redshift After Working hours 20:00-08:00
Schedule expression: cron(0 17 ? * * *)
# start Trigger Resume AWS Redshift Working hours 08:00-20:00
Schedule expression: cron(0 1 ? * * *)
