# Flask Login Monitor – Azure Monitor + KQL Alert Lab
## 📘 Overview
This solution explains how to code and deliver a small application using Python Flask and the Azure Monitor to log into authentication activity, and track real-time threat detection. The application tracks successful and unsuccessful attempts made to log in, suspicious behaviour in logins (e.g. brute-force attacks) is raised if detected via Kusto Query Language (KQL).
---
## ✅ Objectives Completed

- Coded a `/login` route of a Flask Python web application
- Published the application to App Service ( Linux ) on Azure
- allows diagnostic logging and connected to a Log Analytics Workspace
- pulsed-in-out Login data with KQL
- Formed an Azure Monitor alert on failed logins
---
## 💡 What I Learned

In this lab, I found out how to connect a Flask app to the monitoring systems of Azure to use security-driven logs monitoring and alerting. I experienced first-time working with:

- Setting up of diagnostic settings on Azure App Service
- Log forwarding to a Log Analytics Workspace
- Analysis of logs by writing KQL (Kusto Query Language)
- Generation of notification guidelines that to superimpose email notifications
  ---
## ⚠️ Challenges Faced

- **Log Delay**: When diagnostic options were turned on, logs became visible in Log Analytics after several minutes which led to confusion in the first days.
- I was looking forward to certain columns such as `LogLevel` which were not present and I was forced to look through the actual log schema with `search` queries to find the right table and columns.
- **Incorrect URLS**: I entered a missing App Service URL in my `.http` file, and I failed all tests until I changed it to the correct one.
**Flask Logging**: Setting Flask up to log to stdout explicitly had to be done in order to get errors to be captured correctly by Azure.
  ---
## 🔐 How I Would Improve This in a Real-World Scenario

- **IP Address Logging**: Record and log the IP address of a source of the login by each attack because this can enable tracking and blocking.
- **Rate Limiting** Enact a throttle to exclude multiple attempts of logins using the same IP.
- **Trusting CAPTCHA**: Enable CAPTCHA to minimize the amount of bot-based logins.
- **Sophisticated KQL**: Aggregation functions (ex. `summarize count() by bin(TimeGenerated, 5m), IPAddress) can be utilized to find patterns of brute-force in time.
- **Webhook or Logic App Alerts**: Webhook or Logic App alerts will be attended to and instead of just email, automated workflows (Slack, Teams or ticketing systems) can be integrated.
---
## 🔎 KQL Query Used for Alert
AppServiceConsoleLogs
| where _ResourceId contains "flask-login-monitor-8387" 
| where TimeGenerated > ago(15m)
| sort by TimeGenerated desc
---
## Demo Video

