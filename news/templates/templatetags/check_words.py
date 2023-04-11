def censor(self):
    if not isinstance(self.text, str):
        raise ValueError('Можно применить только к строке!')  # Если строка, то в ней уже ищем плохие слова
    if 'редиск' or 'баран' in self.text:
        self.text = self.text.replace('редиск', 'р******')
        self.text = self.text.replace('баран', 'б****')
        return f'{self.text}'
