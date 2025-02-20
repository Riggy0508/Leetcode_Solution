// https://leetcode.com/problems/accounts-merge

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_graph=defaultdict(set)
        email_to_name={}

        for account in accounts:
            name=account[0]
            emails=account[1:]
            for email in emails:
                email_to_name[email]=name

                email_graph[emails[0]].add(email)
                email_graph[email].add(emails[0])


        seen=set()
        merged_account=[]

        def dfs(email,component):
            seen.add(email)
            component.append(email)

            for neighbor in email_graph[email]:
                if neighbor not in seen:
                    dfs(neighbor,component)


        for email in email_graph:
            if email not in seen:
                component=[]
                dfs(email,component)
                merged_account.append([email_to_name[email]]+sorted(component))

        return merged_account