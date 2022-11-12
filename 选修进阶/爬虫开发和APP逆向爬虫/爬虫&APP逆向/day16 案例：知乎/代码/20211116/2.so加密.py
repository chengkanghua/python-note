import hmac
from hashlib import sha1

v23 = "1355" + "2" + "app_build=1031&app_version=5.32.1&bt_ck=1&bundle_id=com.zhihu.android&cp_ct=8&cp_fq=2016000&cp_tp=0&cp_us=100.0&d_n=Redmi%208A&fr_mem=202&fr_st=42809&latitude=0.0&longitude=0.0&mc_ad=E0%3A1F%3A88%3AAA%3AB3%3A39&mcc=cn&nt_st=1&ph_br=Xiaomi&ph_md=Redmi%208A&ph_os=Android%2010&ph_sn=unknown&pvd_nm=%E4%B8%AD%E5%9B%BD%E8%81%94%E9%80%9A&tt_mem=256&tt_st=51140&tz_of=28800" + "1636642368"

hmac_code = hmac.new("dd49a835-56e7-4a0f-95b5-efd51ea5397f".encode('utf-8'), v23.encode('utf-8'), sha1)
res = hmac_code.hexdigest()
print(res) # aba4022b4bc3eabd046e0eabd443e59585157c34
# aba4022b4bc3eabd046e0eabd443e59585157c34
