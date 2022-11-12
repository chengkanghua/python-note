


from deepdiff import DeepDiff


d1 = {"param":{"skuId":123,"num":10}, "status": "0"}
d2 = {"param":{"skuId":123,"num":10}, "status": "1"}

print(DeepDiff(d1, d2))