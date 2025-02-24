letter = ''' Dear <|Name|>,
            You are selected!
            <|Date|>'''
print(letter.replace("<|Name|>", "Ved").replace("<|Date|>", "18th September 2022")) #This is chaining
