class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        unique_addresses = set()
        for email in emails:
            local_name, domain_name = email.split('@')
            
            processed_local_name = []
            for char in local_name:
                if char == '+':
                    break
                if char == '.':
                    continue
                processed_local_name.append(char)
            
            canonical_email = "".join(processed_local_name) + '@' + domain_name
            unique_addresses.add(canonical_email)
            
        return len(unique_addresses)