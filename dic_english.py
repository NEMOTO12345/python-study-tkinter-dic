import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.geometry('600x400')
root.title('英単語辞書')

#調べる
entry1 = tk.Entry(width=40)
entry1.pack()

#イベント発生
button2 = tk.Button(text="調べる")





dic = {}
with open("data/ejdict-hand-utf8.txt" , 'r', encoding='utf-8') as f:
    for line in f:
        temp = line.strip().split('\t')
        dic[temp[0]] = temp[1]
        

#何度も検索できるように繰り返し文に入れる
#繰り返し文に入れるとテキストファイルの読み込み→辞書作成が一回で良い
#何も入力されなければプログラム終了
        
def serach(event):
    result.delete('1.0', 'end -1c')
    entry1_value = entry1.get()
    i = dic.keys()
    for line in i:
        while True:
            if line == entry1_value:
                result.insert('1.0',dic[line])
                break
            elif line == "":
                result.insert('1.0',"入力してください")
                break
            else:
                break
    # while True:
    #     name = entry1_vlue
    #     name = name.lower() #大文字入力されることがあるので小文字に変換
    #     if name == "":
    #         break
    #     #単語登録がないものが入力されたらKeyErrorが起こるのでエラー処理
    #     try:
    #         entry2.insert(tk.END,dic[name])
    #     except KeyError:
    #         entry2.insert(tk.END,f"{name}は見つかりません")

button2.bind('<Button-1>',serach)
button2.pack()

#出力



result = tk.Text(width=60,height=2,)
result.pack()




root.mainloop()




#授業で配った辞書データは以下からDLできます。
#今回はテキスト形式をダウンロードして配布しました。
#https://kujirahand.com/web-tools/EJDictFreeDL.php
#最終章でデータベースを学習したあとはsqlite形式でも同じようなことができます
#sqliteのほうが挙動は早い（とはいえ読み込んでいるテキストデータは4万行以上あるわりには早いと感じると思います）