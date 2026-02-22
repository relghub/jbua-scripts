import make
import makedata

print("Вітаємо!\nПерелік файлів:\n0. Fix\n1. GeoImages\n2. GeoQuestions\n3. Hop\n4. Impostor\n5. ImpostorImages\n6. ImpostorStatements\n7. Loop\n8. Year\n9. Усі\nОберіть категорію питань для обробки")
file_i = int(input())
print("0. Зробити головні джети\n1. Зробити папки\nЩо бажаєте зробити?")
task = int(input())
match task:
    case 0:
        make.make_jet(file_i)
    case 1:
        makedata.make_folders(file_i)
