date= {
  'year' : '2025',
  'month': '12',
  'day' : '31',
}

formatted = ''
part = ['year', 'month', 'day']

for par in part:
  formatted += date[par]
  if par != 'day':
    formatted += '-'

print("'",formatted,"'") # Вывод: 2025-12-31
