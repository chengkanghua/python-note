# import xml.etree.cElementTree as ET
# decrypt_xml="""<xml>
# <AppId><![CDATA[wx89d0d065c7b25a06]]></AppId>
# <CreateTime>1648305909</CreateTime>
# <InfoType><![CDATA[component_verify_ticket]]></InfoType>
# <ComponentVerifyTicket></ComponentVerifyTicket>
# </xml>"""
#
# xml_tree = ET.fromstring(decrypt_xml)
# verify_ticket = xml_tree.find("ComponentVerifyTicket")
# if verify_ticket is None:
#     print("11111")
#     exit()
#
# verify_ticket_text = verify_ticket.text
# if not verify_ticket_text:
#     print(222222)
#     exit()
# print(verify_ticket_text)


import re
text = "您好，您已购买成功。\n\n{{productType.DATA}}：{{name.DATA}}\n购买数量：{{number.DATA}}\n{{remark.DATA}}"

data = re.findall("{{(\w+)\.DATA}}",text)
print(data)

text = "{{first.DATA}}\n订单详情：{{keyword1.DATA}}\n订单编号：{{keyword2.DATA}}\n物流公司：{{keyword3.DATA}}\n物流单号：{{keyword4.DATA}}\n发货时间：{{keyword5.DATA}}\n{{remark.DATA}"
data = re.findall("{{(\w+)\.DATA}}",text)
print(data)
