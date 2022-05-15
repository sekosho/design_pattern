try:
    b = [1,2,3,4,5]
    # b[7]
    a = 5 / 0
except IndexError as e:
    import traceback
    traceback.print_exc()
except Exception as e:
    print("Exception:",e,type(e))
    
else:
    # エラーのときは実行されない
    print("Else処理")

finally:
    # エラーでもじゃなくても必ず実行される
    # tryの中の変数を初期化させたいときやログ出力のときなどに使われる
    print("finally処理")

print("処理が完了しました")