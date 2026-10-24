class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        def date_to_day_of_year(date_str: str) -> int:
            month, day = map(int, date_str.split("-"))
            return sum(days_in_months[:month - 1]) + day
        
        start_date = max(arriveAlice, arriveBob)
        end_date = min(leaveAlice, leaveBob)
        
        if start_date > end_date:
            return 0
            
        return date_to_day_of_year(end_date) - date_to_day_of_year(start_date) + 1