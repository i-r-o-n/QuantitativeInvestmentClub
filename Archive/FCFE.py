# FCFE based on EBIT - (capex - depreciation) - (change in working capital) -(principal payments-debt issuance)

class Stock:
    def __init__(self, capex, depreciation, CIWC, principalPayments, debtIssuance, EBIT):
        #make everything local
        self.capex = capex #Capital Expenditure
        self.depreciation = depreciation #Depreciation, possibly total depreciation (can be negative)
        self.CIWC = CIWC #Change in Working Capital
        self.principalPayments = principalPayments
        self.debtIssuance = debtIssuance #TODO: Insurance or Issuance
        self.EBIT = EBIT #Earnings before interest and taxes
        self.FCFE = self.EBIT - (self.capex - self.depreciation) - self.CIWC - (self.principalPayments - self.debtIssuance)