import os
poke_type = ('红桃', '黑桃', '梅花', '方块')
poke_set = set()
poke_set.update({('小王', 0.5), ('大王', 0.5)})
{(k + i, 0.5) for k in poke_type for i in ['J', 'Q', 'k', 'A']}
poke_set.update({(k + i, 0.5) for k in poke_type for i in ['J', 'Q', 'K', 'A']})
poke_set.update({(k + str(i), i) for k in poke_type for i in range(2, 11)})
# for k in poke_type:
#     for i in ['j','Q','k','A']:
#         poke_set.update({(k+i,0.5)})
print(poke_set)

user_dict = {
    "zhangkai": {'poke': [poke_set.pop()], 'score': 0, 'msg': ''},
    "likai": {'poke': [poke_set.pop()], 'score': 0, 'msg': ''},
    "wangkkai": {'poke': [poke_set.pop()], 'score': 0, 'msg': ''},
}
# print(user_dict)

for i in user_dict:
    while True:
        user_dict[i]['score'] = sum([i[1] for i in user_dict[i]['poke']])
        choice = input('尊敬的用户[{}]，你现在手里有牌[{}]，得分[{}]，要牌y/不要n\n请根据需求输入: '.format(
            i,
            ' '.join([i[0] for i in user_dict[i]['poke']]),
            sum([i[1] for i in user_dict[i]['poke']])
        )).strip()
        if not choice:
            continue
        if choice.upper() == 'N':
            os.system('clear')  # windows 清屏指令cls，Linux请使用 clear
            break

        user_dict[i]['poke'].insert(0, poke_set.pop())
        user_dict[i]['score'] = sum([i[1] for i in user_dict[i]['poke']])
        if user_dict[i]['score'] > 11:
            print('尊敬的用户[{}],你手里有牌[{}],得分是[{}]，大于11点，爆掉了，根据规则，我们不带你玩了!!!'.format(
                i,
                ' '.join([i[0] for i in user_dict[i]['poke']]),
                user_dict[i]['score']
            ))
            user_dict[i]['msg'] = '实际得分[{}]，大于11点，爆掉了'.format(sum([i[1] for i in user_dict[i]['poke']]))
            user_dict[i]['score'] = 0
            break

print('选牌完毕，正在计算得分.....')
for i in user_dict:
    print('尊敬的用户[{}]，你的总得分是[{}]'.format(i, user_dict[i]['score']), user_dict[i]['msg'])

# 计算出赢家
winner_user = max(user_dict, key=lambda x: user_dict[x]['score'])
print("最后的赢家是: {},得分是: {}".format(winner_user, user_dict[winner_user]['score']))

