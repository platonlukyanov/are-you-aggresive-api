import joblib
import pandas as pd
df = pd.read_csv("data.csv", delimiter=";", warn_bad_lines=True, error_bad_lines=False)
df = df[["Текст", "стилистика коммента"]]
df["стилистика коммента"].replace({
    'издевка': 'агрессия',
    'оскорбление героев поста': 'агрессия',
    'смайлы как законченная мысль': 'культурно',
    'оскорбление участника дискуссии': 'агрессия',
    'юмор/ирония': 'культурно',
    'изображение': None,
    'видео': None,
    'ссылка на внешний ресурс': None,
    'аудио': None,
    'стикер': None,
    'комментарий удален ': None,
    'не определено': None
}, inplace=True)
df = df[df["Текст"].notnull() & df["стилистика коммента"].notnull()]
joblib.dump(df, "pickles/df.pkl")
