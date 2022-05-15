# インスタンス変数、クラス変数


class Sample:
    class_val = "class val"

    def set_val(self):
        self.instance_val = "instance val"

    def print_val(self):
        print(f"クラス変数：{self.class_val}")
        print(f"インスタンス変数：{self.instance_val}")


instance_a = Sample()
instance_a.set_val()
print(instance_a.instance_val)
instance_a.print_val()
print(Sample.class_val)
print(instance_a.__class__.class_val)

instance_b = Sample()
instance_b.__class__.class_val = "class val changed"  # クラス変数は書き換えできる。
print(instance_a.__class__.class_val)  # クラス変数はインスタンス間で同じ値が共有される
print(id(instance_a.__class__.class_val))
print(id(instance_b.__class__.class_val))
