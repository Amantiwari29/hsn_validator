import pandas as pd

class HSNValidator:
    def __init__(self, filepath):
        self.hsn_data = pd.read_csv(filepath, dtype=str)
        self.hsn_data['HSNCode'] = self.hsn_data['HSNCode'].str.strip()

    def is_valid_format(self, code):
        return code.isdigit() and len(code) in [2, 4, 6, 8]

    def validate_code(self, code):
        if not self.is_valid_format(code):
            return {"code": code, "valid": False, "reason": "Invalid format"}

        match = self.hsn_data[self.hsn_data['HSNCode'] == code]
        if not match.empty:
            return {
                "code": code,
                "valid": True,
                "description": match.iloc[0]['Description']
            }
        return {"code": code, "valid": False, "reason": "Code not found"}

    def hierarchical_validation(self, code):
        hierarchy = [code[:i] for i in [2, 4, 6, 8] if i <= len(code)]
        results = [self.validate_code(c) for c in hierarchy]
        return results
