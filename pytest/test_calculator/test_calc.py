import pytest
import yaml

from pythoncode.Calculator import Calculator


def get_datas():
    # safe_load: yaml to python object
    # safe_dump: python to yaml
    with open("./datas.yml") as f:
        result = yaml.safe_load(f)

        add_P0_datas = result.get("add").get("P0").get('datas')
        add_P0_ids = result.get("add").get("P0").get('ids')

        print(f"P0 datas {add_P0_datas}")
        print(f"P0 ids {add_P0_ids}")
    # P0 级别的datas [[1, 1, 2], [-0.01, 0.02, 0.01], [10, 0.02, 10.02]]
    # P0 级别的ids ['2 int', '2 float', 'int+float']
    return [add_P0_datas, add_P0_ids]


class TestCalculator:
    def setup_class(self):
        print("Instantiate a calculator object.")
        self.calc = Calculator()

    def setup(self):
        print("start calculating")

    def teardown(self):
        print("end calculating")

    def teardown_class(self):
        print("end testing")

    # smoke test cases
    @pytest.mark.P0
    # 需要至少两个参数，第一参数是字符串- 里面存放要传递的参数，以逗号隔开
    # 第二参数，就是我们要传递的数据序列（可以列表，可以元组），每个序列里存放一组数据
    @pytest.mark.parametrize('a,b, expect',
                             [[1, 1, 2], [-0.01, 0.02, 0.01], [10, 0.02, 10.02]],
                             ids=['整型', '浮点型', '整型+浮点型'])
    def test_add0(self, a, b, expect):
        # test add
        result = self.calc.add(a, b)
        print(result)
        assert result == expect

    # valid boudary value
    @pytest.mark.P1
    @pytest.mark.parametrize('a,b, expect',
                             [[98.99, 99, 197.99],
                              [99, 98.99, 197.99],
                              [-98.99, -99, -197.99],
                              [-99, -98.99, -197.99]],
                             ids=['边界值-正1', '边界值-正2', '边界值-负1', '边界值-负2'])
    def test_add1(self, a, b, expect):
        result = self.calc.add(a, b)
        assert result == expect

    # 无效边界值
    @pytest.mark.P1
    @pytest.mark.parametrize('a,b, expect',
                             [[99.01, 0, "参数大小超出范围"],
                              [-99.01, -1, "参数大小超出范围"],
                              [2, 99.01, "参数大小超出范围"],
                              [1, -99.01, "参数大小超出范围"],
                              ],
                             ids=['边界值-参数超出范围1', '边界值-参数超出范围2',
                                  '边界值-参数超出范围3', '边界值-参数超出范围4'])
    def test_add2(self, a, b, expect):
        result = self.calc.add(a, b)
        assert result == expect

    # 异常情况处理
    @pytest.mark.P1
    @pytest.mark.parametrize('a,b,errortype', [
        ["文", 9.3, TypeError],
        [4, "字", TypeError]
    ])
    def test_add3(self, a, b, errortype):
        # pytest 封装的一种处理异常的方式
        with pytest.raises(errortype) as e:
            result = self.calc.add(a, b)

        print(e.typename)
        # try:
        #     result = self.calc.add("中",9.3)
        # except TypeError as e :
        #     print("异常信息：")
        #     print(e)