# https://www.lifewithpython.com/2017/04/python-searching-large-files.html
from pathlib import Path
from stat import ST_SIZE

def search_files(path, size_min_in_byte):
    """指定されたパスの下にある指定されたサイズ以上のファイル名を一覧表示する
    """
    size_min_in_mb = size_min_in_byte << 20

    p = Path(path)

    # 指定されたパス以下のファイルを再帰的にチェックする
    # 指定されたサイズ以上のファイルは「10MB ファイル名」といった感じに表示する
    for file in p.iterdir():
        if file.is_dir():
            search_files(file, size_min_in_byte)
        elif file.is_file():
            size = file.stat().st_size
            if size >= size_min_in_mb:
                # resolve()を使って絶対パスを表示する
                print('{:.1f}MB\t{}'.format(size >> 20, file.resolve()))

if __name__ == '__main__':
    # Models以下にあるサイズが 5000MB 以上のファイルを表示する

    # スクリプトのディレクトリの絶対パスを取得
    root = Path(__file__)
    abs_root = root.resolve()
    parent = abs_root.parent

    size_in_mb = 80
    search_files(parent, size_in_mb)