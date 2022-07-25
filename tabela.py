from prettytable import PrettyTable

# Criando uma tabela no output usando a biblioteca prettytable.

table = PrettyTable()
table.field_names = ['Nome', 'Sexo', 'Idade']
table.add_row(['Dione','M',31])
table.add_row(['Francine','F',25])
table.add_row(['Zeus','M',0.7])

print(table)

#output

'''+----------+------+-------+
|   Nome   | Sexo | Idade |
+----------+------+-------+
|  Dione   |  M   |   31  |
| Francine |  F   |   25  |
|   Zeus   |  M   |  0.7  |
+----------+------+-------+'''