class Solution:
    def latestTime(self, s: str) -> str:
        res_list = list(s)

        # Handle hours (HH)
        # Determine the first digit of hours (res_list[0])
        if res_list[0] == '?':
            # If the second digit of hours (res_list[1]) allows for "1X" (i.e., '?' or '0' or '1'),
            # we should aim for '1' to maximize the hour.
            if res_list[1] == '?' or res_list[1] in ['0', '1']:
                res_list[0] = '1'
            # Otherwise (res_list[1] is '2' through '9'), res_list[0] must be '0'
            # to keep the hour within 00-11 range (e.g., "09" is valid, "19" is not).
            else:
                res_list[0] = '0'
        
        # Determine the second digit of hours (res_list[1])
        if res_list[1] == '?':
            # If the first digit of hours is '0', we can maximize the second digit to '9' (e.g., "09").
            if res_list[0] == '0':
                res_list[1] = '9'
            # If the first digit of hours is '1', the second digit can only be '0' or '1' to stay within 00-11.
            # To maximize, we set it to '1' (e.g., "11").
            elif res_list[0] == '1':
                res_list[1] = '1'

        # Handle minutes (MM)
        # Determine the first digit of minutes (res_list[3])
        if res_list[3] == '?':
            # To maximize minutes, the tens digit should always be '5' (e.g., "XX:5X").
            res_list[3] = '5'

        # Determine the second digit of minutes (res_list[4])
        if res_list[4] == '?':
            # To maximize minutes, the units digit should always be '9' (e.g., "XX:X9").
            res_list[4] = '9'
        
        return "".join(res_list)