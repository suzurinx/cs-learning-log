# 問題名
<!-- 問題のタイトルを簡潔に記載 -->
バリデーション
## 問題内容
<!-- 問題の概要、何を求められているかを自分の言葉で整理 -->
ラムダ関数を利用して、 与えられた email を評価するバリデーたを作成する。

## 実装ポイント
### 実装方針
<!-- 再帰 / ループ / DFS / BFS など、選んだアプローチと理由 -->
- ラムダ関数を引数として受け取り、評価結果によってメッセージを返す。
### 意識した制約・パフォーマンス
<!-- 実装時に気をつけた制約や、時間・空間効率をどう考慮したか -->
- すべてのバリデータは `O(n)` の文字列走査程度
### 難所・分岐・構造上の注意点
<!-- 実装中につまずいた部分、注意が必要だった構造や分岐条件など -->
- `validator` は関数そのものであり、**`validator(email)` のように呼び出さないと意味がない**。
- `" " in email` は逆で、「空白があったらダメ」→ `" " not in email` に修正した。
### 設計判断メモ（※なぜこの方法を選んだか）
<!-- 他の方法との比較・利点・設計上の意思決定を言語化 -->
- ラムダ関数の、お手軽さ、テストしやすや
## テストケース
<!-- 入力と期待される出力をセットで記載 -->
```python
emailValidation(doesNotStartWithAt, "@gmail.com")      # → Email is not correct.
emailValidation(doesNotStartWithAt, "kkk@gmail.com")    # → Email is correct.
emailValidation(doesNotHaveSpace, "Hello world")        # → Email is not correct.
emailValidation(doesNotHaveSpace, "Helloworld")         # → Email is correct.
emailValidation(hasUppercaseAndLowercase, "hello world")     # → Email is not correct.
emailValidation(hasUppercaseAndLowercase, "HELLO WORLD")     # → Email is not correct.
emailValidation(hasUppercaseAndLowercase, "Hello world")     # → Email is correct.
```

## 出力
<!-- 実際に得られた出力結果を記録 -->
```python
Email is not correct.
Email is correct.
Email is not correct.
Email is correct.
Email is not correct.
Email is not correct.
Email is correct.
```

## 気づき
<!-- 実装中・実行後に得た新しい知見や発見を記録。構文、挙動、制約など何でもOK -->
- `doesNotStartWithAt = lambda email: not email.startswith("@")`　この構文で `true`を返す流れがギクシャクす
- any() や all() は、イテラブル内の真偽チェックに便利
- validator が「関数」なので、そのままでは評価されないことに注意
- 関数呼び出しに () を忘れない

## 再訪メモ

### 不安な構文・表現
<!-- 曖昧だった構文や、処理の流れが読み切れなかった部分 -->
- any() の使い方（ループ生成が必要）
### 理解しきれなかった組み合わせの構文
<!-- 複数の構文が組み合わさった時に直感で読めなかったものなど -->
- 特になし
### 次に類似問題を解くときに注目したいポイント
<!-- 次回似た問題に出会ったときの指針。再利用したい構造など -->
- 標準メソッド（.islower() など）と属性（c.lowercase）の違いに注意

## 解いた日
2025-07-06
