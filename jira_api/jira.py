'''
file: jira.py
description: jira_api to fetch issues from Jira tool

:author: Vasanthakumar
'''

from jira import JIRA
from jira.exceptions import JIRAError
from pprint import pprint
import urllib3

class Jirahandler:
    def __init__(self, **kwargs):
        self.uname = ''
        self.pword = ''        
        self.issue_details = dict()
        self.is_logged_in = False
        self._update(**kwargs)
        self._login()
        
    def _update(self, **kwargs):        
        for key, val in kwargs.items():
            if key not in self.__dict__:
                continue
            self.__setattr__(key, val)

    def _login(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        options = {
            'server': 'https://jira.<org>.com',
            'verify': False,
             }
        print ("\nLogging into JIRA ...\n")
        try:
            self.jira = JIRA(options , basic_auth=(self.uname,self.pword))
            self.is_logged_in = True
        except JIRAError as e:
            if e.status_code == 401:
                print ("Login to JIRA failed. Check your username and password")

    def Fetch_issue(self, Issue_ids=[]):        
        for req_issue in Issue_ids:
            flag = False
            try:
                issue = self.jira.issue(req_issue)
            except JIRAError as e:
                if e.status_code == 404:
                    flag=True
            if flag:
                self.issue_details[req_issue] = 'None'
            else:
                i = issue.fields            
                self.issue_details[req_issue] = {"P-key" : i.project.key, "P-Name" : i.project.name, "Issue-Type" : i.issuetype.name,"Priority" : i.priority.name, "Labels" : i.labels,
                                                "Summary" : i.summary, "Reporter" :{"Name" : i.reporter.displayName,"E-mail" : i.reporter.emailAddress},
                                                "Assignee":{"Name" : i.assignee.displayName,"E-mail" : i.assignee.emailAddress}, "status" : i.status.name, "Description" : i.description}                      
        return (self.issue_details)


if __name__ == '__main__':
    user = "username"
    pwd = "userpwd"
    j = Jirahandler(uname = user, pword= pwd)
    if j.is_logged_in:
        issue_details=j.Fetch_issue(['*']) #projectkey-id
        pprint (issue_details)
