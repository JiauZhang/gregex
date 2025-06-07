import re
from gregex import char, repeat
from gregex.set import Set
from gregex.group import Group

class TestGregex:
    text = '''### Install
```shell
pip install nnops
```

### Example
```python
import nnops, nnops.tensor

x = nnops.tensor.randn(2, 3)
y = nnops.tensor.randn(3, 4)

x = (x + 2) * 3
y = (y - 4) / 5
z = x @ y # [2, 4]
```

### Sponsor
<table align="center">
    <thead>
        <tr>
            <th colspan="2">公众号</th>
        </tr>
    </thead>
    <tbody align="center" valign="center">
        <tr>
            <td colspan="2"><img src="https://jiauzhang.github.io/ghstatic/images/ofa_m.png" style="height: 196px" alt="AliPay.png"></td>
        </tr>
    </tbody>
    <thead>
        <tr>
            <th>AliPay</th>
            <th>WeChatPay</th>
        </tr>
    </thead>
    <tbody align="center" valign="center">
        <tr>
            <td><img src="https://jiauzhang.github.io/AliPay.png" style="width: 196px; height: 196px" alt="AliPay.png"></td>
            <td><img src="https://jiauzhang.github.io/WeChatPay.png" style="width: 196px; height: 196px" alt="WeChatPay.png"></td>
        </tr>
    </tbody>
</table>
'''

    def test_title(self):
        pattern = char.MATCH_BEGIN + Group(name='head'
            ).add_pattern('#' + repeat.ONE_OR_MORE
            ).pattern + char.WHITESPACE + repeat.ONE_OR_MORE + Group(name='title'
            ).add_pattern(char.WORD + repeat.ONE_OR_MORE).pattern
        m = re.match(pattern, self.text)
        assert m is not None and m.lastindex == 2
        assert m.group('head') == '###' and m.group('title') == 'Install'

    def test_code_block(self):
        pattern = '`' + repeat.exactly(3) + Group(name='lang'
            ).add_pattern(char.WORD + repeat.ZERO_OR_MORE).pattern + Group(name='code'
            ).add_pattern(char.SET_ALL + repeat.ZERO_OR_MORE).pattern + '`' + repeat.exactly(3)
        m = re.findall(pattern, self.text)
        assert m is not None