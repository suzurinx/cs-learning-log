# CLIプログラム用：基本の main 関数テンプレート

## 🔧 目的
- コマンドライン引数を受け取り、バリデーション・処理分岐・実行を制御する
- 小規模〜中規模のCLIスクリプトで汎用的に利用できる鉄板構造

---

## 🧩 main関数テンプレート（Python）

```python
import sys

def main():
    # 引数を受け取る（ファイル名以外すべて：コマンド + パラメータ）
    args = sys.argv[1:]

    # 引数の妥当性をチェック（コマンド名や引数数など）
    ok, message = validate_args(args)
    if not ok:
        print(message)
        sys.exit(2)  # User error（ユーザーの入力ミス）

    # コマンドと引数に分解
    command, params = args[0], args[1:]

    try:
        dispatch(command, params)  # 実処理に委譲
    except Exception as error:
        print(f"エラー: {error}")
        sys.exit(1)  # 実行時エラー（ファイル操作・処理系のバグなど）