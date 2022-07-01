import hashlib

s = '101_3_2.0+/api/v4/search_v3?t=general&q=%E5%95%8A%E5%93%88%E5%93%88%E5%93%88%E5%93%88%E5%93%88&correction=1&offset=0&limit=20&filter_fields=&lc_idx=0&show_all_topics=0&search_source=Normal+"ALDZ2_r0ExKPTi0pK29fzASLbErLqovVVMM=|1603356933"'
md = hashlib.md5()
md.update(s.encode('utf-8'))
res = md.hexdigest()
print(res)
