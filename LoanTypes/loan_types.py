def get_loan_type(purpose: str, amount: float) -> str:
    purpose_lower = purpose.lower()

    if purpose_lower in ['housing', 'real estate'] and amount >= 100000:
        return "Mortgage Loan"
    elif purpose_lower in ['vehicle', 'car'] and 5000 <= amount <= 75000:
        return "Auto Loan"
    elif purpose_lower in ['personal', 'debt consolidation'] and amount <= 50000:
        return "Personal Loan"
    elif purpose_lower in ['business', 'startup'] and amount > 50000:
        return "Business Loan"
    elif purpose_lower == 'education' and amount <= 150000:
        return "Student Loan"
    else:
        return "Unclassified Loan"

loan1_type = get_loan_type("housing", 250000)
loan2_type = get_loan_type("car", 30000)
loan3_type = get_loan_type("personal", 15000)
loan4_type = get_loan_type("startup", 100000)
loan5_type = get_loan_type("education", 75000)
loan6_type = get_loan_type("vacation", 5000)
loan7_type = get_loan_type("personal", 60000)
loan8_type = get_loan_type("housing", 50000)
loan9_type = get_loan_type("vehicle", 80000)
loan10_type = get_loan_type("business", 40000)