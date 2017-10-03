import json

from jira.client import JIRA

options  = {'server':'IP_ADDRESS'}

jira = JIRA(options,basic_auth=('xxxxx', 'xxxx'))

projects=jira.projects()

issue=jira.create_issue(project={'key':'DBCAMP1'},summary='Testing from API',description='Test Description',issuetype={'name':'Story'}, assignee={'name': 'devopscave'} )
