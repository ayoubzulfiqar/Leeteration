class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        unique_canonical_emails = set()
        for email in emails:
            local_part, domain_part = email.split('@')

            # Process the local part:
            # 1. Ignore everything after the first '+'
            if '+' in local_part:
                local_part = local_part.split('+')[0]

            # 2. Remove all '.' characters
            local_part = local_part.replace('.', '')

            # Reconstruct the canonical email address
            canonical_email = local_part + '@' + domain_part
            unique_canonical_emails.add(canonical_email)

        return len(unique_canonical_emails)