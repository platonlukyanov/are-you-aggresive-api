Unfortunately, my training data is not public as the owner set.
But you can use your own data. There must be 2 columns: 'Текст' and 'стилистика коммента'.
'Текст' is the text of the comment and values of 'стилистика коммента' could be 'агрессия' or 'культурно' according whether text is aggressive or not. 

After that:
1. Install requirements by command `pip install -r requirements.txt`
1. run parsedata.py
2. run learn.py 
3. run command `uvicorn server:app --reload`
4. That's it you just started this application!