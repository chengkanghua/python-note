# 前端模板
adminLTE:
- https://adminlte.io/themes/v3/index.html
- https://adminlte.io/themes/AdminLTE/index2.html

我们copy的是static/AdminLTE-master/starter.index
修改静态文件的引用方式

# modelform

## it表

**法1**
```python
# 来自张子俊

from django.forms import ModelForm
from django import forms
from django.forms import widgets as wid
from app01 import models

class ItModelForm(ModelForm):
    class Meta:
        model = models.It
        fields = "__all__"
    bootstrapClass_filter = ['it_start_time', 'it_end_time']
    it_start_time = forms.DateField(label="开始时间", widget=wid.DateInput(attrs={"class": "form-control", 'type': "date"}))
    it_end_time = forms.DateField(label="结束时间", widget=wid.DateInput(attrs={"class": "form-control", 'type': "date"}))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if name in self.bootstrapClass_filter:
                continue
            old_class = field.widget.attrs.get('class', "")
            field.widget.attrs['class'] = '{} form-control'.format(old_class)
            field.widget.attrs['placeholder'] = '请输入%s' % (field.label,)
```
**法2**
```python
from django.forms import ModelForm
from django import forms
from django.forms import widgets as wid
from app01 import models

class ItModelForm(ModelForm):
    class Meta:
        model = models.It
        fields = "__all__"
        # 法2
        labels = {
            "it_name": "项目名称",
            "it_desc": "项目描述",
            "it_start_tile": "项目开始时间",
            "it_end_tile": "项目结束时间",
        }
        error_messages = {
            "it_name": {"required": "不能为空"},
            "it_desc": {"required": "不能为空"},
            "it_start_tile": {"required": "不能为空"},
            "it_end_tile": {"required": "不能为空"},
        }
        widgets = {
            "it_name": wid.Input(attrs={"class": "form-control", "placeholder": "输入项目名称"}),
            "it_desc": wid.Textarea(attrs={"class": "form-control", "placeholder": "输入项目名称"}),
            "it_start_time": wid.DateInput(attrs={"class": "form-control", 'type': "date"}),
            "it_end_time": wid.DateInput(attrs={"class": "form-control", 'type': "date"}),
        }
```
# 模板语言

```html
<!-- 切片， 参数必须是 str -->
<td>{{ foo.api_url | slice:"10"}}</td>  
<!-- 截取指定长度字符，后续以点代替， 参数必须是int -->
<td title="{{ foo.api_url }}">{{ foo.api_url | truncatechars:10}}</td>
```


# django的下载逻辑

```python
from django.http import FileResponse
from django.http import StreamingHttpResponse

```

参考：https://www.cnblogs.com/Neeo/articles/11021972.html




# 关于复选框的操作
获取所有的选中状态的复选框：
```javascript
$("#chk1").find('input:checkbox').each(function() { //遍历所有复选框
 
    if ($(this).prop('checked') == true) {
 
        console.log($(this).val()); //打印当前选中的复选框的值
 
    }
 
});
 
function getCheckBoxVal(){ //jquery获取所有选中的复选框的值 
 
    var chk_value =[]; 
 
    $("#chk1").find('input[name="test"]:checked').each(function(){ //遍历，将所有选中的值放到数组中
 
        chk_value.push($(this).val()); 
 
    }); 
 
    alert(chk_value.length==0 ?'你还没有选择任何内容！':chk_value); 
 
} 
```
或者：
```javascript
$("#sure").click(function () {
    var arr = new Array();
    $.each($(".p1"), function (index, item) {
        // console.log(index, item)
        if ($(item).get(0).checked) {
            arr.push($(item).val())
        }
    });
    if (arr.length == 0) {
        // 说明用户未选中用例，需要给提示
        // console.log(2222222, "未选中", arr);
        $("#errorMsg").html("请勾选至少一个用例！");

    } else {
        // 编写后续的操作
    }
});
```







