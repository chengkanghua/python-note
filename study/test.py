def clean(self):
    print("---",self.cleaned_data)
    # if self.cleaned_data["password"]==self.cleaned_data["repeat_password"]:     
    # 报错原因：self.cleaned_data是干净数据，如果页面没有输入内容，则self.cleaned_data没有password。
    # 改如下：
    if self.cleaned_data.get("password")==self.cleaned_data.get("repeat_password"):
        return self.cleaned_data
    ​else:
        raise ValidationError("两次密码不一致")