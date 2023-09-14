from pathlib import Path

#フォルダ階層一層目を探索し、拡張子ごとに連番をつける。名前は親フォルダに順ずる。

def renamefiles(path):
    for afolder in Path(path).iterdir():
        if afolder.is_dir(): # もし階層であれば進む
            sufset = {i.suffix for i in Path(afolder).iterdir()} # 拡張子のセットを作る

            for suf in sufset: # 拡張子毎に処理する
                files = [i for i in Path(afolder).iterdir() if i.suffix in suf]
                i = 0

                for afile in files:
                #”フォルダ名_i”で名前変更
                    newname = afolder / str(afolder.name + '_' + '{0:03d}'.format(i) + afile.suffix) # 3桁の連番
                    afile.rename(newname)
                    i = i + 1
        else:
            continue

if __name__ == '__main__':
    # スクリプトのディレクトリの絶対パスを取得
    root = Path(__file__)
    #print(root)
    abs_root = root.resolve()
    #print(abs_root)
    parent = abs_root.parent
    #print(parent)
    renamefiles(parent)