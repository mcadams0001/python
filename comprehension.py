class InputTemplate:
    def __init__(self, inputId:int, countryCode: str) -> None:
        self.inputId = inputId
        self.countryCode = countryCode
    
    def __str__(self) -> str:
        return f'InputTemplate id:${self.inputId} countryCode:${self.countryCode}'
    
    def __repr__(self) -> str:
        return f'InputTemplate (id:${self.inputId} countryCode:${self.countryCode})'



country_code = ['EUR','USD','GBP']
inputTemplates = [InputTemplate(1, 'EUR'), InputTemplate(2, 'USD')]

inputTemplates2 = {it for it in inputTemplates if it.countryCode in country_code}

print(inputTemplates2)
